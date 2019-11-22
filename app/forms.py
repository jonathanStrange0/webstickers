from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired
from app.models import Collection, CollectionItem

class StickerForm(FlaskForm):
    collection_name = StringField('Collection', validators=[DataRequired()])
    color_name = StringField('Color', validators=[DataRequired()])
    order_num = StringField('Order Number', validators=[DataRequired()])
    run_num = StringField('Run Number', validators=[DataRequired()])
    run_date = StringField('Run Date')
    submit = SubmitField('Print Label')

class SampleLabelForm(FlaskForm):
    collection = QuerySelectField(query_factory=\
        lambda: Collection.query.order_by('collection_name'), \
            allow_blank=True, get_label='collection_name',
                validators=[DataRequired()])

    collection_items = SelectField(label='Flooring SKU', coerce=int, choices=[])
    print_sample_label = SubmitField('Print Sample Label')
    print_crossover_label = SubmitField('Print Crossover Label')
    # delete_product_button = SubmitField('Delete this product')
    # delete_collection_button = SubmitField('Delete this whole colletion')

class NewProductForm(FlaskForm):
    collection_name = StringField('Collection Name', validators=[DataRequired()])
    color_name = StringField('Color Name', validators=[DataRequired()])
    species = StringField('Species', validators=[DataRequired()])
    width = StringField('Width', validators=[DataRequired()])
    durability = StringField('Durability', validators=[DataRequired()])
    length = StringField('Length Structure', validators=[DataRequired()])
    iw_name = StringField('IW Crossover Name', validators=[DataRequired()])
    save = SubmitField('Save New Product')
