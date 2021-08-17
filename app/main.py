from flask import Blueprint, request, redirect, url_for, render_template
from .classes.model import Users

main = Blueprint('main', __name__)

@main.route('/')
def index():
    data = Users.get_users()
    return render_template('index.html', list_data=data)

@main.route('/', methods=['POST'])
def mod_post():
    email = request.form.get('email')
    name = request.form.get('name')
    if request.form.get("submit_add"):
        Users.write_user(name, email)
    if request.form.get("submit_del"):
        Users.remove_user(name, email)
    return redirect(url_for('main.index'))



