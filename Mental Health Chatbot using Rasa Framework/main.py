########################################################################################
######################          Import packages      ###################################
########################################################################################
from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from __init__ import create_app, db

########################################################################################
# our main blueprint
main = Blueprint('main', __name__,static_folder="static", template_folder='templates')

@main.route('/')  # home page that returns 'index'
def index():
    return render_template('index.html')

@main.route('/profile')  # profile page that returns 'profile'
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/detect')
@login_required
def detect():
    return render_template('detect.html')



app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
