# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 17:07:30 2022

@author: Windows 10
"""

#%%
from selenium import webdriver
import time
from selenium.webdriver import ChromeOptions, ActionChains
from selenium.webdriver.common.by import By
import re
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from retrying import retry  # 需第三方库，需pip进行安装

#retry(wait_fixed=10, stop_max_attempt_number=1)

#get直接返回，不再等待界面加载完成
# desired_capabilities = DesiredCapabilities.CHROME
# desired_capabilities["pageLoadStrategy"] = "none"

# 添加参数
options = webdriver.ChromeOptions()

options.add_argument('--headless')
# options.add_argument('--no-sanbox')

# options.add_experimental_option('excludeSwitches', ['enable-automation'])


# options.add_argument("--disable-blink-features=AutomationControlled")
#options.page_load_strategy = 'none'

driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()

# driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#     "source": """
#                 Object.defineProperty(navigator, 'webdriver', {
#                   get: () => undefined
#                 })
#               """
# })



# 解决特征识别
script = 'Object.defineProperty(navigator, "webdriver", {get: () => undefined,});'
driver.execute_script(script)
 
# time.sleep(1)

# await page.evaluate(
#         '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')```

# 创建WebDriver对象

#%%
URL='http://www.boqii.com/baike/cat/'
driver.get(URL) #用模拟浏览器打开网页
#%%
twiceclass=driver.find_element(By.ID,'content').find_elements(By.CLASS_NAME,'fl_tit')##每页每条数据的网址
tcurl=[]
atcurls=[]
for i in twiceclass:
    url=i.find_element(By.TAG_NAME,'a').get_attribute('href')
    #i.click()   
    #time.sleep(1)
    tcurl.append(url)
    #atcurls.append(tcurl)
#%%

start_time = time.time()
# adbq=[]
# ayjbq=[]
aejbq=[]
aurls=[]
abt=[]
#azy=[]
awzny=[]
#starturl=tcurl[0]#读取每个一级分类的主页
#originurl=tcurl[0]
starturl='http://www.kaolaseo.com/seo/list_11_17055.html'
#cleanurl=re.findall(r'[/]$',originurl)
#originurl=originurl.replace(cleanurl[0],'')
# starturl=starturl.replace(cleanurl)
driver.get(starturl)
print(driver)
print(type(driver))
#首页
firstpage = int(re.findall(r'\d+',starturl)[1])
# if firstpage==[]:
#     firstpage=1
# else:
#     firstpage=int(firstpage[0])

#末页
# endurl=driver.find_element(By.ID,'content').find_element(By.ID,'page').find_elements(By.TAG_NAME,'a')
# endurl=endurl[-2].get_attribute('href')
endurl='http://www.kaolaseo.com/seo/list_11_24753.html'
finalpage = int(re.findall(r'\d+',endurl)[1])
# finalpage = 3


for page in range(firstpage,finalpage+1):
    print(' ',page)

    
    #comment = driver.find_element(By.XPATH,'/html/body/div[4]/div/div[1]/div[1]/div[2]/div[1]/a').text
    awzurl=driver.find_element(By.CLASS_NAME,'art_leftbox').find_element(By.TAG_NAME,'ul').find_elements(By.TAG_NAME,'a')#每页每条数据的网址

    urls=[]

    for i in awzurl:
        url=i.get_attribute('href')
        js = 'window.open("'+url+'");'
        driver.execute_script(js)
        #i.click()
        
            
        #time.sleep(1)
        urls.append(url)
        aurls.append(url)

        

    for num in range(1,len(urls)+1):
        #print(num)
        #driver.find_element(By.XPATH,'/html/body/div[4]/div/div[1]/div[1]/div[2]/div[1]/a').click()
        #driver.switch_to.window(driver.window_handles[-num])
        driver.switch_to.window(driver.window_handles[-1])
        # dbq = driver.find_element(By.ID,'content').find_element(By.CLASS_NAME,'content_auto').find_elements(By.TAG_NAME,'a')[1].text
        # yjbq = driver.find_element(By.ID,'content').find_element(By.CLASS_NAME,'content_auto').find_elements(By.TAG_NAME,'a')[2].text
        ejbq = driver.find_element(By.CLASS_NAME,'mianbaoxie').find_elements(By.TAG_NAME,'a')[-1].text
        # adbq.append(dbq)
        # ayjbq.append(yjbq)
        aejbq.append(ejbq)
        bb=driver.current_url
        bt=driver.find_element(By.TAG_NAME,'h1').text
        # if bt == '502网关错误，连接源站失败':
        #     driver.refresh() 
        #     bt=driver.find_element(By.TAG_NAME,'h1').text
        # else:
        #     pass
        #zy= driver.find_element(By.CLASS_NAME,'abstract_center').text
        #driver.find_element(By.CLASS_NAME,'view-allcontent').click()
        zwnr=driver.find_element(By.CLASS_NAME,'artcontent').text[97:]
        # gd=driver.find_element(By.CLASS_NAME,'artcontent').find_element(By.CLASS_NAME,'arttopit').text
        # zwnr=zwnr.replace(gd+'\n', '')
        # ony=[]
        # for i in zwnr:
        #     ny=i.text
        #     ony.append(ny)
            
        abt.append(bt)
        #azy.append(zy)
        awzny.append(zwnr)

            
        #time.sleep(1)
        driver.close()
    driver.switch_to.window(driver.window_handles[0])
    # driver.quit()
    end_time=time.time()
    print(end_time-start_time)
    if page<finalpage:
        nextpage=page+1
        #driver = webdriver.Chrome(options=opt)
        #driver.close()

        # driver = webdriver.Chrome()
        #driver.get(originurl[:-1]+'-'+str(nextpage)+originurl[-1])
        
        driver.get('http://www.kaolaseo.com/seo/list_11_'+str(nextpage)+'.html')
        #time.sleep(1)

    else:
        nextpage=page
        print("已经是最后一页，获取完成")

# 关闭
#driver.close()

#%%
#每页20条
# an=[]
# for n in range(0,len(aurls),20):
#     an.append(aurls[n]) 
# ann=[]
# for c in range(len(an)):
#     for l in range(len(an[c])):
#         ann.append(an[c][l])
# anewurls=ann
# yj=[yjbq]*len(abt)#改
# ej=[ejbq]*len(abt)#改

# alllist=[adbq,ayjbq,aejbq,aurls,abt,azy,awzny]
# awznyn=[]
# for t in range(0,len(awzny)):
#     tn=awzny[t][1:]
#     awznyn.append(tn)

alllist=[aejbq,aurls,abt,awzny]

#%%
import xlsxwriter

workbook = xlsxwriter.Workbook(ejbq+'8.xlsx',options={'strings_to_urls':False})
worksheet = workbook.add_worksheet(ejbq)

# companies = ['House1', 'House2']
# sector = ['Kitchen', 'Living room']
# url = ['www.house1.com', 'www.house2.com']

# list_companies = []
# list_companies.append(companies)
# list_companies.append(sector)
# list_companies.append(url)

# head = ['Company', 'Sector', 'URL']
head=['内容分类','链接','标题','正文内容']
bold = workbook.add_format({'bold':True})

worksheet.write_row(0,0,head, bold)
worksheet.write_column(1, 0, alllist[0])
worksheet.write_column(1, 1, alllist[1])
worksheet.write_column(1, 2, alllist[2])
worksheet.write_column(1, 3, alllist[3])




workbook.close()