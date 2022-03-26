from flask import render_template, Blueprint, redirect, url_for, request

registration = Blueprint('registration', __name__, template_folder='templates', static_folder='static')



@registration.route('/')
def index():
    return redirect(url_for('registration.reg'))


@registration.route('/registration/', methods=['GET', 'POST'])
def reg():
    name = request.form.get('username')
    password = request.form.get('psw')
    email = request.form.get('email')
    return render_template('registration.html', title='Регистрация', name=name, psw=password, email=email)
