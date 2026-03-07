from flask import Flask
from flask_cors import CORS
import config

app = Flask(__name__)

# Load configuration
app.config['SECRET_KEY'] = config.SECRET_KEY
CORS(app)

# Register routes
@app.route('/')
def index():
    return "Hello from Flask!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
