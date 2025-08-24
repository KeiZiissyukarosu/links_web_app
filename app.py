from flask import Flask, render_template_string

app = Flask(__name__)

links = [
    ("Twitter", "https://x.com/home"),
    ("YouTube", "https://www.youtube.com"),
    ("Join Support", "https://www.join-kk.jp/mobile/mypages/"),
    ("GitHub", "https://github.com"),
    ("Google", "https://www.google.com"),
    ("Python公式", "https://www.python.org")
]

@app.route('/')
def index():
    buttons_html = ''
    for name, url in links:
        buttons_html += f'''
        <a href="{url}" target="_blank">
            <button class="link-button">{name}</button>
        </a>
        '''
    return render_template_string(f'''
        <html>
        <head>
        <style>
            body {{
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                min-height: 100vh;
                font-family: sans-serif;
            }}
            .link-button {{
                width: 80%;
                max-width: 300px;
                height: 50px;
                margin: 10px 0;
                font-size: 18px;
                border-radius: 8px;
                border: none;
                background-color: #4CAF50;
                color: white;
            }}
            .link-button:hover {{
                background-color: #45a049;
                cursor: pointer;
            }}
        </style>
        </head>
        <body>
            <h1>佃のリンク集（Web版）</h1>
            {buttons_html}
        </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
