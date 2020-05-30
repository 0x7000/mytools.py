#!/usr/bin/env python
import statistics


def main():
    veriler = [1, 2, 3, 4, 5]
    print("{}".format(statistics.stdev(veriler)))  # fx-82MS sx ( s-var 3 ) standart sapma
    print("{}".format(statistics.variance(veriler)))  # varyans x² standart sapmanın karesi
    print("Mean: {}".format(statistics.mean(veriler)))  # mean fx-82MS sx ( s-var 1 ) ortalama


if __name__ == "__main__":
    main()

