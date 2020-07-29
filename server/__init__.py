from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from .views.db import create_db_blueprint
from .views.nfe import create_nfe_blueprint


def create_app(config, debug):
    app = Flask(__name__)        
    app.secret_key = config["APP"]["SECRET_KEY"]
    app.config['SQLALCHEMY_DATABASE_URI'] = config['DATABASE']['URI']
    
    from server.database import db    
    db.init_app(app)
    
    nfe_blueprint = create_nfe_blueprint(debug, db)
    db_blueprint = create_db_blueprint(debug, db)
    
    app.register_blueprint(nfe_blueprint, url_prefix="/nfe")    
    app.register_blueprint(db_blueprint, url_prefix="/db")
    
    return app