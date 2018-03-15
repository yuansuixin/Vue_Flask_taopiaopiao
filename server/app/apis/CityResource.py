from flask import json
from flask_restful import Resource, fields, marshal, marshal_with

from app.models import City, Letter

# result_city_fields = {
#     'id': fields.Integer,
#     'regionName': fields.String,
#     'cityCode': fields.Integer,
#     'pinYin': fields.String,
# }
#
# result_child_fields = {
#     'A': fields.List(fields.Nested(result_city_fields))
# }
#
# result_fields = {
#     'returnCode': fields.String(default=0),
#     'returnValue': fields.Nested(result_child_fields)
# }


class CitiesResource(Resource):
    # @marshal_with(result_fields)
    def get(self):
        letters = Letter.query.all()
        returnValue = {}

        result_child_fields_dynamic = {}

        result_city_fields = {
            'id': fields.Integer,
            'regionName': fields.String,
            'cityCode': fields.Integer,
            'pinYin': fields.String,
        }

        for letter in letters:
            print(letter.letter)
            result_child_fields_dynamic[letter.letter] = fields.List(fields.Nested(result_city_fields))
            cities = letter.cities
            returnValue[letter.letter] = cities

        result = marshal(returnValue, result_child_fields_dynamic)

        print(result)

        return {'returnValue': result}
