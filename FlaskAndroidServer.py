from flask import Flask
from flask import request
from werkzeug.utils import secure_filename
import os.path
from flask import jsonify

app = Flask(__name__)


@app.route("/", methods=['POST'])
def upload():
    file = request.files['image']
    filename = secure_filename(file.filename)

    path = 'C:\\recorded_gestures'

    updatedfilename = os.path.join(path, filename)
    file.save(updatedfilename)
    resp = jsonify(success=True)
    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0")