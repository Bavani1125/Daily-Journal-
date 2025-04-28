# routes/main.py

from flask import Blueprint, render_template, redirect, url_for, request, Response
from flask_login import current_user
import requests

main_bp = Blueprint('main', __name__)

# 🏡 Landing or redirect to dashboard
@main_bp.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('journal.dashboard'))
    return render_template('index.html')

# ℹ️ About page
@main_bp.route('/about')
def about():
    return render_template('about.html')

# 🛡️ Privacy Policy page
@main_bp.route('/privacy')
def privacy():
    return render_template('privacy.html')

# 🖼️ Safe proxy to load external images like Google Profile Pics
@main_bp.route('/proxy-image')
def proxy_image():
    url = request.args.get('url')
    if not url:
        return 'Missing URL', 400
    try:
        resp = requests.get(url, timeout=5)
        return Response(resp.content, content_type=resp.headers.get('Content-Type', 'image/jpeg'))
    except Exception:
        return 'Image fetch failed', 500
