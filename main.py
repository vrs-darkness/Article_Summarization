from flask import Flask, render_template, request, jsonify
from Summarize import Summarize
# from flask_cors import CORS
# from urllib.parse import unquote
app = Flask(__name__)
summary = Summarize()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/summarize_url', methods=['POST'])
async def summarize_url():
    # print("hi")
    url = request.form['data']
    if "medium" in url:
        result = await summary.Summarize_url(url)
        return render_template("summary.html", data=result)
    else:
        return render_template(
            "summary.html",
            data="Can't Summarize websites Other than medium")


@app.route('/summarize_text', methods=['POST'])
async def summarize_text():
    # print("hi")
    data = request.form['data']
    if (len(data.split("\n")) > 2):
        result = await summary.Summarize_para(data)
        print(result)
        return render_template("summary.html", data=result)
    else:
        return render_template(
            "summary.html",
            data="Please give more that 50 Sentences for summarization !!")


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@app.errorhandler(500)
def server(e):
    return jsonify(error=str(e)), 500


if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port=5000, debug=True)
