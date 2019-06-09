"""
Module tarieli.py
"""

import random
import re


class Tarieli:
    """
    Class for generating random text content from Vefkhistkaosani.
    """

    content = ''

    def __init__(self):
        self.content = self.__read_file()

    @classmethod
    def __read_file(cls):
        """
        Read text content from vefkhistkaosani.txt.
        :return: File content
        """
        file_stream = open("./data/vefkhistkaosani.txt", "r")
        content = file_stream.read()
        file_stream.close()

        return content

    @classmethod
    def __normalize_word(cls, word):
        """
        Remove banned symbols from given word.
        :param word: Word for normalizing.
        :return: Normalized word.
        """
        word = re.sub('[,.!?:;"-_]', '', word)

        return word

    def get_full_content(self):
        """
        Get vefkhistkaosani.txt content.
        :return: vefkhistkaosani.txt content.
        """
        return self.content

    def get_random_words(self, count=1):
        """
        Return random words.
        :param count: Count of word for returning.
        :return: Random words.
        """
        content_array = self.content.split(' ')

        return_value = ''
        for _ in range(count):
            rand = random.randint(0, len(content_array))

            random_word = self.__normalize_word(content_array[rand])

            return_value += random_word + '\n'

        return return_value
