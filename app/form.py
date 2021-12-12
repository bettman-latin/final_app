from flask import Flask, render_template, request, redirect, url_for, make_response
from flask import redirect, url_for # needed for dynamic redirect
from flask import request # needed to respond to post
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('form.html')


@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      if request.form.get("Teach") == None:
         which_page = render_template("result_student.html",result=request.form)
      else:
         which_page = render_template("result_teacher.html",result=request.form)
      resp = make_response(which_page)
      resp.set_cookie('my_name', request.form.get('Name'))
      resp.set_cookie('my_email', request.form.get('Email'))
      return resp
if __name__ == '__main__':
   app.run(debug = True)