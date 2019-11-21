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
        allow_blank=True, get_label='collection_name')

    # collection_items = QuerySelectField(query_factory=\
    #     lambda: CollectionItem.query.order_by('item_name'), \
    #     allow_blank=True, get_label='item_name')

    collection_items = SelectField(label='Flooring SKU', choices=[])
    print_sample_label = SubmitField(label='Print Sample Label')
    print_crossover_label = SubmitField(label='Print Crossover Label')
