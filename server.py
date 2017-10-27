from controller import LightController
from flask import Flask

app = Flask(__name__)
c = LightController()

@app.route('/on')
def on():
  c.on()
  return 'light is ON'

@app.route('/off')
def off():
  c.off()
  return 'light is OFF'

app.run(host='0.0.0.0', port=4000)
