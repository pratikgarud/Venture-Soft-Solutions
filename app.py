from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/business.html')
def business():
    return render_template('business.html')

@app.route('/staff.html')
def staff():
    return render_template('staff.html')

@app.route('/hrsolution.html')
def hrsolution():
    return render_template('hrsolution.html')

@app.route('/consulting.html')
def consulting():
    return render_template('consulting.html')

@app.route('/applicationsupport.html')
def applicationsupport():
    return render_template('applicationsupport.html')

@app.route('/applicationservice.html')
def applicationservice():
    return render_template('applicationservice.html')

@app.route('/project.html')
def project():
    return render_template('project.html')


if __name__=='__main__':
    app.run(debug=True)