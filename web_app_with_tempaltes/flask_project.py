from flask import Flask, render_template, request

app = Flask(__name__)


class Currency:
    def __init__(self, code, name, flag):
        self.code = code
        self.name = name
        self.flag = flag

    def __repr__(self):
        return f'<Currency {self.code}>'


class CantorOffer:
    def __init__(self):
        self.currencies = []

    def load_offer(self):
        """
        ładuje dane do systemu
        :return:
        """
        self.currencies.append(Currency('USD', "Dollar", 'currencies/dollar.png'))
        self.currencies.append(Currency('EUR', "Euro", 'currencies/euro.jpg'))
        self.currencies.append(Currency('HUF', "Forint", 'currencies/huf.jpg'))
        self.currencies.append(Currency('PLN', "Zloty", 'currencies/zloty.jpg'))

    def get_by_code(self, code):
        for currency in self.currencies:
            if currency.code == code:
                return currency  # zwraca obiekt typu Currency zgodny kodem
        return Currency('unknown', 'unknown', 'kantor.png')


@app.route("/")
def index():
    return 'This is index'


@app.route("/exchange", methods=['GET', 'POST'])
def exchange():
    offer = CantorOffer()  # tworzymy pustą listę na obiekty typu Currency
    offer.load_offer()  # Wypełniamy listę obiektami Currency

    if request.method == 'GET':
        return render_template('exchange.html', offer=offer)
    else:
        currency = "EUR"
        if 'currency' in request.form:
            currency = request.form['currency']

        amount = "EUR"
        if 'amount' in request.form:
            amount = request.form['amount']

        return render_template('exchange_results.html', currency=currency, amount=amount,
                               currency_info=offer.get_by_code(currency))


if __name__ == '__main__':
    app.run(debug=True)
