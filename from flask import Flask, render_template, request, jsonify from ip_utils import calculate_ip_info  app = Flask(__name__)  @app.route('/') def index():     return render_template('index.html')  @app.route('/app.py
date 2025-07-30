from flask import Flask, render_template, request, jsonify
from ip_utils import calculate_ip_info

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    ip_input = data.get('ip')
    result = calculate_ip_info(ip_input)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
