from flask import Flask
from flask_migrate import Migrate
from models import Article,User,UserExtension
import config
from exts import db

app = Flask(__name__)
app.config.from_object(config)
# 把app绑定到db上
db.init_app(app)

migrate = Migrate(app, db)




@app.route("/otm")
def one_to_many():
    article1 = Article(title="111",content="xxx")
    article2 = Article(title="222",content="yyy")

    user = User(username="sxy")
    article1.author = user
    article2.author = user
    # db.session.add(user)

    db.session.add(article1,article2)
    db.session.commit()

    print(user.articles)

    return "one to many 数据操作成功"

@app.route("/oto")
def one_to_one():
    # user = User.query.filter_by(id=1).first()
    user = User(username="sxy")
    extension = UserExtension(school="ubc")
    user.extension = extension
    db.session.add(user)
    db.session.commit()
    return "one to one"

@app.route("/article")
def article_view():
    # # 1. 添加数据
    # # insert table article value(xx)
    # article = Article(title="钢铁是怎样炼成的",content="xxx")
    # db.session.add(article)
    # #做一个提交操作
    # db.session.commit()

    # # 2. 查询数据
    # # filter_by: 返回一个类列表的对象
    # article = Article.query.filter_by(id=1)[0]
    # print(article.title)

    # # 3.修改数据
    # article = Article.query.filter_by(id=1)[0]
    # article.content = "yyy"
    # db.session.commit()

    # 4. 删除数据
    # Article.query.filter_by(id=1).delete()
    # # article.delete()
    # db.session.commit()


    return "数据操作成功"






@app.route('/')
def hello_world():  # put application's code here
    # 写一个测试代码来验证连接是否成功
    # db = SQLAlchemy(app)
    engine = db.get_engine()
    # conn = engine.connect()
    # conn.close()
    with engine.connect() as conn:
        result = conn.execute("select 100")
        print(result.fetchone())
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
