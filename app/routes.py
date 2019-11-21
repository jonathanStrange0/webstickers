from flask import render_template, flash, redirect, jsonify, request
from app import app
from app.forms import StickerForm, SampleLabelForm
from app.create_label import ShippingLabel, SampleLabel
from app.models import Collection, CollectionItem

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = StickerForm()
    if form.validate_on_submit():
    	flash('Label Being Created')
    	label = ShippingLabel()
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


    if request.method == 'POST':# and form.validate_on_submit():
        print(form.errors)
        if form.is_submitted():
            print("submitted")
        if form.validate():
            print("valid")
        print(form.errors)
        # return('collection {}, SKU {}'.format(form.collection.data.collection_name,
        #                 CollectionItem.query.filter_by(id=form.collection_items.data).first().item_name))
        # # TODO: Pass in the sample info and generate appropriate label
        # print("Validated? ", form.validate_on_submit())
        if form.print_sample_label.data:
            print('pressed the print sample label button')
            sample_label = SampleLabel(form.collection_items.data)
            return redirect(sample_label.generate_sample_label())

        # elif form.print_crossover_label.data:
        #     pass
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
