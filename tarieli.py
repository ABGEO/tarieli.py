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
    content_array = []

    def __init__(self):
        self.content = self.__read_file()
        self.content_array = self.content.split(' ')

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
        word = re.sub('[,.!?:;"-_\n\r\0]', '', word)

        return word.strip()

    @classmethod
    def __get_random_punctuation_mark(cls):
        """
        Get random punctuation mark.
        :return: Random mark.
        """
        marks = ['.', ',', '!', '?', '?!', ':', ';', ' -']
        random_mark = random.choice(marks)

        return random_mark

    def get_full_content(self):
        """
        Get vefkhistkaosani.txt content.
        :return: vefkhistkaosani.txt content.
        """
        return self.content

    def get_random_words(self, count=1):
        """
        Return random words.
        :param count: Count of words for returning.
        :return: Random words.
        """
        return_value = ''
        for _ in range(count):
            random_word = self.__normalize_word(random.choice(self.content_array))

            return_value += random_word + '\n'

        return return_value

    def get_random_paragraphs(self, count=1):
        """
        Generate random paragraphs.
        :param count: Count of paragraphs for returning.
        :return: Random generated paragraph.
        """
        return_value = ''
        for _ in range(count):
            paragraph_length = random.randint(20, 400)
            punctuation_marks_count = random.randint(0, int(paragraph_length / 2.7))
            punctuation_mark_indexes = [
                random.randint(0, paragraph_length-1) for _ in range(punctuation_marks_count)
            ]

            for i in range(paragraph_length):
                return_value += self.get_random_words().strip()

                if i in punctuation_mark_indexes:
                    return_value += self.__get_random_punctuation_mark()

                return_value += ' '

            return_value = return_value[:-2]
            return_value += '.\n\n'

        return return_value
