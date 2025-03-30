from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api", methods=["GET"])
def my_service():
     return jsonify({
        "message": "Hello, I’m Jhon Frank, a software developer in the frontend area. My work is crucial for ensuring a seamless user experience and a responsive, high-performance interface.",  
    })
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
