import random
import re


class Tarieli:

    content = ''

    def __init__(self):
        self.content = self.__read_file()

    def __read_file(self):
        f = open("./data/vefkhistkaosani.txt", "r")
        content = f.read()
        f.close()

        return content

    def __normalize_word(self, word):
        word = re.sub('[,.!?:;"-_]', '', word)

        return word

    def get_full_content(self):
        return self.content

    def get_random_words(self, count=1):
        content_array = self.content.split(' ')

        return_value = ''
        for i in range(count):
            rand = random.randint(0, len(content_array))

            random_word = self.__normalize_word(content_array[rand])

            return_value += random_word + '\n'

        return return_value
