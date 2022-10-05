from flask import Flask,Response,request,session

app = Flask(__name__)
app.config['SECRET_KEY']="123"




@app.route("/set_cookie")
def set_cookie():
    response = Response("cookie 设置")
    response.set_cookie("user_id","xxx")
    return response

@app.route("/get_cookie")
def get_cookie():
    user_id =  request.cookies.get("user_id")
    print("user_id",user_id)
    return "获取cookie"


@app.route("/set_session")
def set_session():
    # 在flask中，session是先把数据经过加密，然后session_id作为key，存放到cookie中
    # 因为session会经过加密再存储到cookie中，所以我们的敏感信息，会存放到session中
    session['username'] = "sxy"
    return "session设置成功"

@app.route("/get_session")
def get_session():
    username = session.get('username')
    print("username:", username)
    return "get session"

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
