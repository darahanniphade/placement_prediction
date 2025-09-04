from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open("model.pkl", "rb") as f:
    clf = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            # Get inputs from form
            cgpa = float(request.form["cgpa"])
            projects = int(request.form["projects"])
            aptitude = int(request.form["aptitude"])
            softskills = float(request.form["softskills"])
            ssc = int(request.form["ssc"])
            hsc = int(request.form["hsc"])

            # Arrange features in the same order as training
            X_new = np.array([[cgpa, projects, aptitude, softskills, ssc, hsc]])

            # Predict
            y_pred = clf.predict(X_new)[0]
            prediction = "🎉 Placed!" if y_pred == 1 else "❌ Not Placed"

        except Exception as e:
            prediction = f"Error: {e}"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
