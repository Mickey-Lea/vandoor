from flask import render_template
from app import app
from app.forms import QuestionsForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')
@app.route('/questions')
def questions():
	form = QuestionsForm()
	""" questions = [
		{
			'title': 'age',
			'body': 'What is your age?'
		},
		{
			'title': 'gender',
			'body': 'What is your gender?'
		}
	]
	"""
	return render_template('questions.html', title='Questions', form=form, questions=questions)