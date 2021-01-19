from flask import Flask
app = Flask("antenna-control-server")

@app.route('/')
def index():
    return 'Invalid request!'

@app.route('/query/info')
def query_info():
    return '{"status": "ready"}'

app.run(port='8080')