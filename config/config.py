import os


config = {
    "appEnv": os.getenv('NODE_ENV'),
    "application": {
        "port": os.getenv('PORT') if os.getenv('PORT') else 8081
    }
}

