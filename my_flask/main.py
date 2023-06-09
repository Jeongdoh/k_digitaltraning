from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('root.html')

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        num1 = int(num1)
        num2 = int(num2)
        return render_template('result.html', 
                        num1=num1,
                        num2=num2)
    return render_template('calculator.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        num1 = int(num1)
        num2 = int(num2)
        return render_template('result.html', 
                               num1=num1,
                               num2=num2)

if __name__ == '__main__':
    app.run(debug=True)