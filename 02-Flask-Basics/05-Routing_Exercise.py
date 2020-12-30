from flask import Flask
app = Flask(__name__)

@app.route('/') # Fill this in!
def index():
    # Welcome Page
    # Create a generic welcome page.
    return "<h1>Welcome!!</h1>"

@app.route('/puppy/<name>') # Fill this in!
def puppylatin(name):
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!

    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"
    return "<h1>Hello, {}</h1>".format(name)

if __name__ == '__main__':
    app.run()
