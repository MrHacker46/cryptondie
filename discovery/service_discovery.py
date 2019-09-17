from flask import Flask, jsonify
from flask_restful import Api, Resource
from resources.targets import Targets, Target

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_NOTIFICATIONS"] = False

api = Api(app)

@app.before_first_request
def create_database():
    database.create_all()

api.add_resource(Targets, '/targets')
api.add_resource(Target, '/target/<string:target_id>')

if __name__ == '__main__':
    from sql_alchemy import database
    
    database.init_app(app)
    app.run(host='0.0.0.0', debug=True)