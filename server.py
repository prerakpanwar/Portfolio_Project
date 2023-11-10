from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')

# dynamically calling all pages


@app.route("/<string:pagename>")
def html_page(pagename):
    return render_template(pagename)

# function to write data to database.txt file


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

# function to write data to database.csv file


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
        except:
            return 'Did not get saved to the database'
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong! Please try again!'

# we can use 11-13 instead of 16-28.
# @app.route("/works.html")
# def my_works():
#     return render_template('works.html')


# @app.route("/about.html")
# def my_about():
#     return render_template('about.html')


# @app.route("/contact.html")
# def my_contact():
#     return render_template('contact.html')
