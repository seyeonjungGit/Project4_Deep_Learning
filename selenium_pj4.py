import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

# 크롬드라이버
driver =  webdriver.Chrome(executable_path='chromedriver')
# lis = ['2021-22-fall-winter', '2020-21-fall-winter'] 
# lis = ['2019-20-fall-winter-2','201819-fall-winter'] # --> 115~
# lis = [ '2017-fall-winter', '201617-fall-winter'] # --> 230~

# lis = ['2021-spring-summer', '2020-spring-summer'] 
# lis = ['2019-spring-summer'] # 116~
# lis = ['2018-spring-summer'] # --> 231~
lis = ['2017-spring-summer','2016ss'] # --> 348~

for l in lis:
    url = 'https://www.marieclairekorea.com/category/runway/?noCache=&city=&designer=&season={}'.format(l)

    driver.get(url)
    time.sleep(4)

    SCROLL_PAUSE_TIME = 4
    # 스크롤 끝까지 내리는 코드
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_element_by_css_selector(".fusion-load-more-button.fusion-blog-button.fusion-clearfix").click() #이부분만 바꿔주면 ㅗ딘다. 
            except:
                break
        last_height = new_height

    # 이 페이지 내의 이미지들을 리스트 형태로 받아온다. 
    images = driver.find_elements_by_css_selector(".fusion-rollover-gallery")
    count = 348
    for image in images:
        i = image.get_attribute("href")  # 이미지 주소 빼내기.
        urllib.request.urlretrieve(i, str(count) + ".jpg")  # 사진을 저장한다.
        count = count + 1

driver.close()