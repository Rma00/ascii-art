import os


config = {
    "appEnv": os.getenv('NODE_ENV'),
    "application": {
        "port": os.getenv('PORT') if os.getenv('PORT') else 8081,
        "token": os.getenv('TOKEN'),
        "isMaintenance": False,
        "maintenanceMessage": "Scheduled maintenance activity is going on, System will be available soon.",
        "versionNumbers": os.getenv('VERSIONS', '').split(', '),
        "jwtSecret": os.getenv('JWT_SECRET'),
        "jwtSecretAndroid": os.getenv('JWT_SECRET_ANDROID')
    }
}

