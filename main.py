# Напишите класс WordsFinder, объекты которого создаются следующим образом:
# WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
# Объект этого класса должен принимать при создании неограниченного количество названий файлов и записывать их в атрибут file_names в виде списка или кортежа.
#
# Также объект класса WordsFinder должен обладать следующими методами:
# get_all_words - подготовительный метод, который возвращает словарь следующего вида:
# {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
# Где:
# 'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
# ['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.
# Алгоритм получения словаря такого вида в методе get_all_words:
# Создайте пустой словарь all_words.
# Переберите названия файлов и открывайте каждый из них, используя оператор with.
# Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
# Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке. (тире обособлено пробелами, это не дефис в слове).
# Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
# В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.
#
# find(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение - позиция первого такого слова в списке слов этого файла.
# count(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение - количество слова word в списке слов этого файла.
# В методах find и count пользуйтесь ранее написанным методом get_all_words для получения названия файла и списка его слов.
# Для удобного перебора одновременно ключа(названия) и значения(списка слов) можно воспользоваться методом словаря - item().
#
# for name, words in get_all_words().items():
#   # Логика методов find или count
import re
from collections import Counter


class WordFinder:

    def __init__(self, file_names: list[str]):

        self.__file_names: list[str] = file_names
        self.__all_words: dict = {}

    def get_all_words(self) -> dict:

        for fileName in self.__file_names:

            with open(file=fileName, mode='r', encoding='UTF-8') as file:

                self.__all_words[fileName] = re.findall(r'\w+', file.read().lower())

        return self.__all_words

    def find(self, word: str) -> dict:

        findResult: dict = {}

        for key, item in self.__all_words.items():

            pos: int = 0
            for text in self.__all_words[key]:

                if word.lower() == text.lower():
                    findResult[f'Слово найдено в ' + key] = f'Позиция слова: {pos}'

                pos += 1

        return findResult

    def count(self, word: str):

        findResult: dict = {}

        for key, item in self.__all_words.items():

            findResult[f'Слово найдено в ' + key] = f'Слово повторяется: {self.__all_words[key].count(word.lower())} раз'

        return findResult


wf = WordFinder(['example1.txt', 'example2.txt'])

print(wf.get_all_words())

print(wf.count('привет'))