# routes/auth.py

from flask import Blueprint, redirect, url_for, session, render_template, flash
from flask_login import login_user, logout_user, current_user
from extensions import db, oauth
from models.user import User
import os

auth_bp = Blueprint('auth', __name__)

google = oauth.register(
    name='google',
    client_id=os.getenv('GOOGLE_CLIENT_ID'),
    client_secret=os.getenv('GOOGLE_CLIENT_SECRET'),
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid email profile'
    }
)

@auth_bp.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('journal.dashboard'))
    return render_template('login.html')

@auth_bp.route('/login/google')
def google_login():
    redirect_uri = url_for('auth.google_authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@auth_bp.route('/login/google/authorize')
def google_authorize():
    try:
        token = google.authorize_access_token()
        user_info = token['userinfo']  # ✅ Correct way to access userinfo

        user = User.query.filter_by(email=user_info['email']).first()

        if not user:
            user = User(
                email=user_info['email'],
                name=user_info['name'],
                profile_pic=user_info.get('picture', '')
        )
            db.session.add(user)
            db.session.commit()

        login_user(user)
        flash('Logged in successfully!', 'success')
        return redirect(url_for('journal.dashboard'))
    except Exception as e:
        flash(f'Login failed: {str(e)}', 'danger')
        return redirect(url_for('auth.login'))

@auth_bp.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.index'))
