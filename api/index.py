from flask import Flask, render_template, abort
from datetime import date

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

# 게시글 데이터 (DB 없이 딕셔너리로 관리)
POSTS = [
    {
        "id": 1,
        "title": "첫 번째 포스트: Flask와 Vercel로 블로그 만들기",
        "summary": "Python Flask와 Vercel을 사용해 무료로 블로그를 배포하는 방법을 소개합니다.",
        "content": """
        <p>Flask는 Python의 경량 웹 프레임워크입니다.</p>
        <p>Vercel의 서버리스 환경을 활용하면 무료로 웹사이트를 배포할 수 있습니다.</p>
        <h3>장점</h3>
        <ul>
            <li>무료 호스팅</li>
            <li>자동 HTTPS</li>
            <li>GitHub 연동 자동 배포</li>
        </ul>
        """,
        "date": "2025-05-19",
        "tags": ["Python", "Flask", "Vercel"]
    },
    {
        "id": 2,
        "title": "두 번째 포스트: 블로그 커스터마이징 팁",
        "summary": "블로그 디자인과 기능을 확장하는 다양한 방법을 알아봅니다.",
        "content": """
        <p>기본 블로그에서 다양한 기능을 추가할 수 있습니다.</p>
        <h3>확장 아이디어</h3>
        <ul>
            <li>Notion API 연동으로 글 관리</li>
            <li>댓글 기능 (Disqus)</li>
            <li>검색 기능 추가</li>
        </ul>
        """,
        "date": "2025-05-20",
        "tags": ["블로그", "커스터마이징"]
    },
]

@app.route("/")
def index():
    return render_template("index.html", posts=POSTS)

@app.route("/post/<int:post_id>")
def post(post_id):
    post = next((p for p in POSTS if p["id"] == post_id), None)
    if post is None:
        abort(404)
    return render_template("post.html", post=post)

@app.errorhandler(404)
def not_found(e):
    return render_template("base.html"), 404

# Vercel 서버리스 진입점
app = app
