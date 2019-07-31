from flask import Flask, flash, redirect, render_template, request, session, abort


app = Flask(__name__)

@app.route("/")
def index():
    return "Index!"
@app.route("/hello")
def Hello():
    return "Hello World!"

@app.route("/hello/<string:name>/")
def temp():
    return render_template(
    'test.html', name=name)</string:name>
  



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)