from server.database import db

class NotaFiscal(db.Model):
    __tablename__ = 'nfe'
    
    id = db.Column(db.Integer, primary_key=True)
    access_key = db.Column(db.String(120), unique=True, index=True, nullable=False, server_default='')
    total_value = db.Column(db.Float, nullable=False, default=0)

    
    def __repr__(self):
        return f'Nfe: {self.access_key} {self.total_value}'
    
    def to_dict(self):
        return {'access_key':self.access_key, 'total_value':self.total_value}