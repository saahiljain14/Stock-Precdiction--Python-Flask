from flask import Flask, request, redirect, render_template, url_for
import execution
import kNeighbours
app = Flask(__name__)



@app.route('/index',methods=['POST','GET'])
def c_details():
    message = ""
    error = ""
    if request.method == 'POST':
        pe=float(request.form['pe'])
        eps=float(request.form['eps'])
        de=float(request.form['de'])
        cr=float(request.form['cr'])
        if request.form['choice'] == 'Decision Tree':
        #button=request.form['decision']
            message =  execution.getResult([pe,eps,de,cr])
        else:
            message = kNeighbours.kNeighbour([pe,eps,de,cr])
    return render_template("index.html",  message=message)





if __name__ == '__main__':

    app.debug = True
    app.run()
