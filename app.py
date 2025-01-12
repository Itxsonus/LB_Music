from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Rahul'


if _name_ == "__main__":
  app.run()
