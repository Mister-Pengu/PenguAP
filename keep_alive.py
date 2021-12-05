from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route("/")
def index():
  return "salo"

def run():
  app.run("0.0.0.0", 8080)

def keep_elive():
  t = Thread(target=run)
  t.start()
  