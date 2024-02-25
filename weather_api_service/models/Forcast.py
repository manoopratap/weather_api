from weather_api_service import db


class Forcast(db.Model):
    __tablename__ = 'forcasts'
    id = db.Column(db.Integer, db.Sequence('id',start=1000), primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(255), nullable=False)
    citi_name= db.Column(db.String(255), nullable=False)
    region= db.Column(db.String(255), nullable=False)
    country = db.Column(db.String(255), nullable=False)

    def __init__(self, username, full_name,citi_name,region,country):
        self.username = username
        self.full_name = full_name
        self.citi_name = citi_name
        self.region = region
        self.country = country

    def to_json(self):
        return dict(
            id=self.id,
            username=self.username,
            full_name=self.full_name,
            citi_name=self.citi_name,
            region=self.region,
            country=self.country
        )
