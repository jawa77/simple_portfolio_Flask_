import sys
sys.path.append('/home/jawa/Desktop/Program/raspberry/python_hard/websites')


from flask import Flask
from flask import Flask, redirect, url_for, request, render_template, session
import os
import math
import base64
from blueprints import home

application = app = Flask(__name__, static_folder='assets', static_url_path="/")
# app.secret_key = get_config("secret_key")
# app.register_blueprint()



# all functionality wrote in blueprints

app.register_blueprint(home.bp)


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=7000, debug=True)
