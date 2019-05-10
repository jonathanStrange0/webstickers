from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class StickerForm(FlaskForm):
    collection_name = StringField('Collection', validators=[DataRequired()])
    color_name = StringField('Color', validators=[DataRequired()])
    order_num = StringField('Order Number', validators=[DataRequired()])
    run_num = StringField('Run Number', validators=[DataRequired()])
    run_date = StringField('Run Date')
    submit = SubmitField('Print Label')
