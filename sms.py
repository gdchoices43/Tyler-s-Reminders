import time
import schedule
from twilio.rest import Client
from twilio_creds import cellphone, twilio_account, twilio_token, twilio_number


def mon_dose():
    account = twilio_account
    token = twilio_token
    client = Client(account, token)
    text = "Time to take Monday's dose"
    client.messages.create(to=cellphone, from_=twilio_number, body=text)


def tue_dose():
    account = twilio_account
    token = twilio_token
    client = Client(account, token)
    text = "Time to take Tuesday's dose"
    client.messages.create(to=cellphone, from_=twilio_number, body=text)


def wed_dose():
    account = twilio_account
    token = twilio_token
    client = Client(account, token)
    text = "Time to take Wednesday's dose"
    client.messages.create(to=cellphone, from_=twilio_number, body=text)


def thur_dose():
    account = twilio_account
    token = twilio_token
    client = Client(account, token)
    text = "Time to take Thursday's dose"
    client.messages.create(to=cellphone, from_=twilio_number, body=text)


def fri_dose():
    account = twilio_account
    token = twilio_token
    client = Client(account, token)
    text = "Time to take Friday's dose"
    client.messages.create(to=cellphone, from_=twilio_number, body=text)


def sat_dose():
    account = twilio_account
    token = twilio_token
    client = Client(account, token)
    text = "Time to take Saturday's dose"
    client.messages.create(to=cellphone, from_=twilio_number, body=text)


def sun_dose():
    account = twilio_account
    token = twilio_token
    client = Client(account, token)
    text = "Time to take Sunday's dose"
    client.messages.create(to=cellphone, from_=twilio_number, body=text)


schedule.every().monday.at("09:20").do(mon_dose)
schedule.every().tuesday.at("09:20").do(tue_dose)
schedule.every().wednesday.at("09:20").do(wed_dose)
schedule.every().thursday.at("09:20").do(thur_dose)
schedule.every().friday.at("09:20").do(fri_dose)
schedule.every().saturday.at("09:20").do(sat_dose)
schedule.every().sunday.at("09:20").do(sun_dose)

while True:
    schedule.run_pending()
    time.sleep(2)
