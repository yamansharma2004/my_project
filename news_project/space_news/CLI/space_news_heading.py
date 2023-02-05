from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 
import requests 
import time
print("[+] Printing all the heading")
try:
    a=requests.get("http://google.com")
    if "200" in str(a):
        heading_list=[]
        link=[]
        website="https://spacenews.com"
        path="" # add the path for chromedriver.exe
        service=Service(executable_path=path)
        options=Options()
        options.headless=True
        options.add_experimental_option('excludeSwitches',['enable-logging'])
        driver=webdriver.Chrome(service=service,options=options)
        driver.get(website)
        contanner=driver.find_elements(by="xpath",value='//h2/a')
        for i in contanner:
            time.sleep(4)
            print(": "+i.text)
        driver.close()
except requests.exceptions.ConnectionError: 
    print("No internet")
except KeyboardInterrupt:
    print("Come again")
