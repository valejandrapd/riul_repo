from flask import Blueprint, render_template

web_bp = Blueprint('web_bp', __name__)

@web_bp.route('/')
def index():
    return render_template('login.html')

@web_bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')