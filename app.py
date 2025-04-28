from flask import Flask, render_template
from dotenv import load_dotenv
from extensions import db, login_manager, oauth
from flask_wtf import CSRFProtect
from markupsafe import Markup, escape
from datetime import datetime, timezone
import os

# ======================
# Load environment variables
# ======================
load_dotenv()

# ======================
# Initialize Flask App
# ======================
app = Flask(__name__)

app.config.update(
    SECRET_KEY=os.getenv('SECRET_KEY'),
    SQLALCHEMY_DATABASE_URI='sqlite:///journal.db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

# ======================
# Initialize Extensions
# ======================
db.init_app(app)
login_manager.init_app(app)
oauth.init_app(app)
csrf = CSRFProtect(app)   # ✅ CSRF Protection properly attached to app

# ======================
# Import Models
# ======================
from models.user import User
from models.entry import Entry

# ======================
# Flask-Login User Loader
# ======================
@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

# ======================
# Import Blueprints
# ======================
from routes.auth import auth_bp
from routes.journal import journal_bp
from routes.main import main_bp

# ======================
# Register Blueprints
# ======================
app.register_blueprint(auth_bp)
app.register_blueprint(journal_bp)
app.register_blueprint(main_bp)

# ======================
# Create Database Tables
# ======================
with app.app_context():
    db.create_all()

# ======================
# Template Contexts
# ======================
@app.context_processor
def inject_now():
    """ Inject current UTC datetime into templates. """
    return {'now': datetime.now(timezone.utc)}
 # Secure session cookies
    SESSION_COOKIE_HTTPONLY=True,   # prevent JavaScript access to cookie
    SESSION_COOKIE_SECURE=False,    # set True if you deploy with HTTPS!
    SESSION_COOKIE_SAMESITE='Lax'   # prevent CSRF between sites

# ======================
# Custom Jinja2 Filters
# ======================
@app.template_filter('nl2br')
def nl2br_filter(s):
    """ Convert newlines in text to <br> for display. """
    if s is None:
        return ''
    return Markup(escape(s).replace('\n', '<br>\n'))


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

# ======================
# Run Server
# ======================
if __name__ == '__main__':
    app.run(debug=True)
