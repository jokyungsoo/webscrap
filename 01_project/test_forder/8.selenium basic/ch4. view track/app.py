from selenium import webdriver 
import time
from selenium.webdriver.common.by import By 
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

query = "python flask"
target_blog_link = "https://salguworld.tistory.com/27"
many_query = ["python flask", "python selenium"]
many_target_blog_link = [
    "https://salguworld.tistory.com/27",
    "https://cafe.naver.com/hacosa/270984?art=ZXh0ZXJuYWwtc2VydmljZS1uYXZlci1zZWFyY2gtY2FmZS1wcg.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjYWZlVHlwZSI6IkNBRkVfVVJMIiwiY2FmZVVybCI6ImhhY29zYSIsImFydGljbGVJZCI6MjcwOTg0LCJpc3N1ZWRBdCI6MTcwNTY4MTg4MDY1Nn0.p9Pa_MYzsVRQfithqHDrmCFOD5T-X3jyQ8c7njay0Oc"
    ]

for query, target_blog_link in zip(many_query, many_target_blog_link):
    search_link = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={query}"
    driver.get(search_link)
    time.sleep(2)

    link_selector = f'a[href^="{target_blog_link}"]'
    now_rank = -1
    # 예외처리 구문
    BLOG_FOUND = False
    for _ in range(7): #최대 7번 하위 랭크 블로그 글을 불러오게 하겠습니다.
        try:
            Elements = driver.find_element(By.CSS_SELECTOR, link_selector)
            while True:
                New_Elements = Elements.find_element(By.XPATH, "./..")
                now_rank = New_Elements.get_attribute("data-cr-rank")
                if now_rank != None:
                    print(f"{search_link} / {now_rank} : 타겟 블로그의 랭크를 찾았습니다.")
                    BLOG_FOUND = True
                    break
        
                Elements = New_Elements
            if BLOG_FOUND:
                break

        except:
            # print("타겟 블로그의 랭크를 찾았습니다. -> 스크롤하겠습니다.")
            driver.execute_script("window.scrollBy(0,10000);")
            time.sleep(3) # 새로운 글들 로딩하는데 기다려주세요.
        print(f"{search_link} / {now_rank} : 타겟 블로그의 랭크를 찾지 못했습니다.")
input()