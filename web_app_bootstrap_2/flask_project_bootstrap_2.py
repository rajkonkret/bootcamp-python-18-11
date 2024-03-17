from datetime import date

import binascii
import hashlib
import random
import string

from flask import Flask, render_template, request, flash, g, url_for, redirect, session
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


class UserPass:
    def __init__(self, user='', password=''):
        self.user = user
        self.password = password

    def hash_password(self):
        # generujemy losowy ciag bajtów metoda urandom, zapisujemy do zmiennej ( w osobnym pliku)
        os_urandom_static = b'\xb3Z\xfa\xae\xdc\xbe\xdb\xc8\xd5\xf5\\\x0e1I\xa33\xeb\xdb\xf9\x99\xdd\x0b\xc1\xb8\xd4R\xb2\xb5\xe0\xa9\xa19\xbc\x90\x1e\x80\xff\xb6.l/\xfbr\x99\xaf\xecv\xc1\xa9X\xf9\xcc\t7\x12\x11y\x9fp\xdc'
        # generujemy z ciagu znaków salt (sól) czyli dodatkowy element hashowania
        salt = hashlib.sha256(os_urandom_static).hexdigest().encode('ascii')
        # uzywamy algorytmu pbkdf2 do zaszyfrowania hasła siła sha512
        pwdhash = hashlib.pbkdf2_hmac('sha512', self.password.encode('utf-8'), salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)  # zamiana na binascii
        return (salt + pwdhash).decode('ascii')  # budowanie całego hasła i odesłanie w postaci znków ascii

    def verify_password(self, stored_password, provided_password):
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), salt.encode('utf-8'),
                                      100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password

    def get_random_user_password(self):
        random_user = ''.join(random.choice(string.ascii_lowercase) for i in range(3))
        self.user = random_user

        password_characters = string.ascii_letters
        # ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
        # ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # ascii_letters = ascii_lowercase + ascii_uppercase
        random_password = ''.join(random.choice(password_characters) for i in range(3))
        self.password = random_password

    def login_user(self):
        db = get_db()
        sql_statement = 'SELECT id, name, email, password, is_active, is_admin FROM users WHERE name=?'
        cur = db.execute(sql_statement, [self.user])
        user_record = cur.fetchone()

        if user_record != None and self.verify_password(user_record['password'], self.password):
            return user_record
        else:
            self.user = None
            self.password = None
            return None


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html', active_menu='login')
    else:  # tak naprawdę dla POST
        user_name = '' if "user_name" not in request.form else request.form['user_name']
        user_pass = '' if "user_pass" not in request.form else request.form['user_pass']

    login = UserPass(user_name, user_pass)
    login_record = login.login_user()

    if login_record != None:
        session['user'] = user_name
        flash(f"Login succesfull, welcome {user_name}")
        return redirect(url_for('index'))
    else:
        flash("Login failed, try again")
        return render_template('login.html', active_menu='login')


@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user', None)
        flash("You are logged out")
        return redirect(url_for('login'))
    else:
        flash('You are already logged out')
        return redirect(url_for('index'))


@app.route('/init_app')
def init_app():
    db = get_db()
    sql_statement = 'SELECT COUNT(*) AS cnt FROM users WHERE is_active AND is_admin;'
    cur = db.execute(sql_statement)
    active_admins = cur.fetchone()

    if active_admins != None and active_admins['cnt'] > 0:
        flash('Application is already set-up. Nothing to do')
        return redirect(url_for('index'))

    user_pass = UserPass()
    user_pass.get_random_user_password()
    db.execute('''
    INSERT INTO users(name, email, password, is_active, is_admin) VALUES(?,?,?,True,True);
    ''', [user_pass.user, 'none@nowhere.no', user_pass.hash_password()])
    db.commit()
    flash('User {} with password {} has been added'.format(user_pass.user, user_pass.password))
    return redirect(url_for('index'))  # User dvf with password VSF has been added


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
    return render_template('index.html', active_menu='home')


@app.route("/exchange", methods=['GET', 'POST'])
def exchange():
    offer = CantorOffer()  # tworzymy pustą listę na obiekty typu Currency
    offer.load_offer()  # Wypełniamy listę obiektami Currency

    if request.method == 'GET':
        return render_template('exchange.html', active_menu='exchange', offer=offer)
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
                               active_menu='exchange', currency_info=offer.get_by_code(currency))


@app.route('/history')
def history():
    db = get_db()
    sql_command = 'SELECT id, currency, amount, trans_date FROM transactions;'
    cur = db.execute(sql_command)
    transactions = cur.fetchall()

    return render_template('history.html', transactions=transactions, active_menu='history')


@app.route("/delete_transaction/<int:transaction_id>")
def delete_transaction(transaction_id):
    db = get_db()
    sql_statement = 'delete from transactions where id = ?;'
    db.execute(sql_statement, [transaction_id])
    db.commit()

    return redirect(url_for('history'))


@app.route("/edit_transaction/<int:transaction_id>", methods=['GET', 'POST'])
def edit_transaction(transaction_id):
    offer = CantorOffer()  # tworzymy pustą listę na obiekty typu Currency
    offer.load_offer()  # Wypełniamy listę obiektami Currency
    db = get_db()

    if request.method == 'GET':
        sql_statement = 'SELECT id, currency, amount from transactions WHERE id=?;'
        cur = db.execute(sql_statement, [transaction_id])
        transaction = cur.fetchone()  # pobranie jedego elementu

        if transaction == None:
            flash("No such transaction!")
            return redirect(url_for('history'))
        else:
            return render_template('edit_transaction.html', transaction=transaction,
                                   active_menu='history', offer=offer)
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
            sql_command = '''UPDATE transactions SET
            currency=?,
            amount=?,
            user=?,
            trans_date=?
            WHERE id=?;'''
            db.execute(sql_command, [currency, amount, 'admin', date.today(), transaction_id])
            db.commit()
            flash('Transaction was updated')

        return redirect(url_for('history'))


if __name__ == '__main__':
    app.run(debug=True)
