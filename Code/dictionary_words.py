import random
import argparse

def get_words_list():
    file = open("/usr/share/dict/words", 'r')
    all_words = file.readlines()

    file.close()

    return all_words

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('num_words', help="enter the number of words to receive", type=int)

    args = parser.parse_args()
    num_words = args.num_words

    words = get_words(num_words)
    sentence = make_sentence(words)

    print(sentence)