import datetime as dt


def year():
    year = dt.datetime.now().year
    return {
        "year": year
    }