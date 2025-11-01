def log(msg):
    with open("logs/activity_log.txt", "a") as f:
        f.write(msg + "\n")

