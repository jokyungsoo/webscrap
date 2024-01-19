from selenium import webdriver 
import time
from selenium.webdriver.common.by import By 
import chromedriver_autoinstaller
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.get("https://naver.com")
time.sleep(1)

# 3 Driver Wait
# 3-1 3초때 로딩이 끝나서,  element가 찾아짐.
# 3-2 30초까지는 기다리겠음.
# 3-3 30초가 넘어가면 에러던짐.
try:
    selector ="#newsstand > div.ContentHeaderView-module__content_header___nSgPg > div > ul > li:nth-child(2) > a"
    WebDriverWait(driver, 5).untill(EC.presence_of_element_located(
        By.CSS_SELECTOR, selector
    ))
except:
    print("예외 발생, 예외 처리  코드 실행하기")
print("엘리먼트 로딩 끝")
print("다음 코드 실행")
input()




# # 2. browser information
# # 2-1. title ~ 웹 사이트의 타이틀 가지고옴
# title = driver.title
# print(title, "이 타이틀이다.")


# # 2-2 current_url  주소창을 그대로 가지고옴
# now_addr = driver.current_url
# print(now_addr, "가 현재 주소다.")


# if "nid.naver.com" in now_addr:
#     print("지금은 로그인 하는 로직이 필요함")
# else:
#     print("내가 계획한 로직 그대로 실행하면됌")
# input()




# 1. navigation 네비게이션 관련 툴
# # 1.1 get() 원하는 페이지로 이동하는 함수
# driver.get("https://www.naver.com")
# time.sleep(1)
# driver.get("https://google.com")

# # 1-2 back() - 뒤로가기
# driver.back()
# time.sleep(2)

# # 1-3 forward() - 앞으로 가기
# driver.forward()
# time.sleep(2)

# # 1-4 refresh() - 페이지 새로고침
# driver.refresh()
# time.sleep(2)
# print("동작끝")
# input()