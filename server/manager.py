from flask_restful import Api

api = Api()

def init_api(app):
    api.init_app(app)

from flask_migrate import MigrateCommand, migrate
from flask_script import Manager

from app import create_app

app = create_app('develop')
manager = Manager(app)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()
