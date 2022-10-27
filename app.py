
from flask import Flask, make_response, request
import dbhelpers as dh
import apihelpers as a
import json
import dbcreds as d



app= Flask(__name__)

@app.patch('api/client')

def update_client():
    valid_check = a.check_endpoint_info(request.json, ['token', 'email', 'password', 'bio',
    'image_url'])
    





if(d.production_mode == True):
    print("Running in Production Mode")
    import bjoern #type:ignore
    bjoern.run(app, "0.0.0.0", 5000)
    app.run(debug=True)
else:
    from flask_cors import CORS
    CORS(app)
    print("Running in Testing Mode")
    app.run(debug=True)