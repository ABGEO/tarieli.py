#!/usr/bin/python
"""
Module tarieli.py
"""
import os

from tarieli import Tarieli

TARIELI = Tarieli()


def print_logo():
    """
    Print application logo
    """
    print('Welcome to')
    print(' _             _      _ _               ')
    print('| |_ __ _ _ __(_) ___| (_)  _ __  _   _ ')
    print('| __/ _` | \'__| |/ _ \\ | | | \'_ \\| | | |')
    print('| || (_| | |  | |  __/ | |_| |_) | |_| |')
    print(' \\__\\__,_|_|  |_|\\___|_|_(_) .__/ \\__, |')
    print('                           |_|    |___/ ')
    print('<Created ByABGEO />')
    print('                                 v1.0.0')
    print('-----------------------------------------')


def get_menu():
    """
    Print menu and select action.
    """
    menu_items = [
        {"გამოსვლა": exit},
        {"მთლიანი კონტენტის ბეჭდვა": print_content},
        {"შემთხვევითი სიტყვების გენერაცია": print_words},
        {"შემთხვევითი პარაგრაფების გენერაცია": print_paragraphs},
    ]

    while True:
        os.system('clear')

        print_logo()

        print('\nაირჩიეთ მოქმედება:\n')
        for item in menu_items:
            print('[' + str(menu_items.index(item)) + '] ' + list(item.keys())[0])

        action = input(">> ")
        try:
            if int(action) < 0:
                raise ValueError

            selected_action = list(menu_items[int(action)].values())[0]

            # Run selected action.
            os.system('clear')
            selected_action()
        except (ValueError, IndexError):
            pass


def print_content():
    """
    Print all content.
    """
    content = TARIELI.get_full_content()

    print(content)

    app_continue()


def print_words():
    """
    Print random words.
    """
    success_input = False
    words_count = 1
    while not success_input:
        words_count = input('მიუთითეთ სიწყვების რაოდენობა: ')

        try:
            words_count = int(words_count)
            success_input = True

            if int(words_count) < 0:
                success_input = False
                print('არასწორი სიტყვების რაოდენობა. სცადეთ ხელახლა!')
        except ValueError:
            success_input = False
            print('სიტყვების რაოდენობა უნდა იყოს რიცხვი!')

    content = TARIELI.get_random_words(words_count)

    print('\n\n' + content)

    app_continue()


def print_paragraphs():
    """
    Print random paragraphs.
    """
    success_input = False
    paragraphs_count = 1
    while not success_input:
        paragraphs_count = input('მიუთითეთ პარაგრაფების რაოდენობა: ')

        try:
            paragraphs_count = int(paragraphs_count)
            success_input = True

            if int(paragraphs_count) < 0:
                success_input = False
                print('არასწორი პარაგრაფების რაოდენობა. სცადეთ ხელახლა!')
        except ValueError:
            success_input = False
            print('პარაგრაფების რაოდენობა უნდა იყოს რიცხვი!')

    content = TARIELI.get_random_paragraphs(paragraphs_count)

    print('\n\n' + content)

    app_continue()


def app_continue():
    """
    Continue or exit from application.
    """
    action = input("\n\nგსურთ კიდევ ცდა? [y/n] ")

    if action not in ['y', 'Y', 'yes', 'Yes']:
        print('\nმომავალ შეხვედრამდე!\n\n')
        exit()


def main():
    """
    Application main function.
    :return: void
    """
    get_menu()


if __name__ == '__main__':
    main()
