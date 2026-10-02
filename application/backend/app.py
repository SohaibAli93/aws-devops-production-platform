from flask import Flask, jsonify
import socket
import os

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "AWS DevOps Production Platform",
        "status": "running",
        "hostname": socket.gethostname(),
        "environment": os.getenv("APP_ENV", "development")
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    }), 200


@app.route("/api/tasks")
def tasks():
    return jsonify([
        {
            "id": 1,
            "title": "Build Docker Image",
            "status": "completed"
        },
        {
            "id": 2,
            "title": "Deploy to Kubernetes",
            "status": "pending"
        },
        {
            "id": 3,
            "title": "Configure Monitoring",
            "status": "pending"
        }
    ])


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", 5000))
    )