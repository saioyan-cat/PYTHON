import tkinter as tk

# 1. 定義按鈕點擊後要執行的功能（函式）
def on_button_click():
    print("按鈕被點擊了！")

# 2. 建立主視窗
root = tk.Tk()
root.title("Python 按鈕範例")
root.geometry("300x200") # 設定視窗大小

# 3. 建立按鈕元件，並用 command 綁定剛才定義的函式
button = tk.Button(root, text="點我", command=on_button_click)

# 4. 將按鈕放到視窗畫面上
button.pack(pady=20) # pady 可以讓按鈕上下留點空間

# 5. 啟動視窗事件循環
root.mainloop()
