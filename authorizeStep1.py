import pyetrade

consumer_key = "4c9f704cbb2a760658a9fa536f460a03"
consumer_secret = "cf67e63745b2c99cf396e1d271b4e250fb833b2e832e2e59b16940cf3fbbd1c9"

oauth = pyetrade.ETradeOAuth(consumer_key, consumer_secret)
print(oauth.get_request_token())  # Use the printed URL

verifier_code = input("Enter verification code: ")
tokens = oauth.get_access_token(verifier_code)
print(tokens)