from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlreg import femail, fphone, fpassword, fill_data
app = Flask(__name__)
import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
@app.route("/")
def sanity_check():
    return femail
if __name__ == "__main__":
    app.run(debug=True)
