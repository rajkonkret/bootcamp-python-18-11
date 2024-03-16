from flask import Flask, render_template, request, flash, g
import sqlite3

# konfiguracja pliku dla bazy danych
app_info = {
    'db_file': 'data/cantor.db'
}

app = Flask(__name__)
# dodajemy secret_key aby komunikacja flash wykonywała się w bezpieczny sposób
app.config['SECRET_KEY'] = 'KluczTrudnyDoZlamania123!!!'


# g - obiekt globalny, przechowuje dane w sesji, konieczny gdy musimy znac parametry uzyskane w danej sesji
def get_db():
    if not hasattr(g, 'sqlite_db'):  # sprawdza czy obiekt g posiada parametr sqlite_db
        conn = sqlite3.connect(app_info['db_file'])
        conn.row_factory = sqlite3.Row  # zwraca w postaci słownika
        g.sqlite_db = conn  # zapisanie połączenia do bazy do obiektu globalnego g (w ramach sesji)
    return g.sqlite_db


# zamykanie bazy danych, kiedy opuszczamy sesje wykona tą metode
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()
        print(error)


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
        self.denied_codes = []

    def load_offer(self):
        """
        ładuje dane do systemu
        :return:
        """
        self.currencies.append(Currency('USD', "Dollar", 'currencies/dollar.png'))
        self.currencies.append(Currency('EUR', "Euro", 'currencies/euro.jpg'))
        self.currencies.append(Currency('HUF', "Forint", 'currencies/huf.jpg'))
        self.currencies.append(Currency('PLN', "Zloty", 'currencies/zloty.jpg'))
        self.currencies.append(Currency('RUB', "Rubel", 'kantor.png'))
        self.denied_codes.append('RUB')

    def get_by_code(self, code):
        for currency in self.currencies:
            if currency.code == code:
                return currency  # zwraca obiekt typu Currency zgodny kodem
        return Currency('unknown', 'unknown', 'kantor.png')


@app.route("/")
def index():
    # return 'This is index'
    return render_template('index.html')


@app.route("/exchange", methods=['GET', 'POST'])
def exchange():
    offer = CantorOffer()  # tworzymy pustą listę na obiekty typu Currency
    offer.load_offer()  # Wypełniamy listę obiektami Currency

    if request.method == 'GET':
        return render_template('exchange.html', offer=offer)
    else:
        flash("Debug: starting exchange in POST mode")
        currency = "EUR"
        if 'currency' in request.form:
            currency = request.form['currency']

        amount = "100"
        if 'amount' in request.form:
            amount = request.form['amount']

        if currency in offer.denied_codes:
            flash('The currency {} cannot be accepted'.format(currency))
        elif offer.get_by_code(currency) == 'unknown':
            flash('The selected currency is unknown and cannot be accepted')
        else:
            db = get_db()
            sql_command = "INSERT INTO transactions(currency, amount, user) values (?, ?, ?);"
            db.execute(sql_command, [currency, amount, 'admin'])
            db.commit()
            flash('Request to exchange {} was accepted'.format(currency))

        return render_template('exchange_results.html', currency=currency, amount=amount,
                               currency_info=offer.get_by_code(currency))


@app.route('/history')
def history():
    db = get_db()
    sql_command = 'SELECT id, currency, amount, trans_date FROM transactions;'
    cur = db.execute(sql_command)
    transactions = cur.fetchall()

    return render_template('history.html', transactions=transactions)

if __name__ == '__main__':
    app.run(debug=True)
