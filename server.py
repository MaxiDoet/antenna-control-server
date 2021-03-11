from flask import Flask
from io import io_connect, io_write
import json

app = Flask("antenna-control-server")

# Read config
try:
  config_file=open("config.json", "r")
  config=json.loads(config_file.read())
except:
  print("Couln't read configfile!")
  exit(1)

def get_config_value(key):
  try:
    return config[key]
  except:
    print("Couldn't find %s in config!" % key)
    return False

# Init serial device
ser = io_connect(get_config_value("serialDevice"))

@app.route('/')
def index():
    return 'Invalid request!'

@app.route('/query/info')
def query_info():
    return '{"status": "ready"}'

app.run(port='8080')