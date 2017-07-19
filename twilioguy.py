from twilio.rest import Client

class TwilioGuy():
    
    def __init__(self, account_sid, auth_token, from_number, to_numbers):
        self.client = Client(account_sid, auth_token)
        self.from_number = from_number
        self.to_numbers = to_numbers
        
    def send_message(self, text):
        for number in self.to_numbers:
            #message = self.client.api.account.messages.create(to=number, from_=self.from_number, body=text)
            self.client.api.account.messages.create(to=number, from_=self.from_number, body=text)