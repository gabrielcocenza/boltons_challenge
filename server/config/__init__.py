def get_config(debug): 
    config = {
        "DATABASE": {
            "URI": 'postgresql://boltons:admin@postgres:5432'
        },
        "APP": { "SECRET_KEY": "dev" } 
        }
    
    if debug: 
        config['DATABASE']['URI'] = 'postgresql://boltons:admin@localhost:5432'   
    
    return config