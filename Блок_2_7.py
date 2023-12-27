
month = input("Введите название месяца: ")
day = int(input("Введите номер дня: "))

if (month == "январь" and day >= 1) or (month == "февраль") or (month == "март" and day <= 19):
    season = "зима"
elif (month == "март" and day >= 20) or (month == "апрель") or (month == "май") or (month == "июнь" and day <= 20):
    season = "весна"
elif (month == "июнь" and day >= 21) or (month == "июль") or (month == "август") or (month == "сентябрь" and day <= 21):
    season = "лето"
elif (month == "сентябрь" and day >= 22) or (month == "октябрь") or (month == "ноябрь") or (month == "декабрь" and day <= 20):
    season = "осень"
else:
    season = "зима"

print(f"Название времени года для выбранной даты: {season}")