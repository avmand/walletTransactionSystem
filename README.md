

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


The product
---------------

<p align="center"><img src="https://github.com/avmand/walletTransactionSystem/blob/main/images/home.PNG" width="75%"></p>
<p align="center">The home page. Choose any option to proceed.</p><br>
<p align="center"><img src="https://github.com/avmand/walletTransactionSystem/blob/main/images/createWallet.PNG" width="75%"></p>
<p align="center">If you click on 'Add a Wallet' on the home page, you will be redirected to this page.</p><br>
<p align="center"><img src="https://github.com/avmand/walletTransactionSystem/blob/main/images/Admin.PNG" width="75%"></p>
<p align="center">The admin page. This was made to include two features that are supposed to be accessed by admins only.</p><br>
<p align="center"><img src="https://github.com/avmand/walletTransactionSystem/blob/main/images/seeAll.PNG" width="75%"></p>
<p align="center">If you click on 'See All Wallets' on the admin page, you will be redirected to this page to view all of the current wallets</p><br>
