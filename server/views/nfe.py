from flask import Blueprint, render_template, jsonify
from server.models.notafiscal import NotaFiscal


def create_nfe_blueprint(debug, db):
    nfe_blueprint = Blueprint("nfe_blueprint", __name__)

    @nfe_blueprint.route('/', methods=['GET'])
    def count_nfe():    
        result = db.session.query(NotaFiscal).count()        
        code = '200'
        response = jsonify({'response': f'Currently {result} notes registered' })
        
        return response, code

    
    @nfe_blueprint.route('/<string:key>', methods=['GET'])
    def get_single(key):    
        nfe = db.session.query(NotaFiscal).filter_by(access_key=key).first()
        code = '200'
        if not nfe:
            return jsonify({'response': f'key {key} not found'}), code
        
        response = jsonify(nfe.to_dict())
        return response, code
        
        
    
    return nfe_blueprint

