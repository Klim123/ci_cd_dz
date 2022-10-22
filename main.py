import os.path
import random
import time
import unittest
import matplotlib.pyplot as plt


class ArrayCalculator:
    _array: list

    def __init__(self) -> None:
        self._array = list()

    @property
    def array(self) -> list:
        return self._array

    @array.setter
    def array(self, array: list) -> None:
        self._array = array

    def min(self) -> int:
        if len(self.array) == 0:
            return -1
        mn = self.array[0]
        for i in range(1, len(self.array)):
            if self.array[i] < mn:
                mn = self.array[i]
        return mn

    def max(self) -> int:
        if len(self.array) == 0:
            return -1
        mx = self.array[0]
        for i in range(1, len(self.array)):
            if self.array[i] > mx:
                mx = self.array[i]
        return mx

    def mult(self) -> int:
        array_mult = 1
        for i in self.array:
            array_mult *= i
        return array_mult

    def sum(self) -> int:
        array_sum = 0
        for i in self.array:
            array_sum += i
        return array_sum


class TestCalculator(unittest.TestCase):
    calculator: ArrayCalculator

    def setUp(self):
        self.calculator = ArrayCalculator()
        self.calculator.array = [1, 4, 2, 3]

    def test_min(self):
        self.assertEqual(self.calculator.min(), 1)

    def test_max(self):
        self.assertEqual(self.calculator.max(), 4)

    def test_sum(self):
        self.assertEqual(self.calculator.sum(), 10)

    def test_mult(self):
        self.assertEqual(self.calculator.mult(), 24)


def speed_test():
    size = 10 ** 4
    timelines = []  # y
    x = []
    speed_test_arr = []
    speed_test_path = 'speed.txt'
    if os.path.exists(speed_test_path):
        with open(speed_test_path) as speed_test_file:
            for line in speed_test_file.readlines():
                speed_test_arr.append([int(x) for x in line.split()])
        print(f'Speed dataset was taken from file {speed_test_path}.')
    else:
        for i in range(10):
            tmp = []
            for j in range(i * size):
                tmp.append(random.randint(0, 10 ** 6))
            speed_test_arr.append(tmp)
        print(f'Speed dataset was created with random.')
    for i in range(10):
        new_array = ArrayCalculator()
        new_array.array = speed_test_arr[i]
        start = time.time()
        new_array.sum()
        new_array.mult()
        new_array.min()
        new_array.max()
        finish = time.time()
        delta = finish - start
        timelines.append(delta)
        x.append(i * size)
    for i in range(len(timelines)):
        print(f"The array with size {i * size} spent {timelines[i]} s.")
    plt.plot(x, timelines)
    plt.xlabel("Array Size")
    plt.ylabel("Seconds")
    plt.grid(True)
    plt.show()


def average(mas: list) -> float:
    res = 0
    k = len(mas)
    for i in mas:
        res += i / k
    return round(res)


def average_test():
    size = 100
    sums = []
    mults = []
    mins = []
    maxs = []
    average_test_arr = []
    average_test_path = 'average.txt'
    if os.path.exists(average_test_path):
        with open(average_test_path) as average_test_file:
            for line in average_test_file.readlines():
                average_test_arr.append([int(x) for x in line.split()])
        print(f'Average dataset was taken from file {average_test_path}.')
    else:
        for i in range(size):
            tmp = []
            for j in range(size):
                tmp.append(random.randint(1, size))
            average_test_arr.append(tmp)
        print(f'Average dataset was created with random.')
    for i in range(size):
        new_array = ArrayCalculator()
        new_array.array = average_test_arr[i]
        sums.append(new_array.sum())
        mults.append(new_array.mult())
        mins.append(new_array.min())
        maxs.append(new_array.max())
    print(f"Среди {size} массивов размеров {size} было выявлено:")
    print(f"Средня сумма: {average(sums)}")
    print(f"Среднее произведение: {average(mults)}")
    print(f"Средний минимум: {average(mins)}")
    print(f"Средний максимум: {average(maxs)}")


def info() -> None:
    msg = 'min                             - минимальное число из файла\n'
    msg += 'max                             - максимальное число из файла\n'
    msg += 'mult                            - произведение всех чисел из файла\n'
    msg += 'sum                             - сумма всех чисел из файла\n'
    msg += 'info                            - команды программы\n'
    msg += 'exit                            - выход из программы\n'
    print(msg)


def command(cmd):
    try:
        if cmd.startswith('mult'):
            print(arr.mult())
        elif cmd.startswith('sum'):
            print(arr.sum())
        elif cmd.startswith('min'):
            print(arr.min())
        elif cmd.startswith('max'):
            print(arr.max())
        elif cmd == 'help' or cmd == 'info':
            info()
        elif cmd == 'exit':
            print('Программа завершена.')
            return False
        else:
            print('Неизвестная команда. help - список команд.')
    except Exception as ex:
        print(f'Ошибка: {ex}')
    return True


def main(arg1):
    print('user - пользовательский режим\ntest - тестирование')
    mode = arg1
    print(mode)
    while True:
        if mode == 'user':
            # user part
            arr = ArrayCalculator()
            FILENAME = 'test.txt'
            if os.path.exists(FILENAME):
                with open(FILENAME) as file:
                    arr.array = list(map(int, file.readline().split()))
            info()
            while command(input('Введите команду: ')):
                pass
        elif mode == 'test':
            print("-----------------------------------")
            # average test
            print("Average test")
            average_test()
            print("-----------------------------------")
            # speed test
            print("Speed test")
            speed_test()
            print("-----------------------------------")
            # unit tests part
            print("Unit test")
            unittest.main()
        else:
            print('unknown mode')


if __name__ == '__main__':
    main()
