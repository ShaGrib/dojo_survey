from flask import Flask, render_template, redirect, request, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'lalelolelo'
app.permanent_session_lifetime = timedelta(seconds=30)

@app.route('/')
def base_form():
    session.permanent = True
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process_form():
    if request.method == 'POST':
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['favelang'] = request.form['favelang']
        session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def result_form():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)