import numpy,requests,time,os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver 
try:
    os.system("cls")
except:
    os.system("clear")
print("[+] script started")
heading=[]
h=[]
def data():
    heading=[]
    driver.implicitly_wait(4)
    container=driver.find_elements(by="xpath",value="//h2")
    print("[+] Processing data....")
    for i in container:
        heading_=i.text
        heading.append(heading_)
    pop=driver.find_elements(by="xpath",value='//div[@class="pop-title"]')
    for i in pop:
        po=i.text
        heading.append(po)
    print(numpy.array(heading))
    heading=[]
try:
    a=requests.get("https://thehackernews.com")
    time.sleep(4)
    if "200" in str(a):
        print("[+] we have net connection")
        
        path=" "# add path
        website="https://thehackernews.com"
        service=Service(executable_path=path)
        option=Options()
        # option.headless=True
        option.add_experimental_option('excludeSwitches',['enable-logging'])
        driver=webdriver.Chrome(service=service,options=option)
        driver.get(website)
        print("[+] Finding website")
        time.sleep(4)
        data()
        # print(numpy.array(h))
        time.sleep(9)
        while True:
            l=["yes","y","no","n"]
            print(l)
            ask=input("[+] Do you want more:")
            if ask not in l:
                print("Invaild")
                ask=input("[+] Do you want more:")
            else:
                if ask in ["n","no"]:
                    break
                else:
                    driver.implicitly_wait(7)
                    driver.find_element(by="xpath",value='//a[@class="blog-pager-older-link-mobile"]').click()
                    data()
        
        driver.close()
        
except requests.exceptions.ConnectionError: 
    print("No internet")


