import random

# def histogram(word_list):
#     histogram = {}

#     #adds the word if it is already in the histogram, otherwise increments by 1
#     for word in word_list:
#         if word in histogram:
#             histogram[word] += 1
#         else:
#             histogram[word] = 1
    
#     return histogram

# def unique_words(histogram):
#     return len(histogram.keys())

# def frequency(histogram, word):
#     return histogram[word]

# def get_words(file_path):
#     file = open(file_path, "r")
#     word_list = []

#     words = file.readline()
#     while words != "":
#         words = words.rstrip('\n')
#         word_list.extend(words.split(" "))

#         words = file.readline()

#     return word_list

# def sample(histogram):
#     keys = list(histogram.keys())
#     values = []
#     weight = 0
#     for word in keys:
#         weight += histogram[word]
#         values.append(weight)

#     choice = random.choices(keys, cum_weights=values)

#     return choice[0]

class Histogram():
    def __init__(self, in_file):
        self.file = in_file
        
        self.words = self.__get_words(self.file)

        self.histogram = self.__create(self.words)

    def __create(self, word_list):
        histogram = {}

        #adds the word if it is already in the histogram, otherwise increments by 1
        for word in word_list:
            if word in histogram:
                histogram[word] += 1
            else:
                histogram[word] = 1
        
        return histogram
    
    def __get_words(self, file_path):
        file = open(file_path, "r")
        word_list = []

        words = file.readline()
        while words != "":
            words = words.rstrip('\n')
            word_list.extend(words.split(" "))

            words = file.readline()

        return word_list

    def get_unique_words(self):
        return len(self.histogram.keys())

    def get_frequency(self):
        return self.histogram[word]

    def get_sample(self, num_words):
        keys = list(self.histogram.keys())
        values = []
        weight = 0
        for word in keys:
            weight += self.histogram[word]
            values.append(weight)

        choices = random.choices(keys, cum_weights=values, k=num_words)

        text = ""
        for choice in choices:
            text += f"{choice} "

        return text

if __name__ == "__main__":

    words = get_words("data/test.txt")

    hg = histogram(words)

    samples = []
    for i in range (10000):
        samples.append(sample(hg))

    samples_histogram = histogram(samples)
    print(samples_histogram)