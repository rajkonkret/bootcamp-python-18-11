from flask import Flask, request

# pip install Flask==3.0.0

app = Flask(__name__)


@app.route("/")  # / głowna strona
def index():
    print(request.query_string)

    color = 'black'
    if 'color' in request.args:
        color = request.args['color']

    style = 'normal'
    if 'style' in request.args:
        style = request.args['style']

    for p in request.args:
        print(p, request.args[p])

    return f'<h1 style="color: {color};font-style:{style};">Hello World!!!!!!</h1>'


# b'color=red&style=italic'


@app.route('/cantor/<string:currency>/<int:amount>')
def cantor(currency, amount):
    message = f'<h1>You selected {currency} and amount {amount}</h1>'
    return message


@app.route('/exchange')
def exchange():
    body = '''
    <form id="exchange_form" action="/exchange_process" method="POST">
    <label for="currency">Currency</label>
    <input type="text" id="currency" name="currency" value="EUR"><br>
    <label for="amount">Amount</label>
    <input type="text" id="amount" name="amount" value="100"><br>
    <input type="submit" value="Send">
    </form>
    '''
    return body


@app.route("/exchange_process", methods=['POST'])
def exchange_process():
    currency = "EUR"
    if 'currency' in request.form:
        currency = request.form['currency']

    amount = "EUR"
    if 'amount' in request.form:
        amount = request.form['amount']

    body = f"You want to exchange {amount} {currency}"

    return body


@app.route('/about')
def about():
    a = 10
    b = 1
    return '<h1>We are programers</h1>'.format(a / b)


if __name__ == '__main__':
    app.run(debug=True, port=5005)  # debug=True - projekt automatycznie zostaje przeładowany po zmianach w kodzie
