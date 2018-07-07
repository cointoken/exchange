
"""
"""
class Accounts(db.Model):
    # __tablename__ = 'accounts'
    id = db.Column(db.Integer,primary_key = True)
    member_id = db.Column(db.Integer(11),db.ForeignKey('members.id'),nullable = False)
    currency = db.Column(db.Integer(11),nullable = False)
    balance = db.Column(db.Float(32,16))
    locked = db.Column(db.Float(32,16))
    created_at = db.Column(db.DateTime,onupdate=datetime.now)
    updated_at = db.Column(db.DateTime,onupdate=datetime.now)
    in_ = db.Column(db.Float(32,16))
    out = db.Column(db.Float(32,16))
    default_withdraw_fund_source_id = db.Column(db.Integer(11))


