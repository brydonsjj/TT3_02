from flask import Flask

app = Flask(__name__)
app.debug = True


@app.route('/')
def home():
    return {"message": "hello there my name"}
