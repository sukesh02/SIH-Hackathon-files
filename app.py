from flask import Flask, url_for, render_template, request
import os
from face_verification import face_verification
import json

app = Flask(__name__)

image_extentions = ('.png', '.jpg', '.jpeg')

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        # Get values from form
        name = request.form["name"]
        age = request.form["age"]
        sex = request.form["sex"]
        img = request.files["img"]
        sign = request.files["sign"]
        # Check if the uploaded image has proper extention
        # if img.filename.lower().endswith(image_extentions) and sign.filename.lower().endswith(image_extentions):
        #     pass
        # else:
        #     print("--- --- --- --- Extension error")
        # Convert form values into dict
        data = {
            "name": name,
            "age": age,
            "sex": sex,
            "image_src": f"./storage/{name}/{img.filename}",
            "sign_src": f"./storage/{name}/{sign.filename}"
        }
        # Make a folder inside ./storage with name as name variable
        try:
            os.mkdir(f"./storage/{name}")
        except:
            pass
        # Create a json file in ./storage/name to save info from the form
        with open(f"./storage/{name}/{name}.json", "w") as f:
            json.dump(data, f)
        # Save image and sign in ./storage/name
        img.save(f"./storage/{name}/{img.filename}")
        img.save(f"./storage/{name}/{sign.filename}")
        # Verify if the image has a face
        if face_verification(f"./storage/{name}/{img.filename}"):
            print("--- --- --- --- Face detected")
        else:
            print("--- --- --- --- No face detected")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)