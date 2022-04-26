import datetime as dt


class Car:
    def __init__(self, license_plate, day_to_consult, time):
        self.license_plate = license_plate
        self.day = day_to_consult
        self.time = time

    def has_mobility_restriction(self):
        # Parse the input time to the format 'H:M'
        time_format = dt.datetime.strptime(
            "{0}".format(self.time), "%H:%M"
        ).time()
        # Pico y Placa during the morning
        if (
            time_format >= dt.time(7, 0) and time_format <= dt.time(9, 30)
        ) or (
            time_format >= dt.time(16, 0) and time_format <= dt.time(19, 30)
        ):
            return self.day_license_match()
        else:
            return False

    def day_license_match(self):
        # Get the last digit of the plate
        last_digit = int(self.license_plate.strip()[-1])
        match = {
            "Monday": [1, 2],
            "Tuesday": [3, 4],
            "Wednesday": [5, 6],
            "Thursday": [7, 8],
            "Friday": [9, 0],
            "Saturday": [-1],
            "Sunday": [-1],
        }
        return last_digit in match.get(self.day)
