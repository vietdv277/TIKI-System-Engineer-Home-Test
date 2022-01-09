from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/')
def index():
        return dict(**request.headers, client_ip=request.headers.environ['REMOTE_ADDR'])


if __name__ == '__main__':
    app.run(debug=True)
