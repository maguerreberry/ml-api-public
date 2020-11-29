# -*- coding: utf-8 -*-
import settings
import json
from flask import Flask, request
from time import strftime
from views import router

app = Flask(__name__)
app.register_blueprint(router)

@app.after_request
def after_request(response):
    timestamp = strftime('[%Y-%b-%d %H:%M]')
    print(json.dumps({
        'timestamp': timestamp,
        'method': request.method,
        'endpoint': request.full_path,
        'status_code': response.status_code,
    }))
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=settings.API_DEBUG)
