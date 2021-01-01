# Set up your imports and your flask app.
from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route('/')
def index():
    # This home page should have the form.
    return render_template('07-index.html')


# This page will be the page after the form
@app.route('/report')
def report():
    # Check the user name for the 3 requirements.

    # HINTS:
    # https://stackoverflow.com/questions/22997072/how-to-check-if-lowercase-letters-exist/22997094
    # https://stackoverflow.com/questions/26515422/how-to-check-if-last-character-is-integer-in-raw-input

    # Return the information to the report page html.

    userName = request.args.get('userName')

    if userNameTest(userName):
        return render_template(('07-thank_you.html'), userName=userName)
    else:
        return render_template(('07-error.html'), userName=userName)

#Helper function to test the validity of the user input
def userNameTest(userName):
    userNameFlag = True

    if not any(c.islower() for c in userName):
        userNameFlag = False

    if not any(c.isupper() for c in userName):
        userNameFlag = False

    if not userName[-1].isdigit():
        userNameFlag = False

    return userNameFlag

if __name__ == '__main__':
    app.run(debug=True)
