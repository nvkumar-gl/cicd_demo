from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/welcome')
def get_status():
    return jsonify({"message":"Welcome message"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
