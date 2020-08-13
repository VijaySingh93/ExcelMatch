import os
from flask import Flask, render_template, flash, redirect, url_for, request
from forms import compare_excel
from flask_uploads import UploadSet, configure_uploads, DOCUMENTS, patch_request_class
from compare import xcel_compare

app = Flask(__name__)
app.config['SECRET_KEY'] = 'This is for excel comparison'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['UPLOADS_DEFAULT_DEST'] = os.path.join(basedir, 'uploads')

excels = UploadSet('excels', DOCUMENTS)
configure_uploads(app, excels)
patch_request_class(app)


@app.route("/")
def home():
    return render_template('main.html')


@app.route('/showdiff', methods=['GET', 'POST'])
def compare():
    form = compare_excel()
    if request.method == 'GET':
        return render_template('compareform.html', form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            filename1 = excels.save(form.file_path1.data)
            filename2 = excels.save(form.file_path2.data)
            filepath1 = excels.url(filename1)
            filepath2 = excels.url(filename2)
            result = xcel_compare(filepath1, filepath2)
            if type(result) == tuple:
                return render_template('result.html',
                                        result=result[0],
                                        columns=result[1])
            else:
                return render_template('error.html',
                                        result=result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
