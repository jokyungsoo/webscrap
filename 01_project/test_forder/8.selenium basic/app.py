from selenium import webdriver 
import time
from selenium.webdriver.common.by import By 
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
# 1. 웹 브라우저 주소창을 컨트롤하기 드라이버.get
driver.get("https://www.naver.com")
time.sleep(3)

# 2-1 요소를 찾아서  Copy 해옴. 실제 웹 브라우저 + 개발자 도구
CSS_selector = "#feed > div.ContentHeaderView-module__content_header___nSgPg"

# 2-2. 찾아온 요소를 find_element 로 가져오기 -> 상자(변수)에 담기
group_navigation = driver.find_element(By.CSS_SELECTOR, CSS_selector)

# 3-1. 데이터를 가져오기
print(group_navigation.text)

# 3-2. 요소를 클릭하기[액션]
group_navigation.click()
input()