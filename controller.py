import RPi.GPIO as GPIO

class LightController:
  def __init__(self):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)

  def on(self):
    GPIO.output(17, GPIO.HIGH)

  def off(self):
    GPIO.output(17, GPIO.LOW)