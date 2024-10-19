from flask import Flask, request, jsonify,render_template
import os
from flask_cors import CORS, cross_origin
from spams import prediction

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    data = request.json["data"]
    p = prediction(data)
    print(p)
    print(type(p))
    return {"Result": str(p)}


#port = int(os.getenv("PORT"))
if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=port)
    app.run(host='0.0.0.0', port=4000, debug=True)