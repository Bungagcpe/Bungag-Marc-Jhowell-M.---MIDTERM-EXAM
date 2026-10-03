def main():
    class TemperatureConversion:
        def __init__(self, temp=1):
            self._temp = temp

    class CelsiusToFahrenheit(TemperatureConversion):
        def conversion(self):
            return self._temp * 9 / 5 + 32

    class CelsiusToKelvin(TemperatureConversion):
        def conversion(self):
            return self._temp + 273.15

    class FahrenheitToCelsius(TemperatureConversion):
        def conversion(self):
            return (self._temp - 32) * 5 / 9

    class KelvinToCelsius(TemperatureConversion):
        def conversion(self):
            return self._temp - 273.15

    # Celsius to Kelvin and Fahrenheit
    TempInCelsius = float(input("Enter the temperature in Celsius: "))
    convert = CelsiusToKelvin(TempInCelsius)
    print(str(convert.conversion()) + " Kelvin")

    convert = CelsiusToFahrenheit(TempInCelsius)
    print(str(convert.conversion()) + " Fahrenheit")

    # Fahrenheit to Celsius
    TempInFahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    convert = FahrenheitToCelsius(TempInFahrenheit)
    print(str(convert.conversion()) + " Celsius")

    # Kelvin to Celsius
    TempInKelvin = float(input("Enter the temperature in Kelvin: "))
    convert = KelvinToCelsius(TempInKelvin)
    print(str(convert.conversion()) + " Celsius")

main()