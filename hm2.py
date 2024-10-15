s = int(input("Write seconds: "))

if s < 0 or s > 8640000:
    print("Incorrect number")
else:

    days, rem_seconds = divmod(s, 60 * 60 * 24)
    hours, rem_seconds = divmod(rem_seconds, 60 * 60)
    minutes, seconds = divmod(rem_seconds, 60)

    hours_update = str(hours).zfill(2)
    minutes_update = str(minutes).zfill(2)
    seconds_update = str(seconds).zfill(2)

    if days <= 4:
        print(f"{days} Дня, {hours_update}:{minutes_update}:{seconds_update}")
    else:
        print(f"{days} Дней, {hours_update}:{minutes_update}:{seconds_update}")
