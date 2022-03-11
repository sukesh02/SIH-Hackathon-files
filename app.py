from flask import Flask, url_for, render_template, request
import os

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = ".\storage"

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        sex = request.form.get("sex")
        img = request.files["file"]
        os.mkdir(f"storage/{name}")
        img.save(os.path.join(app.config['UPLOAD_FOLDER'], f"\{name}\photo.jpg"))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)