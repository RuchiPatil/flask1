import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='theverycleverbell@gmail.com',
    to_emails='ruchipatil@outlook.com, viktor.vcz88@gmail.com',
    subject='tine gene louise ',
    html_content=f'<strong>oh boo</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
