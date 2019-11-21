from flask import render_template, flash, redirect, jsonify
from app import app
from app.forms import StickerForm, SampleLabelForm
from app.create_label import Label
from app.models import Collection, CollectionItem

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

@app.route('/sample_labels', methods=['GET', 'POST'])
def sample_labels():
    form = SampleLabelForm()
    if request.method == 'POST' and form.validate_on_submit():
        # TODO: Pass in the sample info and generate appropriate label
        if print_sample_label.data:
            pass

        elif print_crossover_label.data:
            pass

    # if form.validate_on_submit():
    	# flash('Label Being Created')
    	# label = Label()
    	# return redirect(label.generate_label(form.collection_name.data, \
    	# 	form.color_name.data, \
    	# 	form.order_num.data, \
    	# 	form.run_num.data, \
    	# 	form.run_date.data))
    	# return redirect('labels/hi.pdf')
    return render_template('samples.html', title='Print Sample Labels', form=form)

@app.route('/collection_items/<collection_id>')
def collection_items(collection_id):
    collection_items = Collection.query.\
                        filter_by(id=collection_id).first().items

    col_item_array = []
    for item in collection_items:
        collection_obj = {}
        collection_obj['id'] = item.id
        collection_obj['name'] = item.item_name
        # collection_obj['species'] = species
        # collection_obj['width'] = width
        # collection_obj['durability'] = durability
        # collection_obj['length'] = length
        # collection_obj['iw_name'] = iw_name
        # collection_obj['collection_id'] = collection_id
        col_item_array.append(collection_obj)

    return jsonify({'collection_items': col_item_array})
