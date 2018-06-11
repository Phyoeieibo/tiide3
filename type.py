from flask import Flask
app=flask(__name__)
@app.route("/")
def type():
    return "Typing.........."
@app.route("/tiide3")
def tiide3():
    return "Hello Tiide3"

