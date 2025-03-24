from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def register():
    message = ""
    if request.method == "POST":
        username = request.form.get("username")

        if username:
            message = "registration successfull"
        else:
            message = "Req"
    return render_template("register.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)