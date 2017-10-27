from controller import LightController
from flask import Flask

app = Flask(__name__)
c = LightController()

@app.route('/')
def index():
  return '''
    <style>a { font-size: 300%; } div {display: block; margin: 20px;}</style>
    <div><a href="/on">on</a></div>
    <div><a href="/off">off</a></div>
  '''

@app.route('/on')
def on():
  c.on()
  return '''
    <style>a { font-size: 300%; } div {display: block; margin: 20px;}</style>
    <div><a href="/on">on</a></div>
    <div><a href="/off">off</a></div>
  '''

@app.route('/off')
def off():
  c.off()
  return '''
    <style>a { font-size: 300%; } div {display: block; margin: 20px;}</style>
    <div><a href="/on">on</a></div>
    <div><a href="/off">off</a></div>
  '''

app.run(host='0.0.0.0', port=4000)

