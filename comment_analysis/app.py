from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', star=0)


@app.route('/review', methods=['POST', 'GET'])
def review():
    if request.method == 'POST':
        result = request.form
        print(result)
        res = result.get('desc')
        print(res)
        return render_template('index.html', star=res)


if __name__ == '__main__':
    app.run(debug=True)
