from flask import Flask, jsonify, render_template
from controller import *

# Create an instance of the Flask application
app = Flask(__name__)

# Define the route for the root URL
@app.route('/')
def index():
    # Render the 'view.html' template
    return render_template('view.html')  

# Define the route for '/fetch_data'
@app.route('/fetch_data')
def fetch_data_route():
# Return data from the 'get_data()' method of the Controller class as JSON
    return jsonify(controller.get_data())  

if __name__ == '__main__':
    # Create an instance of the Controller class
    controller = Controller() 
    
    # Run the Flask application in debug mode on port 5001
    app.run(debug=True, port=5001)
