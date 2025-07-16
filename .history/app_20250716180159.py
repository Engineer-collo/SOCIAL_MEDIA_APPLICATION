from flask import Flask, jsonify
import os
from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv('DATABASE_URL')
if not database_url:
    database_url = 'sqlite:///Social_media.db'

app = Flask(__name__)

# App configurations.
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False

# Index route 
@app.route('/', methods=['GET'])
def index():
    response = {
        "message" : 'Hello from Flask application!'
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=8000)