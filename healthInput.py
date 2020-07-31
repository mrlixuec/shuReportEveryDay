num=""
pwd=""

from selenium import webdriver
import datetime
from time import sleep
import datetime

option = webdriver.ChromeOptions()
option.add_argument('headless')
option.add_argument('no-sandbox')
option.add_argument('disable-dev-shm-usage')
driver = webdriver.Chrome('/usr/local/selenium/chromedriver',chrome_options=option)

driver.implicitly_wait(10)

def isTime():

    d_timeB1 = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '7:00', '%Y-%m-%d%H:%M')
    d_timeE1 = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '9:00', '%Y-%m-%d%H:%M')
    # 当前时间
    n_time = datetime.datetime.now()

    # 判断当前时间是否在范围时间内
    if n_time > d_timeB1 and n_time < d_timeE1:
        return True
    else:
        return False




def login(uname, pwd):
    driver.get("https://selfreport.shu.edu.cn/")

    if(driver.title=="上海大学统一身份认证"):
        inputEle=driver.find_element_by_xpath('//*[@id="username"]')
        inputEle.send_keys(uname)

        pwdEle=driver.find_element_by_xpath('//*[@id="password"]')
        pwdEle.send_keys(pwd)

        loginBtn=driver.find_element_by_xpath('//*[@id="login-submit"]')
        loginBtn.click()



def write():

    eleEveDay=driver.find_element_by_xpath('//*[@id="lnkReport"]/div')
    eleEveDay.click()
    sleep(1)
    if(isTime()):
        eleCommit=driver.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div/a[1]')
    else:
        eleCommit=driver.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div/a[2]')

    eleCommit.click()
    sleep(1)

    eleChengNuo = driver.find_element_by_xpath('// *[ @ id = "p1_ChengNuo-inputEl-icon"]')

    str=eleChengNuo.get_attribute('class')
    subStr = "f-checked"
    if subStr in str:
        pass
    else:
        eleChengNuo.click()

    inputStatus = driver.find_element_by_xpath('//*[@id="fineui_0-inputEl-icon"]')

    inputStatus.click()



    sleep(1)

    inputTemprature= driver.find_element_by_xpath('//*[@id="p1_TiWen-inputEl"]')
    sleep(1)
    inputTemprature.clear()
    inputTemprature.send_keys('36.5')
    sleep(1)


    intputColor=driver.find_element_by_xpath('//*[@id="fineui_7-inputEl-icon"]')
    intputColor.click()
    sleep(1)


    inputB = driver.find_element_by_xpath('//*[@id="fineui_8-inputEl-icon"]')
    inputB.click()
    sleep(1)
    inputL = driver.find_element_by_xpath('//*[@id="fineui_9-inputEl-icon"]')
    inputL.click()
    sleep(1)
    inputD = driver.find_element_by_xpath('//*[@id="fineui_10-inputEl-icon"]')
    inputD.click()
    sleep(1)


    commit=driver.find_element_by_xpath('//*[@id="p1_ctl00_btnSubmit"]/span/span')
    sleep(1)
    commit.click()
    sleep(1)

    eleLastAck=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div/div/a[1]/span/span')
    eleLastAck.click()
    sleep(1)

# main
login(num,pwd)
#
sleep(1)
write()
















