# ascii-art

**Project Title: ASCII Art Generator with Flask**

**Project Description:**
This project is a Python-based web application built using the Flask framework that allows users to generate ASCII art. It provides two RESTful APIs: one for retrieving a list of available ASCII art fonts and another for generating ASCII art based on user input. The application is designed to handle requests seamlessly and return visually appealing ASCII representations of user-provided text.

**Features:**

**List Available Fonts:**
  - API Endpoint: /ascii_fonts
  - Method: GET
  - Description: Returns a list of all fonts available for generating ASCII art.
  **Example Curl Command:**

  **curl --location 'http://127.0.0.1:8081/ascii_fonts'**

**Generate ASCII Art:**

  - API Endpoint: /ascii_arts
  - Method: POST
  - Description: Accepts user input in JSON format, including the text to convert and the font name, and returns the corresponding ASCII art.
  **Example Curl Command:**

  **curl --location 'http://127.0.0.1:8081/ascii_arts' \
  --header 'Content-Type: application/json' \
  --data '{
      "text": "Server !",
      "font": "big_money-sw"
  }'**

**Setup Instructions:**
  
  - Clone the repository from GitHub.
  - Navigate to the project directory.
  - Create venv : python3 -m venv venv
  - Activate venv : source venv/bin/activate
  - Install the required dependencies : pip install -r requirements.txt
  - Run the Flask application : python3 app.py 🚀
