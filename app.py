from flask import Flask, redirect, url_for, render_template, request
import os
from face_verification import face_verification
from signature_verification import signature_verification
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
        # Changing uploaded image's file name
        img.filename = f"{name}_photo.png"
        sign.filename = f"{name}_sign.png"
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
            "image_src": f"./static/storage/{name}/{img.filename}",
            "sign_src": f"./static/storage/{name}/{sign.filename}"
        }
        # Make a folder inside ./storage with name as name variable
        try:
            os.mkdir(f"./static/storage/{name}")
        except:
            pass
        # Create a json file in ./storage/name to save info from the form
        with open(f"./static/storage/{name}/{name}.json", "w") as f:
            json.dump(data, f)
        # Save image and sign in ./storage/name
        img.save(f"./static/storage/{name}/{img.filename}")
        img.save(f"./static/storage/{name}/{sign.filename}")
        # Verify if the image has a face
        if face_verification(f"./static/storage/{name}/{img.filename}") and signature_verification():
            face_detect = True
            # If face detected and sign detected, create admit card
            return render_template("result.html", name=name, age=age, sex=sex, img_path=data["image_src"], sign_path=data["sign_src"])
        else:
            face_detect = False
            # Else return error page
            return render_template("error.html")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)