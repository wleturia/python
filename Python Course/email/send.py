import smtplib

content = "hello i am from python"
mail= smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('email-login','email-password')
mail.sendmail('email-from','email-to',content)
mail.close()