# # Download the helper library from https://www.twilio.com/docs/python/install
# import os
# from twilio.rest import Client
#
#
# # Find your Account SID and Auth Token at twilio.com/console
# # and set the environment variables. See http://twil.io/secure
# account_sid = 'AC067520e526a8d16285bf9583c449d9c2'
# auth_token = 'cc9db22c7e0bd7ada943c02381d6ad67'
# client = Client(account_sid, auth_token)
#
# message = client.messages.create(
#          body='This is the ship that made the Kessel Run in fourteen parsecs?',
#          from_='+19498283224',
#          to='+256773603206'
#      )
#
# print(message.sid)
