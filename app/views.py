from flask import Flask, render_template, request, redirect

from app import app
from app.models import db, Patient, Hospital

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        hospital_id = request.form['hospital_id']
        new_patient = Patient(name=name, hospital_id=hospital_id)

        try:
            db.session.add(new_patient)
            db.session.commit()
            return redirect('/')
        except:
            return "There was a problem adding new stuff."

    else:
        patients = Patient.query.order_by(Patient.created_at.desc()).all()
        hospitals = Hospital.query.order_by(Hospital.id).all()
        return render_template('index.html', patients=patients, hospitals=hospitals)

@app.route('/delete/<int:id>')
def delete(id):
    patient = Patient.query.get_or_404(id)

    try:
        db.session.delete(patient)
        db.session.commit()
        return redirect('/')
    except:
        return "There was a problem deleting data."

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    patient = Patient.query.get_or_404(id)

    if request.method == 'POST':
        patient.name = request.form['name']
        patient.hospital_id = request.form['hospital_id']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return "There was a problem updating data."

    else:
        title = "Update Data"
        hospitals = Hospital.query.order_by(Hospital.id).all()
        return render_template('update.html', title=title, patient=patient, hospitals=hospitals)