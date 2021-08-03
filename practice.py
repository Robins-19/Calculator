from flask import Flask, render_template, request
from werkzeug.utils import redirect



app = Flask(__name__)


@app.route('/')
def calcularor():
    return render_template('calculator.html')


@app.route('/',methods=['POST'])
def hello():
    x=request.form['x']
    length = len(x)

    def index():
        i = 0
        while length > i:
            if x[i] == '+':
                break
            elif x[i] == '-':
                break
            elif x[i] == '*':
                break
            elif x[i] == '/':
                break
            i = i + 1
        return i

    SymbolIndex = index()

    def number1():
        n1 = ""
        b = 0
        while SymbolIndex > b:
            n1 = n1 + x[b]
            b = b + 1
        return n1

    num1 = float(number1())

    def number2():
        n2 = ""
        c = SymbolIndex + 1
        while length > c:
            n2 = n2 + x[c]
            c = c + 1
        return n2

    num2 = float(number2())
    s = x[SymbolIndex]

    def result1():
        if s == '+':
            return num1 + num2
        elif s == '-':
            return num1 - num2
        elif s == '*':
            return num1 * num2
        elif s == '/':
            return num1 / num2


    result=result1()
    return render_template('GetValue.html',result=result)


@app.route('/',methods=['GET'])
def hello1():
    x1=request.form['x1']
    return redirect(calcularor.html)



if __name__ == "__main__":
    app.run()