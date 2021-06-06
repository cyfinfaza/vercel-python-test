from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html', time=str(datetime.datetime.now()))

@app.route('/mult2')
def addone():
	try:
		num = request.args.get('num', type=int)
		return render_template('result.html', result=num*2)
	except:
		return render_template('error.html', error="Failed to get the number.")