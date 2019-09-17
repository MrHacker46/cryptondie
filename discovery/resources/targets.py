import sqlite3

from flask_restful import Resource, reqparse
from models.targets import TargetModel

def normalize_path(target_id = None, target_key = None, target_ip = None, target_hostname = None, target_city = None,
                   target_region = None, target_country = None, target_location = None, 
                   target_organization = None, target_postal = None, target_timezone = None):

    return {
        'target_id': target_id,
        'target_key': target_key,
        'target_ip': target_ip,
        'target_hostname': target_hostname,
        'target_city': target_city,
        'target_region': target_region,
        'target_country': target_country,
        'target_location': target_location,
        'target_organization': target_organization,
        'target_postal': target_postal,
        'target_timezone': target_timezone
    }

path_params = reqparse.RequestParser()
path_params.add_argument('target_id', type=str)
path_params.add_argument('target_key', type=str)
path_params.add_argument('target_ip', type=str)
path_params.add_argument('target_hostname', type=str)
path_params.add_argument('target_city', type=str)
path_params.add_argument('target_region', type=str)
path_params.add_argument('target_country', type=str)
path_params.add_argument('target_location', type=str)
path_params.add_argument('target_organization', type=str)
path_params.add_argument('target_postal', type=str)
path_params.add_argument('target_timezone', type=str)

class Targets(Resource):
    def get(self):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        data = path_params.parse_args()
        data_validate = {key:data[key] for key in data if data[key] is not None}
        parameters = normalize_path(**data_validate)

        query = "SELECT * FROM targets"

        create_tuple = tuple([parameters[key] for key in parameters])
        results = cursor.execute(query, ())

        targets = []

        for result in results:
            targets.append({
                'target_id': result[0],
                'target_key': result[1],
                'target_ip': result[2],
                'target_hostname': result[3],
                'target_city': result[4],
                'target_region': result[5],
                'target_country': result[6],
                'target_location': result[7],
                'target_organization': result[8],
                'target_postal': result[9],
                'target_timezone': result[10],
            })
        
        return targets

class Target(Resource):
    arguments = reqparse.RequestParser()
    arguments.add_argument('target_ip', type=str, required=True)
    arguments.add_argument('target_key', type=str, required=True)
    arguments.add_argument('target_hostname', type=str, required=True)
    arguments.add_argument('target_city', type=str, required=True)
    arguments.add_argument('target_region', type=str, required=True)
    arguments.add_argument('target_country', type=str, required=True)
    arguments.add_argument('target_location', type=str, required=True)
    arguments.add_argument('target_organization', type=str, required=True)
    arguments.add_argument('target_postal', type=str, required=True)
    arguments.add_argument('target_timezone', type=str, required=True)

    def get(self, target_id):
        target = TargetModel.find_target(target_id)

        if target:
            return target.json()
        
        return {'message': 'Target not found'}
    
    def post(self, target_id):
        if TargetModel.find_target(target_id):
            return {'message': 'Target id {0} already exists'.format(target_id)}

        data = Target.arguments.parse_args()
        target = TargetModel(target_id, **data)

        try:
            target.save_target()
        except:
            return {'message': 'Internal server error'}, 500
        
        return target.json()