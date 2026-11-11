
from flask import Blueprint, jsonify

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return jsonify({
        "application": "SecureFlow",
        "message": "DevSecOps Pipeline Application",
        "status": "running"
    })

@main.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    }), 200

@main.route("/api/info")
def info():
    return jsonify({
        "project": "SecureFlow",
        "purpose": "Automated Vulnerability Scanning",
        "version": "1.0"
    })
