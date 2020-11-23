from flask import Flask

app = Flask(__name__)

@app.route('/') 
def index():
	return """<html><head><title>SA 2019/2010</title></head><body><h1>Software Applications 2019/2020
		</h1><p>This is the web page
		of the course</p><p>The slides are available <a href="slides">here</a>.</p></body></html>
		"""

@app.route('/slides') 
def about():
	return """<html><head><title>SA 2019/2010</title></head><body><h1>Slides</h1><ul>
		<li>Introduction</li><li>What is Software?</li></ul><p>Back to <a href="/">home</a>.</p></body>
	</html>
	"""
	
if __name__ == '__main__': 
	app.run()