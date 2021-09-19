from py5paisa import FivePaisaClient

cred={
    "APP_NAME":"TradeX",
    "APP_SOURCE":"YOUR APP_SOURCE",
    "USER_ID":"YOUR USER_ID",
    "PASSWORD":"YOUR PASSWORD",
    "USER_KEY":"YOUR USERKEY",
    "ENCRYPTION_KEY":"YOUR ENCRYPTION_KEY"
    }

client = FivePaisaClient(email="random_email@xyz.com", passwd="password", dob="YYYYMMDD",cred=cred)
client.login()