# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 18:11:01 2022

@author: Windows 10
"""
#%%
from selenium import webdriver
from selenium.webdriver.common.by import By

import time 
import re
#创建配置对象
# opt = webdriver.ChromeOptions()

# # 添加配置参数
# opt.add_argument('--headless')  # 配置对象添加开启无界面模式的命令
# opt.add_argument('--disable-gpu')  # 配置对象添加禁用gpu的命令


# start_time = time.time()
# browser = webdriver.Chrome(options=opt)
browser = webdriver.Chrome()
aurls=[]
abt=[]
azy=[]
awzny=[]
starturl="https://www.huabaike.com/yhjq/p186.html"
browser.get(starturl)
print(browser)
print(type(browser))

firstpage = int(re.findall(r'\d+',starturl)[0])


endurl=browser.find_element(By.CLASS_NAME,'end').get_attribute('href')
 
#finalpage = int(re.findall(r'\d+',endurl)[0])
finalpage = 188
for page in range(firstpage,finalpage+1):
    for nextpage in range(firstpage+1,finalpage+1):

        title = browser.find_element(By.CLASS_NAME,'active').text
        info = browser.find_element(By.CLASS_NAME,'nav_index').text
        
        #comment = browser.find_element(By.XPATH,'/html/body/div[4]/div/div[1]/div[1]/div[2]/div[1]/a').text
        allc=browser.find_elements(By.CLASS_NAME,'listItem')#每页每条数据的网址
            
        urls=[]

        for i in allc:
            while True:
                try:
                    url=i.find_element(By.TAG_NAME,'a').get_attribute('href')
                    i.find_element(By.TAG_NAME,'a').click()
                        
                    #time.sleep(1)
                    urls.append(url)
                    aurls.append(urls)
                
                    for num in range(1,len(urls)+1):
                        print(num)
                        #browser.find_element(By.XPATH,'/html/body/div[4]/div/div[1]/div[1]/div[2]/div[1]/a').click()
                        browser.switch_to.window(browser.window_handles[-num])
                        bb=browser.current_url
                        bt=browser.find_element(By.TAG_NAME,'h1').text
                        # if bt == '502网关错误，连接源站失败':
                        #     browser.refresh() 
                        # else:
                        zy= browser.find_element(By.TAG_NAME,'blockquote').text
                        browser.find_element(By.CLASS_NAME,'view-allcontent').click()
                        zwnr=browser.find_element(By.XPATH,'/html/body/div[5]/div/div[1]/div[1]/div[2]/div[3]').text
                        abt.append(bt)
                        azy.append(zy)
                        awzny.append(zwnr)
                    break
                except:
                    continue
                
            #time.sleep(1)
            #browser.close()
        #browser.switch_to.window(browser.window_handles[0])
        browser.quit()
        # browser = webdriver.Chrome(options=opt)
        browser = webdriver.Chrome()

        browser.get("https://www.huabaike.com/yhjq/p"+str(nextpage)+".html")
    
#%%
from selenium import webdriver
from selenium.webdriver.common.by import By

import time 
import re
#创建配置对象
opt = webdriver.ChromeOptions()

# 添加配置参数
opt.add_argument('--headless')  # 配置对象添加开启无界面模式的命令
opt.add_argument('--disable-gpu')  # 配置对象添加禁用gpu的命令


start_time = time.time()
#browser = webdriver.Chrome(options=opt)
browser = webdriver.Chrome()
aurls=[]
abt=[]
azy=[]
awzny=[]
starturl="https://www.huabaike.com/yhjq/p495.html"
browser.get(starturl)
print(browser)
print(type(browser))

firstpage = int(re.findall(r'\d+',starturl)[0])

endurl=browser.find_element(By.CLASS_NAME,'end').get_attribute('href')
 
finalpage = int(re.findall(r'\d+',endurl)[0])
# finalpage = 188
for page in range(firstpage,finalpage+1):
    print(' ',page)


    title = browser.find_element(By.CLASS_NAME,'active').text
    info = browser.find_element(By.CLASS_NAME,'nav_index').text
    
    #comment = browser.find_element(By.XPATH,'/html/body/div[4]/div/div[1]/div[1]/div[2]/div[1]/a').text
    allc=browser.find_elements(By.CLASS_NAME,'listItem')#每页每条数据的网址
        
    urls=[]

    for i in allc:
        url=i.find_element(By.TAG_NAME,'a').get_attribute('href')
        i.find_element(By.TAG_NAME,'a').click()
            
        #time.sleep(1)
        urls.append(url)
        aurls.append(urls)
    
    for num in range(1,len(urls)+1):
        #print(num)
        #browser.find_element(By.XPATH,'/html/body/div[4]/div/div[1]/div[1]/div[2]/div[1]/a').click()
        #browser.switch_to.window(browser.window_handles[-num])
        browser.switch_to.window(browser.window_handles[-1])
        bb=browser.current_url
        bt=browser.find_element(By.TAG_NAME,'h1').text
        if bt == '502网关错误，连接源站失败':
            browser.refresh() 
            bt=browser.find_element(By.TAG_NAME,'h1').text
        else:
            pass
        zy= browser.find_element(By.TAG_NAME,'blockquote').text
        browser.find_element(By.CLASS_NAME,'view-allcontent').click()
        zwnr=browser.find_element(By.XPATH,'/html/body/div[5]/div/div[1]/div[1]/div[2]/div[3]').text
        abt.append(bt)
        azy.append(zy)
        awzny.append(zwnr)

            
        #time.sleep(1)
        browser.close()
    browser.switch_to.window(browser.window_handles[0])
    # browser.quit()
    end_time=time.time()
    print(end_time-start_time)
    if page<finalpage:
        nextpage=page+1
        #browser = webdriver.Chrome(options=opt)
        #browser.close()

        # browser = webdriver.Chrome()
        browser.get("https://www.huabaike.com/yhjq/p"+str(nextpage)+".html")
        #time.sleep(1)

    else:
        nextpage=page
        print("已经是最后一页，获取完成")


#%%
#每页20条
an=[]
for n in range(0,len(aurls),20):
    an.append(aurls[n]) 
ann=[]
for c in range(len(an)):
    for l in range(len(an[c])):
        ann.append(an[c][l])
anewurls=ann
yj=[title]*len(abt)
ej=[info]*len(abt)

alllist=[yj,ej,anewurls,abt,azy,awzny]
#%%
import pandas as pd
import os
def write_to_one_excel(filepath,sheetname,datelist):
    print("正在保存 %s to %s\n" % (sheetname,filepath))
    #创建一个空的Dataframe
    #columns 只有一项是用[]
    # result =pd.DataFrame(columns=['name'])
    #result =pd.DataFrame(columns=('name','url','icon'))
    result =pd.DataFrame(columns=('一级分区','二级分区','链接','标题','摘要','正文内容'))
    for list in datelist:
        #print(list)
        result=result.append(pd.DataFrame({'一级分区':[alllist[0]],'二级分区':[alllist[1]],'链接':[alllist[2]],
                                           '标题':[alllist[3]],'摘要':[alllist[4]],'正文内容':[alllist[5]]}))
    #判断文件是否存在
    if os.path.exists(filepath):
        # 然后再实例化ExcelWriter
        #使用with方法打开了文件，生成的文件操作实例在with语句之外是无效的，因为with语句之外文件已经关闭了。无需writer.save()和writer.close()，否则报错
        with pd.ExcelWriter(filepath,engine="openpyxl",mode='a') as writer:
            # 保存到本地excel
            # 接下来还是调用to_excel, 但是第一个参数不再是文件名, 而是上面的writer
            result.to_excel(writer,sheet_name=sheetname)
    else:
        result.to_excel(filepath,sheet_name=sheetname, index=False)
    # writer.save()
    # writer.close()
    
write_to_one_excel('C:/Users/Windows 10/Desktop/'+info+'.xlsx',info,alllist)

#%%
import xlsxwriter

workbook = xlsxwriter.Workbook(info+'4.xlsx')
worksheet = workbook.add_worksheet(info)

# companies = ['House1', 'House2']
# sector = ['Kitchen', 'Living room']
# url = ['www.house1.com', 'www.house2.com']

# list_companies = []
# list_companies.append(companies)
# list_companies.append(sector)
# list_companies.append(url)

# head = ['Company', 'Sector', 'URL']
head=['一级分区','二级分区','链接','标题','摘要','正文内容']
bold = workbook.add_format({'bold':True})

worksheet.write_row(0,0,head, bold)
worksheet.write_column(1, 0, alllist[0])
worksheet.write_column(1, 1, alllist[1])
worksheet.write_column(1, 2, alllist[2])
worksheet.write_column(1, 3, alllist[3])
worksheet.write_column(1, 4, alllist[4])
worksheet.write_column(1, 5, alllist[5])

workbook.close()

#%%
# dic = {}
# dic['书名'] = title
# dic['其他信息'] = info.split('\n')
# dic['评分'] = score
# dic['评论人数'] = comment
# print(dic)
# end_time = time.time()
# print("花费了{:.2f}秒".format(end_time-start_time))