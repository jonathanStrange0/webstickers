from flask import render_template, flash, redirect
from app import app
from app.forms import StickerForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = StickerForm()
    if form.validate_on_submit():
    	flash('Label Being Created')
    	return redirect('/labels/hi.pdf')
    return render_template('index.html', title='Print Stickers', form=form)
