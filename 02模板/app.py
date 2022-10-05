from flask import Flask,render_template

app = Flask(__name__)


@app.route("/about")
def about():
    context = {
        "username":"sxy",
        'books':['红楼梦','三国演义']
      #  ",".join()
    }
    # 字典需要变成关键字参数
    return render_template("about.html",**context)

@app.route("/control")
def control():
    context = {
        "age":18,
        'books': ['红楼梦', '三国演义','水浒传','西游记'],
        "person": {"name":"sxy","age":18}
    }
    return render_template("control.html",**context)

@app.route('/')
def index():  # put application's code here
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
