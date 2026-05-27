from flask import Flask, render_template

app = Flask(__name__, template_folder="./")

@app.route("/")
def home():
    return render_template("Propuesta01.html")

# Second HTML
@app.route("/prop2")
def gpt():
    return render_template("Propuesta01gpt.html")

# Third HTML
@app.route("/prop3")
def claudio():
    return render_template("prop1claudio.html")


# WSGI entrypoint
application = app

if __name__ == "__main__":
    app.run(debug=True)