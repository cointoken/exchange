from flask_rest_jsonapi import Api

api = Api()
# members
api.route(MemberList,'member_list','/members')


#orders
