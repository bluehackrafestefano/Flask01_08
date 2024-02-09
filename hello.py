from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/products")
def products():
    return "<h1>Product Page</h1>"

if __name__ == '__main__':
    # app.run(debug=True)
    # app.run(debug=True, port=3003)
    app.run(host='0.0.0.0', port=80)
