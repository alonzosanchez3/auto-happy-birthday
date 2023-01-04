import smtplib

my_email = "alonzosanchez3@gmail.com"



# with smtplib.SMTP('smtp.gmail.com') as connection:
#   connection.starttls()
#   connection.login(user=my_email, password=password)
#   connection.sendmail(from_addr=my_email, to_addrs="brookthornock@gmail.com", msg="Subject:Test\n\nI hate you")

import datetime as dt

# now = dt.datetime.now()
# year = now.year
# if year == 2023:
#   print(True)
# print(now)

# date_of_birth = dt.datetime(year=1995, month=7, day=10)
# print(date_of_birth)
import random

now = dt.datetime.now()
weekday = now.weekday()
print(weekday)
if weekday == 6:
  with open('quotes.txt') as quote_file:
    all_quotes = quote_file.readlines()
    quote = random.choice(all_quotes)
  print(quote)
  with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(my_email, password)
    connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Quote\n\n{quote}")



