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

    # full_content = TARIELI.get_full_content()
    # random_words = TARIELI.get_random_words(count=1000)
    random_paragraphs = TARIELI.get_random_paragraphs(count=10)

    print(random_paragraphs)


if __name__ == '__main__':
    main()
