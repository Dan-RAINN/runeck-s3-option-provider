from flask import Flask
from flask import Response
from flask import request
from boto.s3.connection import S3Connection
import json

app = Flask(__name__)
conn =  S3Connection()
bucket = ['your_bucket_name']
artifact_bucket = conn.get_bucket(bucket)

@app.route('/')
def rundeck-s3-option-provider():
    artifacts_list = []
    artifacts_folder = request.args.get('artifacts_folder', '')
    for key in artifact_bucket.list():
        if str(key.name).startswith(artifacts_folder) is True:
            artifacts_list.append(key.name)
    return Response(json.dumps(artifacts_list), mimetype='application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

