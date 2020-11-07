from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('/temp/home_form.html')

@app.route('/register')
def register():
  return render_template('/temp/register_form.html') 

@app.route('/login')
def login():
    return render_template('/temp/login_form.html')

@app.route('/QandA')
def QandA():
  return render_template("/temp/QandA_form.html")

@app.route('/about')
def about():
  return render_template('/temp/about_form.html')

@app.route('/feedback')
def feedback():
  return render_template('/temp/feedback_form.html')

@app.errorhandler(404)
def page_not_found(E):
  return render_template("page_not_found.html"), 404

if __name__ == '__main__':
  app.run()
  
