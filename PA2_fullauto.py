import webbrowser
import tkinter as tk
import time
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
def webopener():
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    driver.get("https://user.tsgyun.com/user/login")
def download():
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By

    #driver.get("https://user.tsgyun.com/center/bookshelf?activeLi=1")
    #print("enter the webbrowser")
    driver.implicitly_wait(30)
    downloadlist = driver.find_elements("xpath", '//*[@id="fullText"]')

    print("getelements")
    print(downloadlist)

    length = len(downloadlist)
    print(length)
    for i, a in enumerate(downloadlist):
     if i <10:
        current_window = driver.current_window_handle  # 获取当前的窗口句柄
        print(current_window)
        # 使用execute_script方法，而不是click方法
        driver.execute_script("arguments[0].click();", a)
        time.sleep(10)
        #点击命令到此结束
        #新窗口的点击操作
        all_windows = driver.window_handles# 获取所有的窗口句柄
        print(all_windows)
        for window in all_windows:# 切换到新的窗口句柄
            if window != current_window:
                driver.switch_to.window(window)
                current_window2 = driver.current_window_handle  # 获取当前的窗口句柄
                print(current_window2)
                driver.implicitly_wait(30)
                # 定位到按钮
                pdfdownload = driver.find_element(By.CSS_SELECTOR, 'body > div.yellowTips > button:nth-child(3)')
                # 点击按钮
                driver.execute_script("arguments[0].click();", pdfdownload)

                print("downloading")
                driver.close()
                print("close windows")
                driver.switch_to.window(current_window)
                print("back to main")
     else:
        driver.implicitly_wait(30)
        button7 = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[5]/div/ul[1]/li[last()]")
        driver.execute_script("arguments[0].click();", button7)
        time.sleep(5)
        print("Page Change success")
        download()


def webdownload():
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    driver.get("https://user.tsgyun.com/center/bookshelf?activeLi=1")
    print("enter the webbrowser")
    download()
def endprocess():
    driver.quit()


#可视化
window = tk.Tk()
window.title("自动化下载文献-济宁医学院图书馆专用")
window.geometry("330x200")

label1 = tk.Label(window, text="首先点击-打开浏览器")
label1.pack(side="top")
button1 = tk.Button(window, text="打开浏览器",command=webopener, padx=20, font=('微软雅黑', 16))#command=download
button1.pack(side="top")
label2 = tk.Label(window, text="登录账号后-点击下载文献")
label2.pack(side="top")
button2 = tk.Button(window, text="点击下载文献",command=webdownload, padx=20, font=('微软雅黑', 16))#command=download
button2.pack(side="top")
label3 = tk.Label(window, text="全自动下载我的书架中的所有已申请成功的文献")
label3.pack(side="top")
window.mainloop()