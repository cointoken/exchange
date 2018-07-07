"""
撮合交易表
"""
class Trades(db.Model):
    id = db.Column(db.Integer(11,primary_key = True))
    price = db.Column(db.Float(32,16))
    volume = db.Column(db.Float(32,16))
    ask_id = db.Column(db.Integer(11))
    bid_id = db.Column(db.Integer(11))
    trend = db.Column(db.Integer(11))
    currency = db.Column(db.Integer(11))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    ask_member_id = db.Column(db.Integer(11),db.ForeignKey('members.id'))
    bid_member_id = db.Column(db.Integer(11),db.ForeignKey('members.id'))
    funds = db.Column(db.Float(32,16))