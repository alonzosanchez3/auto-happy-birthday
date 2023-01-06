import smtplib
import random
import datetime as dt
import pandas

MY_EMAIL = 'alonzosanchez3@gmail.com'
FILES_LIST = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']

def send_email(name, email):
  random_file = random.choice(FILES_LIST)
  random_file = 'letter_templates/' + random_file
  with open(random_file, 'r') as message:
    text = message.read()
    text = text.replace('[NAME]', name)
    print(text)


  with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=email, msg=f"Subject:Happy Birthday!\n\n{text}")

data = pandas.read_csv('./birthday.csv')
data_list = data.to_dict(orient='records')
print(data_list)
now = dt.datetime.now()
day = now.day
month = now.month
for record in data_list:
  if record['month'] == month and record['day'] == day:
    send_email(record['name'], record['email'])


