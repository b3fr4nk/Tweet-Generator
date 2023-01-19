def histogram(word_list):
    histogram = {}

    #adds the word if it is already in the histogram, otherwise increments by 1
    words
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

if __name__ == "__main__":

    words = get_words("data/dickens.txt")

    hg = histogram(words)

    print(hg)
    print(frequency(hg, "one"))