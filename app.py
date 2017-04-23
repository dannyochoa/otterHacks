import os
import re
from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)
@app.route('/')
def login():
    return render_template('homepage.html')
    
@app.route('/', methods = ['POST'])
def login_process():
	#this is the user input 
	#*************************************
	#modifies the global username variable for later use
	print ("in")
	url = request.form['url']
	#*************************************
	print (url)
	#checks the user name and password. if they match this part of the code will redirect them to
	#the logged_in. If the username does not match the password it the code will redirect them to
	#a screen where they are told that they have entered the wrong input
	if (request.form['submit'] == "login"):
	    os.system("wget " + url)
	    i = 0
	    index = 0
	    for word in url:
	        if(word == '/'):
	            index = i
	        i = i + 1
	    img = url[index+1:]
	    print ("IMG")
	    os.system("python label_image.py " + img)
	    os.system("mv " + img + " static/")
	    return redirect(url_for('results'))
	    
@app.route('/results')
def results():
    return render_template("results.html")

    
    
if __name__ == '__main__':
    app.run(
        debug=True,
        port = int(os.getenv('PORT', 8080)),
        host = os.getenv('IP', '0.0.0.0')
    )