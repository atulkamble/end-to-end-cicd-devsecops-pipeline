from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message": "Welcome to the DevSecOps CI/CD Demo App", "status": "healthy"})


@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/version")
def version():
    return jsonify({"version": "1.0.0", "app": "devsecops-demo"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
