import pandas as pd
from flask import Flask, render_template

'''
Process with Pandas the Auto.csv dataset contained into the GitHub repo of the course then:
 - compute the average number of cylinders into the dataset;
 - compute the maximum number of cylinders into the dataset;
 - compute the minimum number of cylinders into the dataset;
 - present the information about average, maximum, and minimum number of cylinders into a Web page published by a Flask application you implement;
 - The Flask application uses the templating mechanism in order to keep separate the HTML presentation from the Python logics.
'''

app = Flask(__name__)


df = pd.read_csv('https://raw.githubusercontent.com/anuzzolese/genomics-unibo/master/2019-2020/data/Auto.csv')
	
avg = df['cylinders'].mean()
mx = df['cylinders'].max()
mn = df['cylinders'].min()

@app.route('/') 
def index():
	return render_template('index.html', values={'avg': avg, 'max': mx, 'min': mn})

if __name__ == '__main__':
	app.run(debug=True)