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
    print("enter the webbrowser")
def webdownload():
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    current_window = driver.current_window_handle
    print(current_window)
    all_windows = driver.window_handles
    print(all_windows)
    for window in all_windows:  # 切换到新的窗口句柄
        if window != current_window:
            driver.switch_to.window(window)
            current_window2 = driver.current_window_handle  # 获取当前的窗口句柄
            print(current_window2)
            driver.implicitly_wait(30)
            paperselector()

def paperselector():
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By


    driver.implicitly_wait(30)
    kickall = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[3]/div[2]/div[2]/div[2]/ul[1]/li[1]")
    driver.execute_script("arguments[0].click();", kickall)
    print("kickall success")

    driver.implicitly_wait(30)
    requestall = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div[3]/div[2]/div[2]/div[2]/ul[2]/li[1]")
  #  driver.execute_script("arguments[0].click();", requestall)
    requestall.click()
    print("requestall success")

    driver.implicitly_wait(30)
    acceptall = driver.find_element(By.XPATH, "/html/body/div[8]/div[3]/a[1]")
    driver.execute_script("arguments[0].click();", acceptall)
    print("acceptall success")

    driver.implicitly_wait(30)
    nextpage = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[3]/div[2]/div[2]/div[3]/ul[1]/li[last()]")
    driver.execute_script("arguments[0].click();", nextpage)
    print("nextpage success")

    paperselector()


def windows():
    current_window = driver.current_window_handle
    print(current_window)
    all_windows = driver.window_handles
    print(all_windows)




#可视化
window = tk.Tk()
window.title("自动化下载文献-济宁医学院图书馆专用")
window.geometry("350x200")

label1 = tk.Label(window, text="首先点击-打开浏览器")
label1.pack(side="top")
button1 = tk.Button(window, text="打开浏览器",command=webopener, padx=20, font=('微软雅黑', 16))#command=download
button1.pack(side="top")
label2 = tk.Label(window, text="登录账号后-搜索文献")
label2.pack(side="top")
label2 = tk.Label(window, text="搜素文献后保持在有文献界面的第一页-点击一键获取文献")
label2.pack(side="top")
button2 = tk.Button(window, text="点击一键获取文献",command=webdownload, padx=20, font=('微软雅黑', 16))#command=download
button2.pack(side="top")
label3 = tk.Label(window, text="自动获取当前搜索界面的所有文献，注意个人账号每日获取限额")
label3.pack(side="top")
window.mainloop()