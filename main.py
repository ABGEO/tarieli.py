"""
Module tarieli.py
"""

from tarieli import Tarieli

TARIELI = Tarieli()


def main():
    """
    Application main function.
    :return: void
    """

    random_words = TARIELI.get_random_words(count=1000)

    print(random_words)


if __name__ == '__main__':
    main()
