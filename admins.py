from flask import render_template, redirect, Blueprint, url_for
from flask_login import login_required, current_user,logout_user

admin_bp = Blueprint('admin_bp', __name__)
