import tkinter as tk
import webbrowser

# ウィンドウ作成
root = tk.Tk()
root.title("佃のリンク集")
root.geometry("400x600")  # 縦長ウィンドウ

# タイトルラベル
label = tk.Label(root, text="よく使うリンク集", font=("Arial", 18, "bold"))
label.pack(pady=20)

# Webサイトを開く関数
def open_website(url):
    webbrowser.open(url)

# ボタンのリスト（表示名とURL）
links = [
    ("Twitter", "https://x.com/home"),
    ("YouTube", "https://www.youtube.com"),
    ("Join Support", "https://www.join-kk.jp/mobile/mypages/"),
    ("GitHub", "https://github.com"),
    ("Google", "https://www.google.com"),
    ("Gmail", "https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox"),
    ("Python公式", "https://www.python.org")
]

# ボタン作成
for text, url in links:
    btn = tk.Button(root, text=text, width=25, height=2,
                    font=("Arial", 12, "bold"),
                    command=lambda u=url: open_website(u))
    btn.pack(pady=5)

# ウィンドウ表示
root.mainloop()
