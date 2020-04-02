from flask import Flask


app = Flask(__name__)


@app.route('/ip')
def index():
    return 'l'


if __name__ == '__main__':
    app.run(debug=True)
