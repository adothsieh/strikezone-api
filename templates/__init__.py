from flask import Flask
import sys

app = Flask(__name__, static_folder="./public", template_folder="./static")

from templates.main.views import main_blueprint

# register blueprints
app.register_blueprint(main_blueprint)

