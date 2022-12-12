from flask import Flask, render_template, request, send_from_directory
import RPi.GPIO as pi

SESSION_TYPE = "secret key"
app = Flask(__name__, static_url_path="")
app.secret_key = "secret key"
app.config["SESION_TYPE"] = "filesystem"

@app.route("/<path:path>")
def static_file(path):
    return app.send_static_file(path)

@app.route("/")
def index():
    return render_template("index.html")

yanık = False

@app.route("/yak")
def yak():
    global yanık
    pi.setmode(pi.BCM)
    pi.setwarnings(True)
    pi.setup(4, pi.OUT)
    if(yanık == False):
        pi.output(4, pi.HIGH)
        yanık = True
        return "yakıldı"
    else:
        pi.output(4, pi.LOW)
        yanık = False
        return "söndü"


if __name__=="__main__":
    app.secret_key="anahtar"
    app.run(debug=True, host="0.0.0.0")