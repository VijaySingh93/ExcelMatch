from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed


class compare_excel(FlaskForm):
    file_path1 = FileField('Select file 1',
                             validators=[FileRequired('File was empty!')])
    file_path2 = FileField('Select file 2',
                             validators=[FileRequired('File was empty!')])
    submit = SubmitField('Compare')