from car import Car as C
import schedule


def main():
    print(
        """Welcome to the Pico y Placa Predictor for the city of Quito!\n
Check if your car may or may not be on the road and
take the necessary measures.
    """
    )
    plate = input("Enter the alphanumeric characters of the license plate: ")
    date = input("Enter the date in format dd/mm/yyyy: ")
    time = input("Enter the time in 24 hours format hh:mm: ")
    # Invocation of the 'day' method to return the string day of the date
    day_to_consult = schedule.finder(date)
    car_in_sight = C(plate, day_to_consult, time)
    print(f"On {day_to_consult} at {time}, your car CAN ", end="")
    if car_in_sight.has_mobility_restriction():
        print("NOT ", end="")
    print("BE on the streets of Quito.")


if __name__ == "__main__":
    main()
