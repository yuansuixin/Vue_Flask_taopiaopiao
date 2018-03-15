from flask_restful import Resource, marshal_with, fields, reqparse

from app.models import Movie

movie_fields = {
    'showname': fields.String,
    'shownameen': fields.String,
    'director ': fields.String,
    'leadingRole': fields.String,
    'type ': fields.String,
    'country': fields.String,
    'language ': fields.String,
    'duration': fields.Integer,
    'screeningmodel': fields.String,
    'openday ': fields.DateTime,
    'backgroundpicture': fields.String,
    'flag ': fields.Integer,
}

result_fields = {
    'msg': fields.String(default='ok'),
    'pageNumber': fields.Integer,
    'returnCode': fields.String,
    'returnValue': fields.List(fields.Nested(movie_fields))
}

parser = reqparse.RequestParser()
parser.add_argument(name='page', default=1, type=int)
parser.add_argument(name='page_size', default=15, type=int)
parser.add_argument(name='type_flag', default=1, type=int)


class MoviesResource(Resource):
    @marshal_with(result_fields)
    def get(self):
        args = parser.parse_args()
        page = args.get('page')
        page_size = args.get('page_size')
        type_flag = args.get('type_flag')

        if page_size > 30:
            page_size = 30

        offset = page * (page_size - 1)
        if type_flag == 1 or type_flag == 2:
            movies = Movie.query.filter_by(flag=type_flag).limit(page_size).offset(offset).all()
        elif type_flag == 0:
            movies = Movie.query.limit(page_size).offset(offset).all()
        else:
            print('can shu wei fa ')
            return {'returnCode': '4xx', 'msg': 'fei fa canshu '}
        return {'returnValue': movies, 'pageNumber': page}
