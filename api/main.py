from flask import Flask, request, jsonify
from flask_cors import CORS
from routes.problems import problems_bp
from routes.users import users_bp

app = Flask(__name__)

app.register_blueprint(problems_bp)
app.register_blueprint(users_bp)


@app.route('/')
def helloWorld():
    return jsonify({"OK":"The unofficial PbInfo API is up and running!"}), 200


if __name__ == "__main__":
    app.run(debug=True)