import random

def histogram(word_list):
    histogram = {}

    #adds the word if it is already in the histogram, otherwise increments by 1
    for word in word_list:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    
    return histogram

def unique_words(histogram):
    return len(histogram.keys())

def frequency(histogram, word):
    return histogram[word]

def get_words(file_path):
    file = open(file_path, "r")
    word_list = []

    words = file.readline()
    while words != "":
        words = words.rstrip('\n')
        word_list.extend(words.split(" "))

        words = file.readline()

    return word_list

def sample(histogram):
    keys = list(histogram.keys())
    values = []
    weight = 0
    for word in keys:
        weight += histogram[word]
        values.append(weight)

    choice = random.choices(keys, cum_weights=values)

    return choice[0]
if __name__ == "__main__":

    words = get_words("data/test.txt")

    hg = histogram(words)

    samples = []
    for i in range (10000):
        samples.append(sample(hg))

    samples_histogram = histogram(samples)
    print(samples_histogram)