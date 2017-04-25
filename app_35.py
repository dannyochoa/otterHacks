import os
from flask import Flask, render_template, request, url_for, redirect, send_from_directory
from werkzeug.utils import secure_filename
from label_image import getScores
from rot_segmentation import getRotRatio

score = 0
img = 'moc.jpg'

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
        global img
        img = url[index + 1:]
        global score
        score = getScores(img)
        # os.system("python label_image.py " + img)
        os.system("mv " + img + " static/")
        img = "static/" + img
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
    global score
    score = getScores("static/" + filename)
    global img
    img = "static/" + filename
    # os.system("python label_image.py static/"+filename)
    # Redirect the user to the uploaded_file route, which
    # will basicaly show on the browser the uploaded file
    return redirect(url_for('results'))


@app.route('/results')
def results():
    print(score)
    print("in results")
    if (score['notaleaf'] > .5):
        return render_template("results.html", rot='NA', health='NA', other='NA')
    else:
        print(img)
        os.system("rm static/rot.jpg")
        percentace_of_rot = getRotRatio(img)
        print("got it")
        return render_template("final.html", rot=(score['blackrot'] * 100), health=(score['notaleaf'] * 100),
                               other=(score['leaves'] * 100), percent=percentace_of_rot)


@app.route('/static/<img>')
def uploaded_file(img):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               img)


if __name__ == '__main__':
    app.run(
        debug=True,
        port=int(os.getenv('PORT', 8080)),
        host=os.getenv('IP', '0.0.0.0')
    )
