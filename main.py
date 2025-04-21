
from flask import Flask, request,jsonify ,send_from_directory
from flask_sqlalchemy import SQLAlchemy
import random
from datetime import datetime
import os
from flask_mail import Mail,  Message as MailMessage 
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv # type: ignore
from flask import Flask, render_template
from flask_cors import CORS 
from bs4 import BeautifulSoup
import requests
import psycopg2

app = Flask(
    __name__,
    template_folder='html',
    static_folder=".",
    static_url_path="/"
)

CORS(app) 


current_dir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(current_dir, '.env.local'))
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cart.html")
def cart(): return render_template("cart.html")

@app.route("/community.html")
def community(): return render_template("community.html")

@app.route("/demo.html")
def demo(): return render_template("demo.html")

@app.route("/earth-festival.html")
def earth_festival(): return render_template("earth festival.html")

@app.route("/home3.html")
def home3(): return render_template("home3.html")

@app.route("/homepage.html")
def homepage(): return render_template("homepage.html")

@app.route("/message.html")
def message(): return render_template("message.html")

@app.route("/newall.html")
def newall(): return render_template("newall.html")

@app.route("/notice.html")
def notice(): return render_template("notice.html")

@app.route("/pay.html")
def pay(): return render_template("pay.html")

@app.route("/public.html")
def public(): return render_template("public.html")

@app.route("/search.html")
def search(): return render_template("search.html")

@app.route("/shop.html")
def shop(): return render_template("shop.html")

@app.route("/team.html")
def team(): return render_template("team.html")

@app.route("/test.html")
def test(): return render_template("test.html")

@app.route("/tips.html")
def tips(): return render_template("tips.html")

# html/activity
@app.route("/activity/answer.html")
def activity_answer(): return render_template("activity/answer.html")

@app.route("/activity/ask.html")
def activity_ask(): return render_template("activity/ask.html")

@app.route("/activity/carbonjs.html")
def activity_carbonjs(): return render_template("activity/carbonjs.html")

# html/new/guoji
@app.route("/new/guoji/hd<int:num>.html")
def new_guoji_hd(num): return render_template(f"new/guoji/hd{num}.html")

# html/new/guonei
@app.route("/new/guonei/nr<int:num>.html")
def new_guonei_nr(num): return render_template(f"new/guonei/nr{num}.html")

# html/new/hbfq
@app.route("/new/hbfq/fg1.html")
def new_hbfq_fg1(): return render_template("new/hbfq/fg1.html")

# html/new/hbzcyxd
@app.route("/new/hbzcyxd/zc<int:num>.html")
def new_hbzcyxd_zc(num): return render_template(f"new/hbzcyxd/zc{num}.html")

# html/hjxw
@app.route("/hjxw/xw<int:num>.html")
def hjxw_news(num): return render_template(f"hjxw/xw{num}.html")

# html/kcxxcpvw
@app.route("/kcxxcpvw/cp<int:num>.html")
def cp(num): return render_template(f"kcxxcpvw/cp{num}.html")

@app.route("/kcxxcpvw/cpnews.html")
def cpnews(): return render_template("kcxxcpvw/cpnews.html")

@app.route("/kcxxcpvw/hjnews.html")
def hjnews(): return render_template("kcxxcpvw/hjnews.html")

@app.route("/kcxxcpvw/text.html")
def cptext(): return render_template("kcxxcpvw/text.html")

@app.route("/kcxxcpvw/zcnews.html")
def zcnews(): return render_template("kcxxcpvw/zcnews.html")

# html/new/s_along
@app.route("/new/s_along/social.html")
def social(): return render_template("new/s_along/social.html")

@app.route("/new/s_along/social-ch.html")
def social_ch(): return render_template("new/s_along/social-ch.html")

# html/new/v_along
@app.route("/new/v_along/video.html")
def video(): return render_template("new/v_along/video.html")

# html/new/y_along
@app.route("/new/y_along/laws.html")
def laws(): return render_template("new/y_along/laws.html")

@app.route("/new/y_along/standard.html")
def standard(): return render_template("new/y_along/standard.html")

@app.route("/new/y_along/enduction.html")
def enduction(): return render_template("new/y_along/enduction.html")

@app.route("/new/y_along/environment.html")
def environment(): return render_template("new/y_along/environment.html")

@app.route("/new/y_along/guojizuzhi.html")
def guojizuzhi(): return render_template("new/y_along/guojizuzhi.html")

@app.route("/new/y_along/guoneizuzhi.html")
def guoneizuzhi(): return render_template("new/y_along/guoneizuzhi.html")

@app.route("/new/y_along/huanbaofagui.html")
def huanbaofagui(): return render_template("new/y_along/huanbaofagui.html")

@app.route("/new/y_along/interview.html")
def interview(): return render_template("new/y_along/interview.html")

@app.route("/new/y_along/product.html")
def product(): return render_template("new/y_along/product.html")

@app.route("/new/y_along/product-new.html")
def product_new(): return render_template("new/y_along/product new.html")

@app.route("/new/y_along/zhengce-new.html")
def zhengce_new(): return render_template("new/y_along/zhengce new.html")

@app.route("/new/y_along/zhiliangbiaozhun.html")
def zhiliangbiaozhun(): return render_template("new/y_along/zhiliangbiaozhun.html")

# html/team
@app.route("/team/t<int:num>.html")
def team_page(num): return render_template(f"team/t{num}.html")

# html/theory
@app.route("/theory/home<int:num>.html")
def theory_home(num): return render_template(f"theory/home{num}.html")

@app.route("/theory/theory.html")
def theory_main(): return render_template("theory/theory.html")

# html/tips
@app.route("/tips/green.html")
def tips_green(): return render_template("tips/green.html")

@app.route("/tips/plant.html")
def tips_plant(): return render_template("tips/plant.html")

@app.route("/tips/rubbish.html")
def tips_rubbish(): return render_template("tips/rubbish.html")

@app.route("/tips/salvage.html")
def tips_salvage(): return render_template("tips/salvage.html")


# 调试输出环境变量
print("当前工作目录:", os.getcwd())
print("目录下的文件:", os.listdir(os.getcwd()))
print("DATABASE_URL:", os.environ.get('DATABASE_URL'))  # 确保输出正确


comments = []  # 临时存储留言

db = SQLAlchemy(app)

# 头像列表
AVATAR_LIST = [
    "/img/avatar0.png", "/img/avatar6.png", "/img/avatar2.png",
    "/img/avatar3.png", "/img/avatar4.png", "/img/avatar7.png"
]

# 定义留言表
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ename = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    avatar = db.Column(db.String(255), nullable=False, default="/img/avatar0.png")
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow) 

    def __repr__(self):
        return f'<Message {self.ename}>'

# 创建数据库表
with app.app_context():
    db.create_all()

#加载网页的网站图标
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


# 添加留言
@app.route('/add_comment', methods=['POST'])
def add_comment():
    try:
        data = request.get_json()
        ename = data.get('ename')
        content = data.get('content')

        if not data or 'ename' not in data or 'content' not in data:
            return jsonify({"status": "error", "message": "缺少名字或内容"}), 400

        # 随机选择头像
        avatar = random.choice(AVATAR_LIST) if 'avatar' not in data else data['avatar']

        # 创建新的留言并保存到数据库
        new_message = Message(ename=ename, content=content, avatar=avatar)
        db.session.add(new_message)
        db.session.commit()  # 提交到数据库

        print("留言成功，提交到数据库:", new_message)

        return jsonify({"status": "success", "message": "恭喜您留言成功！", "comment": {
            "ename": new_message.ename,
            "content": new_message.content,
            "avatar": new_message.avatar
        }})
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500

#获取留言
@app.route('/comments', methods=['GET'])
def get_comments():
    messages = Message.query.order_by(Message.created_at.desc()).all()
    return jsonify([{
        'ename': msg.ename,
        'content': msg.content,
        'avatar': msg.avatar,
        'created_at': msg.created_at.strftime('%Y-%m-%d %H:%M:%S')
    } for msg in messages])


#发送邮件功能
# 邮件服务器配置（使用 SMTP 发送邮件）
app.config['MAIL_SERVER'] = 'smtp.qq.com' 
app.config['MAIL_PORT'] = 587  # 端口号
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = '2606659976@qq.com'  # 你的邮箱
app.config['MAIL_PASSWORD'] = 'fuqurjvlrhnuebeh'  # SMTP授权码

mail = Mail(app)

# 定义“联系工作人员”表
class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ename = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)

    def __repr__(self):
        return f'<ContactMessage {self.ename}>'


# 接收用户意见
@app.route('/contact', methods=['POST'])
def contact_staff():
    try:
        data = request.get_json()
        print("收到的原始 JSON 数据：", data)

        ename = data.get('ename')
        message_content = data.get('message')
        print(f"ename: {ename}, message: {message_content}")

        if not ename or not message_content:
            return jsonify({'status': 'error', 'message': '名字和意见不能为空！'}), 400

        # 存入数据库
        new_contact = ContactMessage(ename=ename, message=message_content)
        db.session.add(new_contact)
        db.session.commit()
        print(f"{ename} 的留言已存入数据库")

        # 发送邮件
        msg = MailMessage(
            "环保网站 - 用户意见反馈",
            sender=app.config['MAIL_USERNAME'],
            recipients=["2606659976@qq.com"],
            body=f"来自 {ename} 的用户留言：\n\n{message_content}"
        )
        mail.send(msg)
        print("邮件发送成功")

        return jsonify({'status': 'success', 'message': '您的留言已提交，并已发送给工作人员！'})

    except Exception as e:
        print(f"服务器错误: {str(e)}") 
        return jsonify({'status': 'error', 'message': str(e)}), 500


# 定义报名表
class Signup(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)

#志愿者报名
@app.route('/signup', methods=['POST'])
def add_signup():
    try:
        data = request.get_json()
        username =data.get('username')
        email = data.get('email')
        address = data.get('address')

        if not username or not email or not address:
                return jsonify({'status': 'error', 'message': '不能为空！'}), 400
        
        # 报名新的用户并保存到数据库
        new_apply = Signup(username=username,email=email,address=address)
        db.session.add(new_apply)
        db.session.commit()  # 提交到数据库

        print("报名成功，提交到数据库:",new_apply) 

        return jsonify({"status": "success", "message": "恭喜您报名成功！", "comment": {
            "username": new_apply.username,
            "email": new_apply.email,
            "address": new_apply.address
        }})

    except Exception as e:
        print(f"服务器错误: {str(e)}") 
        return jsonify({'status': 'error', 'message': str(e)}), 500

#获取报名信息
@app.route('/get_signup', methods=['GET'])
def get_signup():
    messages = Signup.query.order_by(Signup.created_at.desc()).all()
    return jsonify([{
        'username': sign.username,
        'email': sign.email,
        'address': sign.address,
        'created_at': sign.created_at.strftime('%Y-%m-%d %H:%M:%S')
    } for sign in messages])


#获取智能问答
#访问接口进行身份验证
client = OpenAI(api_key="sk-dc7f14bb841542f3abd258f180481396", base_url="https://api.deepseek.com/v1")

#发送请求
@app.route('/ask', methods=['POST'])
def ask_deepseek():
    # 获取前端发送的问题
    data = request.get_json()
    user_question = data.get('question', '')
    
    if not user_question:
        return jsonify({"error": "问题不能为空"}), 400
    
    try:
        # 发送请求到 DeepSeek
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "你是一个专业知识解答客户助手，请用正式的语气回答用户的问题"},
                {"role": "user", "content": user_question},
            ],
            stream=False
        )
        
        answer = response.choices[0].message.content
        return jsonify({"answer": answer})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

conn = psycopg2.connect("postgresql://postgres:n3NNuQt0Z7pKTmbk@db.lprctmqyclfvyveblbin.supabase.co:5432/postgres")
print("✅ 数据库连接成功！")
conn.close()

# 运行服务器
if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', port=5000, debug=False)
    except Exception as e:
        print("应用启动失败:", str(e))


