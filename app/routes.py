from flask import render_template, flash, redirect
from app import app
from app.forms import StickerForm
from app.create_label import Label

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = StickerForm()
    if form.validate_on_submit():
    	flash('Label Being Created')
    	label = Label()
    	print(form.collection_name.data, \
    		form.color_name.data, \
    		form.order_num.data, \
    		form.run_num.data, \
    		form.run_date.data)
    	return redirect(label.generate_label(form.collection_name.data, \
    		form.color_name.data, \
    		form.order_num.data, \
    		form.run_num.data, \
    		form.run_date.data))
    	# return redirect('labels/hi.pdf')
    return render_template('index.html', title='Print Stickers', form=form)
