import os
from flask import Flask, render_template, request, url_for, redirect
from werkzeug import secure_filename
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/'


@app.route('/')
def login():
    return render_template('homepage.html')


@app.route('/', methods=['POST'])
def login_process():
    # this is the user input
    # *************************************
    # modifies the global username variable for later use
    print("in")
    url = request.form['url']
    #	file = request.files['file']
    #	filename = secure_filename(file.filename)
    #	file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #	return redirect(url_for('uploaded_file',
    #                               filename=filename))
    # *************************************
    print(url)
    # checks the user name and password. if they match this part of the code will redirect them to
    # the logged_in. If the username does not match the password it the code will redirect them to
    # a screen where they are told that they have entered the wrong input
    if (request.form['submit'] == "login"):
        os.system("wget " + url)
        i = 0
        index = 0
        for word in url:
            if (word == '/'):
                index = i
            i = i + 1
        img = url[index + 1:]
        print("IMG")
        os.system("python label_image.py " + img)
        os.system("mv " + img + " static/")
        return redirect(url_for('results'))


@app.route('/upload', methods=['POST'])
def upload():
    # Get the name of the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    # if file and allowed_file(file.filename):
    # Make the filename safe, remove unsupported chars
    filename = secure_filename(file.filename)
    # Move the file form the temporal folder to
    # the upload folder we setup
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    os.system("python label_image.py static/" + filename)
    # Redirect the user to the uploaded_file route, which
    # will basicaly show on the browser the uploaded file
    return redirect(url_for('results'))


@app.route('/results')
def results():
    return render_template("results.html")


@app.route('/static/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


if __name__ == '__main__':
    app.run(
        debug=True,
        port=int(os.getenv('PORT', 8080)),
        host=os.getenv('IP', '0.0.0.0')
    )
