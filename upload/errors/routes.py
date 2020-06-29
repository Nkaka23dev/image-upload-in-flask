from flask import Blueprint,render_template

errors=Blueprint('errors',__name__)

@errors.app_errorhandler(404)
def error404(error):
    return render_template('error.html',title='error')