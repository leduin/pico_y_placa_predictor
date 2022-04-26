import datetime as dt


def finder(date):
    try:
        # Parse the string datatype to a date object
        date_format = dt.datetime.strptime(date, "%d/%m/%Y")
        # Parse the date object to a string in the day
        string_date = date_format.strftime("%A")
    except ValueError:
        print("Please, enter the correct date format!")

    return string_date
