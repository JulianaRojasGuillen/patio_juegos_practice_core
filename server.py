from flask import Flask, render_template

app =Flask(__name__)

@app.route('/play', methods=['GET'])
def nivel1():
    return render_template("index.html",number=3,color="lightblue")

@app.route('/play/<int:number>', methods=['GET'])
def nivel2(number):
    return render_template("index.html",number=number,color="lightblue")

@app.route('/play/<int:number>/<color>', methods=['GET'])
def nivel3(number,color):
    return render_template("index.html",number=number,color=color)

if __name__ =="__main__":
    app.run(debug=True)