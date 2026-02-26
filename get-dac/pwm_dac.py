import RPi.GPIO as GPIO
import time

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose=False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT)

        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)

        self.pwm.start(0)

        if self.verbose:
            print(f"PWM DAC инициализирован на пине {self.gpio_pin} | Частота: {self.pwm_frequency} Гц | Диапазон: 0-{self.dynamic_range} В")

    def deinit(self):
        self.pwm.stop()
        GPIO.cleanup(self.gpio_pin)

        if self.verbose:
            print("\nРабота ШИМ остановлена, ресурсы GPIO освобождены.")

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            if self.verbose:
                print(f"Ошибка: Напряжение выходит за диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)")
            return

        duty_cycle = (voltage / self.dynamic_range) * 100.0

        self.pwm.ChangeDutyCycle(duty_cycle)

        if self.verbose:
            print(f"Установлено: {voltage:.2f} В (Скважность ШИМ: {duty_cycle:.1f}%)")


if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.290, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

            except KeyboardInterrupt:
                break

    finally:
        dac.deinit()
