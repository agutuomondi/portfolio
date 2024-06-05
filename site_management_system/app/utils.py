from flask_mail import Message
from app import mail

def send_email(subject, recipient, body):
    msg = Message(subject, recipients=[recipient])
    msg.body = body
    mail.send(msg)


@bp.route('/send_reminder')
def send_reminder():
    # Logic to determine who needs reminders
    send_email('Reminder Subject', 'recipient@example.com', 'Reminder Body')
    return 'Reminder sent!'
