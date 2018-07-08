"""
充值表
"""
class Deposits(db.Model):
    id = db.Column(db.Integer(11),primary_key=True)
    account_id = db.Column(db.Integer(11),ForeignKey('accounts.id)'))
    member_id = db.Column(db.Integer(11),ForeignKey('members.id'))
    currency = db.Column(db.Integer(11))
    amount = db.Column(db.Float(32,16))
    fee  = db.Column(db.Float(32,16))
    fund_uid = db.Column(db.String(255))
    fund_extra = db.Column(db.String(255))
    txid = db.Column(db.String(255))
    state = db.Column(db.Integer(11))
    assm_state = db.Column(db.String(255))
    created_at = db.Column(db.DateTime,onupdate=datetime.now)
    updated_at = db.Column(db.DateTime,onupdate=datetune.now)
    done_at = db.Column(db.DateTime)
    confirmations = db.Column(db.String(255))
    type = db.Column(db.String(255))
    payment_transaction_id = db.Column(db.Integer(11))
    txout = db.Column(db.Integer(11))
