from flask import Flask
app = Flask(__name__)
from app import routes
print("The Munin started observability")