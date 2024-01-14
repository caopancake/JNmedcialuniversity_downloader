import webbrowser
import tkinter as tk
import time

# 定义一个函数，用于生成序号连续的网页地址
def generate_urls(start,end,delay):
    urls = [] # 创建一个空列表，用于存储网页地址

    base_url = 'https://fulltext.yuntsg.com/pdfviewer?casesid='
    suffix_url = '&type=user'
    Delay = delay
    #网页打开
    for i in range(start, end + 1): # 遍历序号范围
        url = base_url + str(i) +suffix_url# 拼接网页地址
        webbrowser.open_new_tab(url)
        time.sleep(Delay)
        urls.append(url) # 将网页地址添加到列表中
    return urls # 返回网页地址列表


#程序本体_打开网页
def starweb():
    #数据处理
    start = int(entry_start.get())
    end = int(entry_end.get())
    delay = int(entry_delay.get())
    urls = generate_urls(start, end, delay)
    open_urls(urls)



#可视化
window = tk.Tk()
window.title("批量打开网页-济宁医学院图书馆专用")
window.geometry("400x220")
label = tk.Label(window, text="序列号格式如88571656")
label.pack(side="top")

label = tk.Label(window, text="起始序列号——小")
label.pack(side="top")
entry_start = tk.Entry(window)
entry_start.pack(side="top")

label = tk.Label(window, text="终止序列号——大")
label.pack(side="top")
entry_end = tk.Entry(window)
entry_end.pack(side="top")

label = tk.Label(window, text="启动浏览器延迟/秒")
label.pack(side="top")
entry_delay = tk.Entry(window)
entry_delay.pack(side="top")

button2 = tk.Button(window, text="启动浏览器",command=starweb,  padx=20, font=('微软雅黑', 16))#command=starweb,
button2.pack()
window.mainloop()# 进入主循环，显示窗口
#程序本体_可视化输入数据处理








