from flask import Flask  # Imports the Flask class from the flask module
app = Flask(__name__)    # Creates an instance of the Flask application

@app.route("/")          # Defines a route for the root URL
def hello():             
    return "whhhat isss goiiing on"  # Response returned when the root URL is accessed

if __name__ == "__main__":           # Ensures the app runs only if this file is executed directly
    app.run(host="0.0.0.0", port=5000)  # Runs the app on all available network interfaces on port 5000
