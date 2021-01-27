from flask import Flask, jsonify, request

from flask_cors import CORS

from datetime import datetime
import pytz
val = []


# configuration

DEBUG = True



# instantiate the app

app = Flask(__name__)

app.config.from_object(__name__)



# enable CORS

CORS(app, resources={r'/*': {'origins': '*'}})





# sanity check route

@app.route('/ping', methods=['GET', 'POST'])
    

def clock_face():
    
    timeZones = {
     "EST": "0",
     "CST": "1",
     "MST": "2",
     "PST": "3"
     }
    i = len(val) - 1
    if request.method == 'POST':
        post_data = request.get_json()
        #print(post_data)
        #print(post_data.get('time'))
        val.append(post_data.get('time'))
        
    else:
        print(val)
        
    print(timeZones[val[i]])
    return jsonify(timeZones[val[i]])
    
    


if __name__ == '__main__':

    app.run()
