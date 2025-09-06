import pickle
import numpy as np

# Load saved model
with open("model.pkl", "rb") as f:
    clf = pickle.load(f)

# Take inputs (cast them properly)
cgpa = float(input("Enter your CGPA: "))
internships = int(input("How many internships have you done: "))
projects = int(input("Projects: "))
workshops = int(input("Workshops/Certifications: "))
aptitude = int(input("Aptitude Test Score: "))
softskills = float(input("Soft Skills Rating: "))
extra = int(input("Extracurricular (0=No, 1=Yes): "))
training = int(input("Placement training (0=No, 1=Yes): "))
ssc = int(input("SSC Marks: "))
hsc = int(input("HSC Marks: "))

# Put in the same order as training features
X_new = np.array([[cgpa, internships, projects, workshops, aptitude,
                   softskills, extra, training, ssc, hsc]])

# Predict
y_pred = clf.predict(X_new)
print("Prediction:", "Placed" if y_pred[0] == 1 else "Not Placed")
