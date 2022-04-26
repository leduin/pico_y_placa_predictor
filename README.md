# StackBuilders Exercise

## Description

The predictor "Pico y Placa" is a program written in Python language that predicts whether a car will be able to circulate on the streets on a date and time specified by the user through the command-line interface (CLI). To develop this application we consider the past rules of the Pico&Placa.

| **Day**   | **Censored plates**              |
|-----------|----------------------------------|
| Monday    | Plates ending in 1 and 2.        |
| Tuesday   | Plates ending in 3 and 4.        |
| Wednesday | Plates ending in 5 and 6.        |
| Thursday  | Plates ending in 7 and 8.        |
| Friday    | Plates ending in 9 and 0.        |
| Saturday  | Free circulation all day.        |
| Sunday    | Free circulation all day.        |

Traffic limitation hours are from 07:00 to 09:30 and from 16:00 to 19:30, from Monday to Friday, according to the last digit of the license plate.

## Considerations

### Code

* The class `Car` inside `car.py`, has all the logical methods of the program. The class is composed of three attributes: `license plate`, `date` and `time`.

* A specific output is presented depending on the inputs of the `main.py`.

* Also, `schedule.py` has the methods to convert the date input from string datatype to object datatype and then get the day in string datatype.

* `test_car.py` is the validator script. Only run it to verify the program.

### Python

Please, check if you have Python installed on your machine.

```bash
python --version
```

If not, [download](https://www.python.org/downloads/) and install it.

### Technical details

This program was developed on Debian 11 OS with Python 3.9.2 version.

## License

The following program is based on [Daniel Erazo's Pico y Placa Predictor](https://github.com/Danii2020/pico-y-placa-predictor-python) under [MIT License](LICENSE).

## Usage

1. Open your CLI and run `main.py` file from the container directory.

    ```bash
    python main.py
    ```

2. Enter only the alphanumeric characters of the license plate.

3. Enter the date in format `dd/mm/yyyy`.

4. Enter the time in 24 hours format `hh:mm`.

5. The result of the query is displayed on the screen.