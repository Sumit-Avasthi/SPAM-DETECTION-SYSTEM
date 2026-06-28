import pandas as pd
from flask import Flask,render_template,request
import pickle

app = Flask(__name__)


@app.route("/")
def HomePage():
    return render_template('Home.html')


sms_model = pickle.load(open('model/sms_model.pkl','rb'))
sms_tranform = pickle.load(open('model/sms_vectorizer.pkl','rb'))


@app.route("/sms",methods=["GET","POST"])
def DetectSMS():
    if request.method == "POST":
        raw_data = request.form['message']
        data = sms_tranform.transform([raw_data])
        result = sms_model.predict(data)[0]
        p = max(sms_model.predict_proba(data)[0])*100
        p = round(p,2)
        return render_template('sms.html',prediction=result,confidence=p)
    else :
        return render_template('sms.html')



@app.route("/email")
def DetectEmail():
    return render_template('email.html')


if '__main__' == __name__:
    app.run(host='0.0.0.0',debug=True)