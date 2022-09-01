import smtplib
import os
from email.mime.text  import MIMEText



def send_email(name,surname,surname2,birthday,work1,work2,work3,phone):
        sender = "anketagosniimash@gmail.com"
        #password = "http://A@amov/?nR"
        password = "gbuxjkfqpvhzzghy"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        try:
            server.login(sender, password)
            message = f'Новая анкета\nИмя: - {name}\nФамилия: - {surname}\nОчество: - {surname2}\nДата рождения: - {birthday} \nПоследнее 1 место работы:  {work1}\nПоследнее 2 место работы:  {work2}\nПоследнее 3 место работы:  {work3}\nОбратная связь:  {phone}'
            msg = MIMEText(message)

            msg["Subject"] = "Новая анкета - " + surname
            server.sendmail(sender, sender, msg.as_string())

            # server.sendmail(sender, sender, f"Subject: CLICK ME PLEASE!\n{message}")

            return "The message was sent successfully!"
        except Exception as _ex:
            return f"{_ex}\nCheck your login or password please!"

def main():
        message = input("Type your message: ")
        print(send_email(message=message))

if __name__ == "__main__":
        main()
