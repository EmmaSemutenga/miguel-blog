from flask import Flask

app = Flask(__name__)


#this avoid circular imports
from blog_app import routes