from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def welcome():
    return render_template('form.html')


@app.route('/result', methods=['POST'])
def result():
    var_1 = request.form.get("var_1", type=int)
    result = var_1 + 2
    entry = result
    return render_template('result.html', entry=entry)

if __name__ == '__main__':
    app.run(debug=True)
