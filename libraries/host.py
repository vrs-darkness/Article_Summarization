from flask import Flask,request, jsonify
from main1 import main
from flask_cors import CORS
from urllib.parse import unquote


app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/get',methods=['POST'])
def summarize():
    print("hi")
    inp = request.json
    url = unquote(inp['data'])
    output = main(url)
    return {"data":output}

if __name__ =='__main__':
    app.run(port=5000,debug=True)