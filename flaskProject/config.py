# 数据库的配置变量
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = '02sxy'
USERNAME = 'root'
PASSWORD = 'Qr977207'
DB_URI   = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'swqdejnfwkbfhvjkcl121334'





# 邮箱配置:
# 项目使用qq邮箱
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = 465
MAIL_USE_TLS =  False
MAIL_USE_SSL = True
MAIL_DEBUG = True
MAIL_USERNAME = "1534840095@qq.com"
MAIL_PASSWORD = "xhctfawypshibafh"
MAIL_DEFAULT_SENDER = "1534840095@qq.com"
