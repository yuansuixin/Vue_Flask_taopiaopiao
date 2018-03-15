from flask_restful import Api

from app.apis import CityResource
from app.apis.CityResource import CitiesResource
from app.apis.MovieResource import MoviesResource

api = Api()

def init_api(app):
    api.init_app(app)


api.add_resource(CitiesResource,'/cities/')
api.add_resource(MoviesResource,'/movies/')