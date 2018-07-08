"""
注册会员表
"""
from passlib.apps import custom_app_context 


class Members(db.Model):
    # __tablename__=
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100),nullable=False,unique=True)
    pwd = db.Column(db.String(255),nullable=False)
    activated = db.Column(db.Boolean)
    country_code = db.Column(db.Integer(11))
    phone_number = db.Column(db.String(255))
    disable = db.Column(db.Boolean)
    nickname = db.Column(db.String(255))
    invited_code =  db.Column(db.String(20))
    #Foreignkey('')
    #relationship('')
    created_at = db.Column(db.DateTime,onupdate=datetime.now) 
    updated_at = db.Column(db.DateTime,onupdate=datetime.now)
    
    def _repr__(self):
        pass


    def encrypt_password(self, pwd):
        self.pwd = custom_app_context.encrypt(pwd)


    def verify_password(self,pwd):
        return custom_app_context.verify(pwd,self.pwd)
    
    def set_invited_code(self):
        self.invited_code = 1000000+self.id
    
    