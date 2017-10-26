from controller import LightController
from flask import Flask

app = Flask(__name__)
c = LightController()

@app.route('/on')
def on():
  c.on()

@app.route('/off')
def off():
  c.off()

