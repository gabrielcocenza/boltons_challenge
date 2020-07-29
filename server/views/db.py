from flask import Blueprint, render_template, jsonify
from server.models.notafiscal import NotaFiscal
from sqlalchemy.exc import SQLAlchemyError
from .utils import extract_total_value, get_nfes_data

def create_db_blueprint(debug, db):
    db_blueprint = Blueprint("db_blueprint", __name__)

    @db_blueprint.route("/repopulate", methods=['GET','POST'])
    def repopulate():
        try:
            db.drop_all()
            db.create_all()
            xml_nfes_data = get_nfes_data()
            for data in xml_nfes_data:
                _access_key = data['access_key']
                _total_value = extract_total_value(data['xml'])		
                nfe = NotaFiscal(access_key=_access_key, total_value=_total_value)                
                db.session.add(nfe)            
            db.session.commit()
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            return error
        
        code = '200'
        response = jsonify({'response': 'Database Repopulated'})
        return response, code

    @db_blueprint.route("/clear", methods=['GET','POST'])
    def clear():        
        db.drop_all()
        code = '200'
        response = jsonify({'response': 'Database Clear'})
        
        return response, code

    
    return db_blueprint
