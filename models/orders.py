"""
订单表
"""
class Orders(db.Model):
    id = db.Column(db.Integer(11),primary_key = True)
    bid = db.Column(db.Integer(11))
    ask = db.Column(db.Integer(11))
    currency = db.Column(db.Integer(11))
    price = db.Column(db.Float(32,16))
    volumne = db.Column(db.Float(32,16))
    origin_volumn = db.Column(db.Float(32,16))
    state = db.Column(db.Integer(11))
    done_at = db.Column(db.DateTime)
    type = db.Column(db.String(8))
    member_id = db.Column(db.Integer(11),ForeignKey('members.id'))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    sn = db.Column(db.String(255))
    source = db.Column(db.String(255))
    order_type = db.Column(db.String(10))
    locked = db.Column(db.Float(32,16))
    origin_locked = db.Column(db.Float(32,16))
    funds_received = db.Column(db.Float(32,16))
    trades_count = db.Column(db.Integer(11))