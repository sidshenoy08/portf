from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

import csv

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<parameter>')
def render(parameter):
    file = parameter + ".html"
    return render_template(file)

@app.route('/submit_form', methods=['GET', 'POST'])
def submit():
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)
        temp = str(data)
        with open("database.txt", "a") as file:
            file.write(temp+"\n")
        with open("database.csv", "a", newline='') as file:
            email = data["email"]
            subject = data["subject"]
            message = data["message"]
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([email, subject, message])
        return redirect('/acknowledgement')
    else:
        print("Something went wrong")

'''
@app.route('/works')
def works():
    #return render_template('works.html')

#@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/components')
def components():
    return render_template('Components.html')

@app.route('/work')
def work():
    return render_template('work.html')
'''
