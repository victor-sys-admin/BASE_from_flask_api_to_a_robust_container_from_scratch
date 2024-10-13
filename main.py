#!/usr/bin/env python
"""
Author      : Vik
Filename    : main.py
Project     : Demo API
Description : Main and unique file for the demo API project
"""

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    """function for the root of the API"""
    app.logger.info("Receiving request")
    return jsonify({"Welcome": "This is a demo API"}), 200

@app.route("/health", methods=["GET"])
def get_health():
    """API Function to get health of the API and vaultwarden"""
    app.logger.info("Receiving request")
    return jsonify({"success": "The API is UP"}), 200

def main():
    """Main function"""
    app.run(host="127.0.0.1", port=5001)

if __name__ == "__main__":
    main()
