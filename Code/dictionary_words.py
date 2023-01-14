import random
import argparse

def get_words_list():
    file = open("/usr/share/dict/words", 'r')
    all_words = file.readlines()
    output = []

    file.close()
    
    for word in all_words:
        output.append(word.rstrip("\n"))

    return output

def get_words(num_words):
    words = random.choices(get_words_list(), k=num_words)

    return words

def make_sentence(words):
    output = ''
    for i in range(len(words)):
        if i < len(words) - 1:
            output += words[i].strip("\n") + " "
        else:
            output += words[i].strip("\n") + "."

    return output

def auto_complete(typed_letters):
    words = get_words_list()
    output = []

    for word in words:
        if typed_letters == word[:len(typed_letters)]:
            output.append(word)

    return output 

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # parser.add_argument('num_words', help="enter the number of words to receive", type=int)
    parser.add_argument('letters', type=str, help="enter the start of a word to be autocompleted")

    args = parser.parse_args()
    # num_words = args.num_words
    letters = args.letters

    # words = get_words(num_words)
    # sentence = make_sentence(words)

    # print(sentence)
    completed = auto_complete(letters)
    print(completed)
