from flask import Flask

# pip install Flask==3.0.0

app = Flask(__name__)


@app.route("/")  # / głowna strona
def index():
    return 'Hello World!!!!!!'


@app.route('/cantor/<currency>/<int:amount>')
def cantor(currency, amount):
    message = f'<h1>You selected {currency} and amount {amount}</h1>'
    return message


@app.route('/about')
def about():
    a = 10
    b = 1
    return '<h1>We are programers</h1>'.format(a / b)


if __name__ == '__main__':
    app.run(debug=True)  # debug=True - projekt automatycznie zostaje przeładowany po zmianach w kodzie
