from flask import render_template, flash, redirect, jsonify, request, url_for
from app import app
from app.forms import StickerForm, SampleLabelForm, NewProductForm
from app.create_label import ShippingLabel, SampleLabel, CrossoverLabel
from app.models import Collection, CollectionItem
from app import db

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
        print("Validated? ", form.validate_on_submit())
        if form.print_sample_label.data:
            print('pressed the print sample label button')
            sample_label = SampleLabel(form.collection_items.data)
            return redirect(sample_label.generate_sample_label())

        elif form.print_crossover_label.data:
            print('pressed the print crossover label button')
            crossover_label = CrossoverLabel(form.collection_items.data)
            return redirect(crossover_label.generate_crossover_label())
        # elif form.delete_product_button.data:
        #     delete_item = CollectionItem.query.filter_by(id=form.collection_items.data).first()
        #     db.session.delete(delete_item)
        #     db.session.commit()
        #     return render_template('samples.html', title='Print Sample Labels', form=form)
        # elif form.delete_collection_button.data:
        #     delete_item = form.collection.data
        #     db.session.delete(delete_item)
        #     db.session.commit()
        #     return(redirect(url_for('sample_labels'))) #render_template('samples.html', title='Print Sample Labels', form=form)
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

        col_item_array.append(collection_obj)

    return jsonify({'collection_items': col_item_array})

@app.route('/new_product', methods=['GET', 'POST'])
def new_product():
    form = NewProductForm()
    if request.method == 'POST' and form.validate_on_submit():
        flash('Your product is being created')
        collection_name = form.collection_name.data
        collection = None
        color_name = form.color_name.data
        species = None
        width = None
        durability = None
        length = None
        iw_name = None
        if len(Collection.query.filter_by(collection_name=collection_name).all()) ==0:
            collection = Collection(collection_name=collection_name)
            db.session.add(collection)
            db.session.commit()
        else:
            collection = Collection.query.filter_by(collection_name=collection_name).first()
        if len(CollectionItem.query.filter_by(item_name=color_name).all()) ==0:
            color_name = CollectionItem(item_name=color_name)
            db.session.add(color_name)
            db.session.commit()
        else:
            color_name = CollectionItem.query.filter_by(item_name=color_name).first()
        color_name.collection_id = collection.id
        color_name.species = form.species.data
        color_name.width = form.width.data
        color_name.durability = form.durability.data
        color_name.length = form.length.data
        color_name.iw_name = form.iw_name.data

        db.session.commit()

        return(redirect(url_for('new_product')))



    return render_template('new_products.html', title='Make New Products', form=form)


@app.route('/delete_product/<product_id>')
def delete_product(product_id):
    delete_item = CollectionItem.query.filter_by(id=product_id).first()
    db.session.delete(delete_item)
    db.session.commit()
    return(redirect(url_for('sample_labels'))) #render_template('samples.html', title='Print Sample Labels', form=form)

@app.route('/delete_collection/<collection_id>')
def delete_collection(collection_id):
    delete_item = Collection.query.filter_by(id=collection_id).first()
    db.session.delete(delete_item)
    db.session.commit()
    return(redirect(url_for('sample_labels'))) #render_template('samples.html', title='Print Sample Labels', form=form)
