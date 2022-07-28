
from unittest import result
from flask import Flask, request, render_template, jsonify, make_response
import util

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('app.html')

@app.route('/home_price', methods = ['POST', 'GET'])
def home_price():
    if request.method == 'POST':
        size = request.form['size']
        total_sqft = request.form['total_sqft']
        bath = request.form['bath']

        response = (util.predict_home_price(size,total_sqft, bath))
        # response.headers.add('Access-Control-Allow-Origin', '*')
        
        result = response
        return render_template('result.html', result = result)




if __name__ == "__main__":
    util.load_saved_artifacts()
    app.run(debug=True)