
# importing twilio
from twilio.rest import Client
import os
# Your Account Sid and Auth Token from twilio.com / console
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')

auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)

#Change the value of 'from' with the number
#received from Twilio and the value of 'to'
#with the number in which you want to send message.
numbers = ['+16473909082', '+15197744393']
for number in numbers:
    message = client.messages.create(
                                  from_='+19382225448',
                                  body ='pizza',
                                  to = number
                              )

    print(message.sid)
'''
import os
from sendgrid import SendGridAPIClient, helpers
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='theverycleverbell@gmail.com',
    to_emails='ruchipatil@outlook.com', #'viktor.vcz88@gmail.com'),
    subject='tine gene louise ',
    html_content=f'<strong>oh boo</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
except Exception as e:
    print(e.message)
'''
