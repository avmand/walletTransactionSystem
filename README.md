

What Is This?
-------------

This is a wallet transaction system using Python/Flask. 


How To Use This
---------------

1. Run `pip install -r requirements.txt` to install dependencies
2. Run `python wallet.py`
3. Navigate to http://127.0.0.1:5000/ in your browser to use the transaction system


What can be done?
---------------

1. Create a New Wallet
2. Credit money to a certain wallet
3. Debit money from a wallet
4. View the current balance
5. (Admin only) See all of the existing wallets
6. (Admin only) Delete all of the existing wallets

The features added as 'Admin only' were just to make the process of resetting and viewing a bit easier for us.


Assumptions
---------------

The higher level applications calling these APIs would simultaneously call the debit function on the phone number/user trying to credit that money to the chosen account.
