from sql_alchemy import database

class TargetModel(database.Model):
    __tablename__ = 'targets'

    target_id = database.Column(database.String, primary_key=True)
    target_key = database.Column(database.String(16))
    target_ip = database.Column(database.String(15))
    target_hostname = database.Column(database.String(80))
    target_city = database.Column(database.String(80))
    target_region = database.Column(database.String(80))
    target_country = database.Column(database.String(80))
    target_location = database.Column(database.String(80))
    target_organization = database.Column(database.String(80))
    target_postal = database.Column(database.String(20))
    target_timezone = database.Column(database.String(20))

    def __init__(self, target_id, target_key, target_ip, target_hostname,
                 target_city, target_region, target_country, target_location,
                 target_organization, target_postal, target_timezone):
        
        self.target_id = target_id
        self.target_key = target_key
        self.target_ip = target_ip
        self.target_hostname = target_hostname
        self.target_city = target_city
        self.target_region = target_region
        self.target_country = target_country
        self.target_location = target_location
        self.target_organization = target_organization
        self.target_postal = target_postal
        self.target_timezone = target_timezone

    def json(self):
        return {
            'target_id': self.target_id,
            'target_key': self.target_key,
            'target_ip': self.target_ip,
            'target_hostname': self.target_hostname,
            'target_city': self.target_city,
            'target_region': self.target_region,
            'target_country': self.target_country,
            'target_location': self.target_location,
            'target_organization': self.target_organization,
            'target_postal': self.target_postal,
            'target_timezone': self.target_timezone
        }
        
    @classmethod
    def find_target(cls, target_id):
        target = cls.query.filter_by(target_id=target_id).first()

        if target:
            return target
        return None
        
    def save_target(self):
        database.session.add(self)
        database.session.commit()
