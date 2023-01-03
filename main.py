import smtplib

my_email = "alonzosanchez3@gmail.com"


with smtplib.SMTP('smtp.gmail.com') as connection:
  connection.starttls()
  connection.login(user=my_email, password=password)
  connection.sendmail(from_addr=my_email, to_addrs="brookthornock@gmail.com", msg="Subject:Test\n\nI hate you")

