from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def turn_page():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.htm")


if __name__=='__main__':
    app.run()