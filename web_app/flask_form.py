from flask import Flask, request, url_for, redirect

# pip install Flask==3.0.0

app = Flask(__name__)


@app.route("/")  # / głowna strona
def index():
    # print(request.query_string)
    #
    # color = 'black'
    # if 'color' in request.args:
    #     color = request.args['color']
    #
    # style = 'normal'
    # if 'style' in request.args:
    #     style = request.args['style']
    #
    # for p in request.args:
    #     print(p, request.args[p])

    menu = f'''
    Go <a href="{url_for('exchange')}">here</a> to exchange money</br>
    To exchange 50 SEK go <a href="{url_for('cantor', currency='SEK', amount=50)}">here</a>
'''
    # return f'<h1 style="color: {color};font-style:{style};">Hello World!!!!!!</h1>'
    return f'<h1 >Hello World!!!!!!</h1></br>{menu}'


# b'color=red&style=italic'


@app.route('/cantor/<string:currency>/<int:amount>')
def cantor(currency, amount):
    message = f'<h1>You selected {currency} and amount {amount}</h1>'
    return message


@app.route('/exchange', methods=['GET', 'POST'])
def exchange():
    print(request.method)

    if request.method == 'GET':
        body = f'''
        <form id="exchange_form" action="{url_for('exchange')}" method="POST">
        <label for="currency">Currency</label>
        <input type="text" id="currency" name="currency" value="EUR"><br>
        <label for="amount">Amount</label>
        <input type="text" id="amount" name="amount" value="100"><br>
        <input type="submit" value="Send">
        </form>
        '''
        return body
    else:
        currency = "EUR"
        if 'currency' in request.form:
            currency = request.form['currency']

        amount = "EUR"
        if 'amount' in request.form:
            amount = request.form['amount']

        body = f"You want to exchange {amount} {currency}"

        # return body
        # return redirect(url_for('index'))
        return redirect(url_for('cantor', currency=currency, amount=amount))


#
# @app.route("/exchange_process", methods=['POST'])
# def exchange_process():
#     currency = "EUR"
#     if 'currency' in request.form:
#         currency = request.form['currency']
#
#     amount = "EUR"
#     if 'amount' in request.form:
#         amount = request.form['amount']
#
#     body = f"You want to exchange {amount} {currency}"
#
#     return body


@app.route('/about')
def about():
    a = 10
    b = 1
    return '<h1>We are programers</h1>'.format(a / b)


if __name__ == '__main__':
    app.run(debug=True, port=5005)  # debug=True - projekt automatycznie zostaje przeładowany po zmianach w kodzie
