from flask import render_template,flash,redirect,url_for,request,Blueprint,request
from upload.users.forms import CreateAccount,LoginForm
from upload import bcrypt,db
from upload.models import User
from flask_login import login_user,login_required,logout_user,current_user
from .utils import save_picture

users=Blueprint('users',__name__)

@users.route('/register',methods=['GET','POST'])
def register():
    form=CreateAccount()
    if form.validate_on_submit():
        name=form.name.data
        password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        image_file=save_picture(form.profile.data)
        user=User(name=name,password=password,image_file=image_file)
        db.session.add(user)
        db.session.commit()
        flash('{} Your data has been submitted'.format(form.name.data),'success')
        return redirect(url_for('main.index'))
    return render_template('register.html',title='Account',form=form)

@users.route('/retrieve')
@login_required
def retrieve():
    page=request.args.get('page',1,type=int)
    users=User.query.order_by(User.id.desc()).paginate(per_page=2,page=page)
    return render_template('retrieve.html',users=users)

@users.route('/delete/<int:user_id>',methods=['POST'])
def delete(user_id):
    user=User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    flash(F'{user.name} is removed from the database','danger')
    return redirect(url_for('main.index')) 

@users.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(name=form.name.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user)
            next_page=request.args.get('next')
            flash(f'{user.name} you have signed in','info')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        else:
            flash('Invalid Username and Password!','danger')
    return render_template('login.html',title='Login',form=form)

@users.route('/logout/user')
def logout():
    logout_user()
    return redirect(url_for('main.index'))