from flask import Flask, request
from flask_cors import CORS
import time

# Custom Modules
from routes.routes import handler
from config.config import config
from middleware.controller import ascii
from config.custom import custom


# Initialize Flask app
app = Flask(__name__)

# Apply middleware
CORS(app)

# Middleware to log response time
@app.after_request
def after_request(response):
    start_time = time.time()
    response_time = time.time() - start_time
    print(f"{request.method} {request.path} {response_time:.2f}ms")
    return response

# Serve routes
handler(app)
arts = ascii.create_ascii_art("Ghost server !", "big_money-sw", 500) #big_money-sw, graceful, fire_font-k, big_money-se, big_money-ne, big_money-nw
custom.print(arts, custom.GREEN)

def start_server():
    try:
        print(f" * Ghost server started at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f" * HTTP Port: {config["application"]['port']}")
        app.run(port=config["application"]['port'], debug=True)
    except Exception as e:
        print(f"Server Start Failed: {e}")

if __name__ == '__main__':
    start_server()
