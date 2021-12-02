import re

from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'session_secret_key'

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/form", methods = ['POST'])
def form_input():
    userInput = request.form.get('userInput')
    print(userInput)
    print(re.match(r'<script>|alert|</script>',userInput))
    if re.match(r'<script>|alert|</script>',userInput):
        return render_template("index.html")
    session['userInput'] = userInput
    return redirect(url_for('completed'))

@app.route("/completed")
def completed():
    return render_template("completed.html", userInput=session['userInput'])

if __name__ == '__main__':
    app.run("0.0.0.0", "5000")