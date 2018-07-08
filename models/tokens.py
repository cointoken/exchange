"""
"""
class Tokens(db.Model):
    id = db.Column(db.Integer(11),primary_key = True)
    token = db.Column(db.String(255))
    expire_at = db.Column(db.DateTime)
    is_used = db.Column(db.Boolean)
    type = db.Column(db.String(255))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

