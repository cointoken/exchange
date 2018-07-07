"""
This requires the following Python libraries to be installed: 
* Flask
* Flask-SQLALchemy
* Flask-Restless
* Flask-Login
* pymysql
"""

from flask import Flask
from  flask_sqlalchemy import SQLAlchemy
from  flask_restless import APIManager 

app = Flask(__name__)
app.config['DEBUG'] = True
# python3.6以上使用pymysql 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/exchange'
db =  SQLAlchemy(app)


class Members(db.Model):
    # __tablename__=
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100),nullable=False,unique=True)
    pwd = db.Column(db.String(255),nullable=False)
    actived = db.Column(db.Integer(1),)
    #Foreignkey('')
    #relationship('')
    createTime = db.Column(db.DateTime,onupdate=datetime.now) 
    
    def _repr__(self):
        pass


"""
cros  xss 允许跨域
"""
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = 'example.com'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    # Set whatever other headers you like...
    return response


if __name__=='__main__':
    db.create_all()
    manager = APIManager(app,flask_sqlalchemy_db=db)
    #primary_key  设置主键名字
    #methods 
    #collection_name 
    #url_prefix 
    #include_columns 包含列
    manager.create_api(User,methods = ['GET','POST','DELETE','PATCH'],collection_name='session',url_prefix='/api/v2')
    manager.after_request(add_cors_headers)

    app.run(port=8888)

