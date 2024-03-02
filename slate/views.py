from flask import render_template
from slate import app
from slate import db

with app.test_request_context():
    db.create_all()

@app.route('/', methods=['POST', 'GET'])
def main():
    return render_template('main.html')
