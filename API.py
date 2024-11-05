from flask import request,Flask, render_template
import pickle

app=Flask(__name__,template_folder='C:\Users\nada safan\Desktop\New folder')



# "http://127.0.0.1:9090/"
@app.route("/",methods=["GET"])
def first_function():
    return render_template("prediction.html")

# "http://127.0.0.1:9090/getlabel"
@app.route("/get_label",methods=["GET"])
def get_label():
    age=request.args.get("age")
    sex=request.args.get("sex")
    cp=request.args.get("cp")
    trestbps=request.args.get("trestbps")
    chol=request.args.get("chol")
    fbs=request.args.get("fbs")
    restecg=request.args.get("restecg")
    thalach=request.args.get("thalach")
    exang=request.args.get("exang")
    oldpeak=request.args.get("oldpeak")
    slope=request.args.get("slope")
    ca=request.args.get("ca")
    thal=request.args.get("thal") 
    model=pickle.load(open('C:\Users\nada safan\Desktop\New folder\finalized_model.sav', 'rb'))
    result=model.predict([[age,sex,cp,trestbps,chol,
                           fbs,restecg,thalach,exang,
                           oldpeak,slope,ca,thal]])[0]
    if result==1:
        result="Yes"
    else:
        result="No"
    return result

if __name__ == '__main__':
    app.run(host="127.0.0.1",port=9090)