import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    """Root endpoint returning basic service status."""
    return jsonify({
        "message": "Welcome !",
        "status": "running"
    })

@app.route('/health', methods=['GET'])
def health_check():
    """Healthcheck endpoint used by orchestrators (K8s/Docker) and CI/CD pipelines."""
    return jsonify({
        "status": "UP",
        "service": "flask-app"
    }), 200

@app.route('/description', methods=['GET'])
def message():
    return "<p>The purpose of this website is to help me practice developing and optimizing an entire project using a DevSecOps approach.</p> <h1>Specifically: Develop a web microservice, containerize it properly, automate testing, build an automated CI/CD pipeline</h1>"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)