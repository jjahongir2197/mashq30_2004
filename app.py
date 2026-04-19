@app.route("/color27", methods=["GET", "POST"])
def color27():

    if request.method == "POST":

        color = request.form.get("color")
        number = request.form.get("number")

        return render_template(
            "result27.html",
            color=color,
            number=number
        )

    return render_template("index27.html")
