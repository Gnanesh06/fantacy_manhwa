from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load the mock data from JSON
def load_data():
    with open('manhwa.json') as f:
        return json.load(f)

# Route for the homepage
@app.route('/')
def index():
    manhwa_list = load_data()
    return render_template('index.html', manhwa_list=manhwa_list)

if __name__ == '__main__':
    app.run(debug=True)
