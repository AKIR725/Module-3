def send_email(message, recipient, sender = "university.help@gmail.com"):
    for c in recipient and sender:
        if recipient and sender in ("@" or ".com" or ".ru" or ".net"):
            print("Невозможно отправить письмо с адреса <sender> на адрес <recipient>")
    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")

send_email("vdggjggngngn", "university.help@gmail.com")
