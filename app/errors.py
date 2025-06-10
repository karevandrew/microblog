"""Handle app errors."""

from flask import render_template
from app import app, db


@app.errorhandler(404)
def not_found_error(error):
    """Return HTML page when 404 error happens."""
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    """Return HTML page when 500 error happens."""
    db.session.rollback()
    return render_template('500.html'), 500
