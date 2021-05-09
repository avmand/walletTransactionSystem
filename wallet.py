from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, flash, url_for, redirect, render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///WalletTransactions'
app.config['SECRET_KEY'] = "WalletTransaction"

db = SQLAlchemy(app)

    
class Wallet(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   phoneNumber = db.Column(db.String)
   minimumBalance = db.Column(db.Float)
   currentBalance = db.Column(db.Float)
   transactions = db.relationship('Transaction', backref='wallet', lazy='dynamic')

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    debitOrCredit = db.Column(db.String(20))
    amount = db.Column(db.Float)
    phoneNumber = db.Column(db.String, db.ForeignKey('wallet.id'))
    

@app.route('/')
def home():
   return render_template('home.html' )


@app.route('/home')
def homeagain():
   return render_template('home.html' )


@app.route('/admin')
def adminPage():
   return render_template('admin.html' )


@app.route('/deleteAll')
def deleteAll():
    for per in Wallet.query.all():
        db.session.delete(per)
    for per in Transaction.query.all():
        db.session.delete(per)
    db.session.commit()
    flash ('All of the wallets have been deleted!', 'success')
    return render_template('show.html', Wallets = Wallet.query.all() )

@app.route('/show_all')
def show_all():
   if (Wallet.query.all() == []):
      flash ('There are no wallets to be shown.', 'success')
   return render_template('show.html', Wallets = Wallet.query.all() )


@app.route('/createWallet', methods = ['GET', 'POST'])
def createWallet():
    if request.method == 'POST':
      if not request.form['phoneNumber'] or not request.form['minimumBalance'] or not request.form['startingBalance']:
         flash('Please enter all the fields', 'error')
      elif Wallet.query.filter_by(phoneNumber = request.form['phoneNumber']).first() != None:
         flash ('This phone number already has a wallet.', 'error')
      elif len(request.form['phoneNumber']) !=10 :
         flash ('Not a valid phone number. Please enter a 10 digit phone number.', 'error')
      elif int(request.form['minimumBalance']) <=0:
         flash ('Enter a minimum balance greater than 0. ', 'error')
      elif int(request.form['startingBalance']) <=0:
         flash ('Enter a starting balance greater than 0. ', 'error')
      elif int(request.form['startingBalance']) < int(request.form['minimumBalance']):
         flash ('Please make sure that your starting balance is greater than your minimum limit.', 'error')   
      else:
         walletEntry = Wallet(phoneNumber = request.form['phoneNumber'], minimumBalance =request.form['minimumBalance'],
                              currentBalance =request.form['startingBalance'])
         countOfTransactions = len(Transaction.query.all())
         transactionsEntry = Transaction(id = countOfTransactions, phoneNumber = request.form['phoneNumber'], debitOrCredit ="Credit",
                              amount =request.form['startingBalance'])
         db.session.add(walletEntry)
         db.session.add(transactionsEntry)
         db.session.commit()
         return render_template('yourWallet.html', myWallet = walletEntry, Transactions = Transaction.query.filter_by(phoneNumber = request.form['phoneNumber']).order_by(Transaction.id.desc()).all())
    return render_template('newWallet.html')


@app.route('/creditMoney', methods = ['GET', 'POST'])
def creditMoney():
    if request.method == 'POST':
      if not request.form['phoneNumber'] or not request.form['amount']:
         flash('Please enter all the fields', 'error')
      elif int(request.form['amount']) <=0:
         flash ('Credit an amount greater than 0. ', 'error')
      else:
         updated = Wallet.query.filter_by(phoneNumber = request.form['phoneNumber']).first()
         updated.currentBalance +=int(request.form['amount'])
         countOfTransactions = len(Transaction.query.all())
         transactionsEntry = Transaction(id = countOfTransactions, phoneNumber = request.form['phoneNumber'], debitOrCredit ="Credit",
                              amount =request.form['amount'])
         db.session.add(transactionsEntry)
         db.session.commit()
         return render_template('yourWallet.html', myWallet = updated, Transactions = Transaction.query.filter_by(phoneNumber = request.form['phoneNumber']).order_by(Transaction.id.desc()).all())
    return render_template('creditMoney.html')



@app.route('/debitMoney', methods = ['GET', 'POST'])
def debitMoney():
    if request.method == 'POST':
      if not request.form['phoneNumber'] or not request.form['amount']:
         flash('Please enter all the fields', 'error')
      elif int(request.form['amount']) <=0:
         flash ('Debit an amount greater than 0. ', 'error')
      elif Wallet.query.filter_by(phoneNumber = request.form['phoneNumber']).first().currentBalance - int(request.form['amount']) < Wallet.query.filter_by(phoneNumber = request.form['phoneNumber']).first().minimumBalance:
         flash ('Cannot debit that amount as it will cause the current balance to drop below the minimum balance.', 'error')
      else:
         updated = Wallet.query.filter_by(phoneNumber = request.form['phoneNumber']).first()
         updated.currentBalance -=int(request.form['amount'])
         countOfTransactions = len(Transaction.query.all())
         transactionsEntry = Transaction(id = countOfTransactions, phoneNumber = request.form['phoneNumber'], debitOrCredit ="Debit",
                              amount =request.form['amount'])
         db.session.add(transactionsEntry)
         db.session.commit()
         return render_template('yourWallet.html', myWallet = updated, Transactions = Transaction.query.filter_by(phoneNumber = request.form['phoneNumber']).order_by(Transaction.id.desc()).all())
    return render_template('debitMoney.html')


@app.route('/currentBalance', methods = ['GET', 'POST'])
def currentBalance():
    if request.method == 'POST':
      if not request.form['phoneNumber']:
         flash('Please enter data for all of the fields', 'error')
      elif Wallet.query.filter_by(phoneNumber = request.form['phoneNumber']).first() == None:
         flash ('This phone number doesn\'t have a wallet. ', 'error')
      else:
        theChosenOne = Wallet.query.filter_by(phoneNumber = request.form['phoneNumber']).first()
        return render_template('yourWallet.html', myWallet = theChosenOne, Transactions = Transaction.query.filter_by(phoneNumber = request.form['phoneNumber']).order_by(Transaction.id.desc()).all())
    return render_template('currentBalance.html')


if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)