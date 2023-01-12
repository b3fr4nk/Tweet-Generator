import argparse
import random

def rearrange(words):
    output  = ""
    temp_list = words

    for i in range(len(words)):
        selection = random.choice(temp_list)
        output += f"{selection} "
        temp_list.remove(selection)

    return output

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('words', metavar='words', type=str, nargs='*', help="enter the words to be randomized")

    args = parser.parse_args()

    words = args.words
    print(rearrange(words))