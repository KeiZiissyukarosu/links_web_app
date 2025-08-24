from flask import Flask, render_template_string, request
import webbrowser

app = Flask(__name__)

# --- links_gui.pyw のリンク集を関数化 ---
links = [
    ("Twitter", "https://x.com/home"),
    ("YouTube", "https://www.youtube.com"),
    ("Join Support", "https://www.join-kk.jp/mobile/mypages/"),
    ("GitHub", "https://github.com"),
    ("Google", "https://www.google.com"),
    ("Python公式", "https://www.python.org")
]

def open_link(url):
    webbrowser.open(url)

# --- ルートページ ---
@app.route('/')
def index():
    buttons_html = ''
    for name, url in links:
        buttons_html += f'''
        <form action="/open" method="post" style="margin-bottom:5px;">
            <input type="hidden" name="url" value="{url}">
            <input type="submit" value="{name}" style="width:200px; height:40px;">
        </form>
        '''
    return render_template_string(f'''
        <h1>佃のリンク集（Web版）</h1>
        {buttons_html}
    ''')

# --- リンクを開く処理 ---
@app.route('/open', methods=['POST'])
def open_link_route():
    url = request.form['url']
    open_link(url)
    return f'リンク <a href="{url}" target="_blank">{url}</a> を開きました<br><a href="/">戻る</a>'

if __name__ == '__main__':
    # 同じネットワーク内やテザリング中のスマホからもアクセス可能
    app.run(host='0.0.0.0', port=5000)
