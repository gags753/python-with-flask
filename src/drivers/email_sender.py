import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_address, body):
  from_addr = "kacupg7pk2e663vq@ethereal.email"
  login = "kacupg7pk2e663vq@ethereal.email"
  password = "YGyW4u3sEqzMMhfv3r"

  msg = MIMEMultipart()
  msg["from"] = "viagens_confirmar@email.com"
  msg["to"] = ', '.join(to_address)

  msg["subject"] = "Confirmação de viagem!"
  msg.attach(MIMEText(body, 'plain'))

  server = smtplib.SMTP("smtp.ethereal.email", 587)
  server.starttls()
  server.login(login, password)
  text = msg.as_string()

  for email in to_address:
    server.sendmail(from_addr, email, text)
  server.quit()
