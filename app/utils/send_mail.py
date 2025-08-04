# utils/email.py
import smtplib
from email.message import EmailMessage

def send_feedback_email(user_email, message):
    EMAIL_ADDRESS = "your_email@gmail.com"
    EMAIL_PASSWORD = "your_password"

    msg = EmailMessage()
    msg['Subject'] = 'New Feedback Received'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = "admin_email@example.com"
    msg.set_content(f"From: {user_email}\n\nMessage:\n{message}")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
