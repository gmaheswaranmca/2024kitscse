from flask import Flask, render_template, request

app = Flask(__name__)

# code 
@app.route("/",methods=["GET","POST"])
def calc():
    if request.method == "POST":
        num = int(request.form["num"])
        res = num ** 2
    else:
        num = 0
        res = 0
    return render_template('calc.html',
            num=num,
            res=res)

app.run(debug=True)