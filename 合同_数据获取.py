# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 14:49:26 2022

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
# options = webdriver.ChromeOptions()

# options.add_argument('--headless')
# options.add_argument('--no-sanbox')

# options.add_experimental_option('excludeSwitches', ['enable-automation'])


# options.add_argument("--disable-blink-features=AutomationControlled")
#options.page_load_strategy = 'none'

# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()

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
URL='https://www.liuxue86.com/hetongfanben/fangwuzulinghetong/'
driver.get(URL) #用模拟浏览器打开网页

twiceclass=driver.find_element(By.CLASS_NAME,'article2-left').find_element(By.CLASS_NAME,'article_list').find_elements(By.CLASS_NAME,'grid_list')##每页每条数据的网址

tcurl=[]
atcurls=[]
for i in twiceclass:
    divurl=i.find_elements(By.TAG_NAME,'a')
    for u in divurl:
        url=u.get_attribute('href')
        #i.click()   
        #time.sleep(1)
        tcurl.append(url)
    #atcurls.append(tcurl)
#%%

start_time = time.time()
# adbq=[]
# ayjbq=[]
# aejbq=[]
aurls=[]
aerurls=[]
# abt=[]
#azy=[]
# awzny=[]
aht=[]
ahtbt=[]
#starturl=tcurl[0]#读取每个一级分类的主页
#originurl=tcurl[0]
# starturl='https://www.liuxue86.com/hetongfanben/fangwuzulinghetong/'
# starturl='https://www.liuxue86.com/hetongfanben/zulin/'
# starturl='https://www.liuxue86.com/hetongfanben/hezuoxieyi/'
# starturl='https://www.liuxue86.com/hetongfanben/shigong/'
# starturl='https://www.liuxue86.com/hetongfanben/zhuangxiu/'
# starturl='https://www.liuxue86.com/hetongfanben/chengbao/'

#未处理区




#未处理区


# starturl='https://www.liuxue86.com/hetongfanben/jiagong/'
# starturl='https://www.liuxue86.com/hetongfanben/lihunxieyishu/'
# starturl='https://www.liuxue86.com/hetongfanben/wuyeguanli/'
# starturl='https://www.liuxue86.com/hetongfanben/jujian/'
# starturl='https://www.liuxue86.com/hetongfanben/yunshu/'
# starturl='https://www.liuxue86.com/hetongfanben/gonghuo/'
# starturl='https://www.liuxue86.com/hetongfanben/jiekuan/'
# starturl='https://www.liuxue86.com/hetongfanben/danbao/'
# starturl='https://www.liuxue86.com/hetongfanben/weituoshu/'
# starturl='https://www.liuxue86.com/hetongfanben/daili/'
starturl='https://www.liuxue86.com/hetongfanben/jiti/'
# starturl=''
# starturl=''
# starturl=''
# starturl=''
# starturl=''
# starturl=''
# starturl=''
# starturl=''
# starturl=''
# starturl=''

#cleanurl=re.findall(r'[/]$',originurl)
#originurl=originurl.replace(cleanurl[0],'')
# starturl=starturl.replace(cleanurl)
driver.get(starturl)
print(driver)
print(type(driver))
#首页
firstpage = 1
#firstpage = int(re.findall(r'\d+',starturl)[0])
# if firstpage==[]:
#     firstpage=1
# else:
#     firstpage=int(firstpage[0])

#末页
# endurl=driver.find_element(By.ID,'content').find_element(By.ID,'page').find_elements(By.TAG_NAME,'a')
# endurl=endurl[-2].get_attribute('href')
endurl=starturl+'5.html'
finalpage = int(re.findall(r'\d+',endurl)[1])
# finalpage = 3


for page in range(firstpage,finalpage+1):
    print(' ',page)

    
    #comment = driver.find_element(By.XPATH,'/html/body/div[4]/div/div[1]/div[1]/div[2]/div[1]/a').text
    awzurldiv=driver.find_element(By.CLASS_NAME,'article2-left').find_element(By.CLASS_NAME,'article_list').find_elements(By.CLASS_NAME,'grid_list')#每页每条数据的网址
    atcurls=[]
    urls=[]

    for i in awzurldiv:
        divurl=i.find_elements(By.TAG_NAME,'a')
        for u in divurl:
            url=u.get_attribute('href')
            u.click()   
            #time.sleep(1)
            aurls.append(url)
            urls.append(url)

    # for i in awzurl:
    #     url=i.get_attribute('href')
    #     js = 'window.open("'+url+'");'
    #     driver.execute_script(js)
    #     #i.click()
        
            
    #     #time.sleep(1)
    #     aurls.append(url)
    for num in range(1,len(urls)+1):
        #print(num)
        #driver.find_element(By.XPATH,'/html/body/div[4]/div/div[1]/div[1]/div[2]/div[1]/a').click()
        #driver.switch_to.window(driver.window_handles[-num])
        driver.switch_to.window(driver.window_handles[-1])
        #driver.get("https://www.liuxue86.com/a/4312886.html") 
        
        # driver.get('https://www.liuxue86.com/a/4313306.html')
        
        #driver.get('https://www.liuxue86.com/a/4230461.html')
        
        text=driver.find_element(By.ID,'article-content').text
        
        tx=text.split('\n')#[1:]#去掉首行广告
        
        #'推荐阅读：'
        
        #'小编精心推荐'
        
        #'买卖合同小编精心推荐：购房合同、售房合同'
        
        # ['房屋租赁合同 租房合同 出租房屋合同 个人租房合同 房屋出租合同 个人房屋租赁合同',
        #  '租房合同范本 租房协议 房屋转租合同 个人房屋出租 房租合同范本 房屋租赁合同范本']
        

        title=driver.find_element(By.ID,'article-content').find_elements(By.TAG_NAME,'h3')
        titisext='yes'
        if title==[]:
            title=driver.find_element(By.ID,'article-content').find_elements(By.TAG_NAME,'h2')
            titisext='yes'

        if title==[]:
            title=driver.find_element(By.XPATH,'//*[@id="main_content_zwxb"]/div[3]/div[1]').find_elements(By.TAG_NAME,'h1')
            titisext='no'
        
        divtitle=[]
        #获取标题集
        for  i in range(len(title)):
            onet=title[i].text
            divtitle.append(onet)
        while '' in divtitle:
            divtitle.remove('')
        atindex=[]
        
        if tx[0]!=divtitle[0] and titisext=='no':
            tx=tx[1:]
        elif tx[0]!=divtitle[0]:
            tx=tx[tx.index(divtitle[0]):]
            
        if '推荐阅读：' in tx:
            print('推荐存在')
            endindex=tx.index('推荐阅读：')
            tx=tx[:endindex]#去除尾部脏数据

            
        elif '小编精心推荐' in tx:
            print('精选存在')
            endindex=tx.index('小编精心推荐')
            tx=tx[:endindex]#去除尾部脏数据

        
            
        elif '买卖合同小编精心推荐：购房合同、售房合同' in tx:
            print('精选存在')
            endindex=tx.index('买卖合同小编精心推荐：购房合同、售房合同')
            tx=tx[:endindex]#去除尾部脏数据

        
            
        elif '房屋租赁合同 租房合同 出租房屋合同 个人租房合同 房屋出租合同 个人房屋租赁合同' in tx:
            print('table存在')
            endindex=tx.index('房屋租赁合同 租房合同 出租房屋合同 个人租房合同 房屋出租合同 个人房屋租赁合同')
            tx=tx[:endindex]#去除尾部脏数据

        else:
            pass
        
        
        #合同标题索引
        for v in divtitle:
            try:
                titleindex=tx.index(v)
            except:
                print('该页无标题')

                titleindex='该页无标题'
            atindex.append(titleindex)
        
        for d in range(len(atindex)):#分割文章
            print(d)
            if d <len(atindex)-1 and isinstance(atindex[d],int):
                hetong=tx[atindex[d]:atindex[d+1]]
                ahtbt+=[divtitle[d]]*len(hetong)
                erurl=driver.current_url
                aerurls+=[erurl]*len(hetong)
                #aht.append(hetong) 
                aht+=hetong
                #print(1)
            elif d==len(atindex)-1 and isinstance(atindex[d],int):
                hetong=tx[atindex[d]:]
                ahtbt+=[divtitle[d]]*len(hetong)
                erurl=driver.current_url
                aerurls+=[erurl]*len(hetong)
                #aht.append(hetong) 
                aht+=hetong
        
                #print(0)
            else:
                print('合同无标题')
                hetong=tx
                ahtbt+=divtitle*len(hetong)
                erurl=driver.current_url
                aerurls+=[erurl]*len(hetong)
                #aht.append(hetong) 
                aht+=hetong

        # dbq = driver.find_element(By.ID,'content').find_element(By.CLASS_NAME,'content_auto').find_elements(By.TAG_NAME,'a')[1].text
        # yjbq = driver.find_element(By.ID,'content').find_element(By.CLASS_NAME,'content_auto').find_elements(By.TAG_NAME,'a')[2].text
        #ejbq = driver.find_element(By.CLASS_NAME,'mianbaoxie').find_elements(By.TAG_NAME,'a')[-1].text
        # adbq.append(dbq)
        # ayjbq.append(yjbq)
        # aejbq.append(ejbq)
        # bb=driver.current_url
        # bt=driver.find_element(By.TAG_NAME,'h1').text
        # if bt == '502网关错误，连接源站失败':
        #     driver.refresh() 
        #     bt=driver.find_element(By.TAG_NAME,'h1').text
        # else:
        #     pass
        #zy= driver.find_element(By.CLASS_NAME,'abstract_center').text
        #driver.find_element(By.CLASS_NAME,'view-allcontent').click()
        #zwnr=driver.find_element(By.CLASS_NAME,'artcontent').text[97:]
        # gd=driver.find_element(By.CLASS_NAME,'artcontent').find_element(By.CLASS_NAME,'arttopit').text
        # zwnr=zwnr.replace(gd+'\n', '')
        # ony=[]
        # for i in zwnr:
        #     ny=i.text
        #     ony.append(ny)
            
        # abt.append(bt)
        #azy.append(zy)
        # awzny.append(zwnr)

            
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
        
        driver.get(starturl+str(nextpage)+'.html')
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
yjbt=['无法判断分类']*len(aht)
ejbt=['集体合同']*len(aht)
alllist=[yjbt,ejbt,ahtbt,aht,aerurls]

#%%
import xlsxwriter

workbook = xlsxwriter.Workbook(yjbt[0]+'_'+ejbt[0]+'.xlsx',options={'strings_to_urls':False})
worksheet = workbook.add_worksheet(ejbt[0])

# companies = ['House1', 'House2']
# sector = ['Kitchen', 'Living room']
# url = ['www.house1.com', 'www.house2.com']

# list_companies = []
# list_companies.append(companies)
# list_companies.append(sector)
# list_companies.append(url)

# head = ['Company', 'Sector', 'URL']
head=['品类','合同类型','合同名称','合同条款']#,'合同链接']
bold = workbook.add_format({'bold':True})

worksheet.write_row(0,0,head, bold)
worksheet.write_column(1, 0, alllist[0])
worksheet.write_column(1, 1, alllist[1])
worksheet.write_column(1, 2, alllist[2])
worksheet.write_column(1, 3, alllist[3])
# worksheet.write_column(1, 4, alllist[4])



workbook.close()