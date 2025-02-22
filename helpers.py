def time():
    from datetime import datetime as dt
    now = dt.now()
    return now.strftime("%I:%M %p")
