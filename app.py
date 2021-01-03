from flask import Flask
import pyetrade
# Importing the pyetrade module
import pyetrade
import pandas as pd
import json

# Obtained secrets from Etrade for Sandbox or Live
consumer_key = "4c9f704cbb2a760658a9fa536f460a03"
consumer_secret = "cf67e63745b2c99cf396e1d271b4e250fb833b2e832e2e59b16940cf3fbbd1c9"
# L6EY2
tokens = {'oauth_token': 'GO+MxXmHBdpopT3ISH7O4h/VvDq80EGp1Wcpm2/qtxQ=', 'oauth_token_secret': 'DQn4M/f102UhTA+3dioH6Oslmf1vE2SmjA0pVqIfjuc='}
accounts = pyetrade.ETradeAccounts(
    consumer_key,
    consumer_secret,
    tokens['oauth_token'],
    tokens['oauth_token_secret'],
    dev=True
)

# lists all the accounts for
accountsInfo = accounts.list_accounts(resp_format='json')
print(accountsInfo)
accountIDKey = accountsInfo['AccountListResponse']['Accounts']['Account'][0]['accountIdKey']
print(accounts.get_account_portfolio(accountIDKey, resp_format='json'))

app = Flask(__name__)
df = pd.DataFrame(accounts.get_account_portfolio(accountIDKey, resp_format='json')["PortfolioResponse"])
df = df.iloc[0].iloc[0]
df = df['Position']

#df = pd.DataFrame(df)
print(type(df))


@app.route('/')
def trades():
    return json.dumps(df)


if __name__ == '__main__':
    app.run()
