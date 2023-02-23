from dictogram import Dictogram
import random

# class Markov():
#     def __init__(self, word_list):
#         self.states = []

#         self.states.append(State(word_list[-1]))
#         for i in range(len(word_list)-2, 0, -1):
#             state_index = len(word_list) - i + 1
#             self.states.append(word_list[i], self.states[state_index])

#         self.start_state = self.states[0]

#     def walk(self, start=None, sentence=""):
#         sentence_enders = ".!?"
#         if start == None:
#             start = self.start_state
        
#         word = self.states[start].sample()
#         sentence += f' {word}'

#         if sentence_enders not in word:
#             self.walk(next=start.sample(), sentence=sentence)
#         else:
#             return sentence

# class State(Dictogram):
#     def __init__(self, word=None, next_state=None):
#         super().__init__(word)
#         self.next = {}
#         self.word = 

#         for state in next_state:
#             self.add_state(state)

#     def add_count(self, word, count=1):
#         if word == self.word:
#             return super().add_count(word, count)

#     def add_state(self, state):
#         #TODO make self.next will contain key value with key being the word, and value a tuple of number of times occured and transition chance
#         self.next[state.word] = (State, self.calc_trans_chance(state))

#         self.transition.append(tuple(state, state.frequency(self.word) / self.frequency(self.word)))

#     def calc_trans_chance(self, state):
#         return self.next[state].frequency[self.word] / self.frequency(self.word)

#     def sample(self):
#         return super().sample(1)

class Markov(Dictogram):
    def __init__(self, word_list=None):
        """Initialize this histogram as a new dict and count given words."""
        super(Dictogram, self).__init__()  # Initialize this as a new dict
        self.stop = '.!?'
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        self.first = word_list[0]
        # Count words in given list, if any
        if word_list is not None:
            for i in range(1, len(word_list)):
                self.add_count(word_list[i - 1], word_list[i])
            self.add_count(word_list[-1], None)

    def add_count(self, word, next_word, count=1):
        if word in self:
            self[word]["count"] += count
            if next_word in self[word]:
                self[word][next_word] += count
            elif next_word is not None:
                self[word][next_word] = count
        else:
            self[word] = {next_word:count, "count":count}

        self.tokens += count
        self.types = len(list(self.keys()))

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        # TODO: Retrieve word frequency count
        if word in self:
            return self[word]['count']
        return 0

    def sample(self, num_words=1):
        """Return a word from this histogram, randomly sampled by weighting
        each word's probability of being chosen by its observed frequency."""
        # TODO: Randomly choose a word based on its frequency in this histogram
        keys = list(self.keys())
        values = []
        weight = 0
        for word in keys:
            weight += self[word]['count']
            values.append(weight)

        choices = random.choices(keys, cum_weights=values, k=num_words)

        text = ""
        for choice in choices:
            text += f"{choice}"

        return text

    def get_transition_percent(self, word, options):
        chances = 0
        cum_weights = []
        for next_word in options:
            if next_word != 'count':
                chances += self[word][next_word] / self[word]['count']*100
                cum_weights.append(chances)
        return cum_weights
    
    def walk(self, start=None, sentence=""):
    
        if start is None:
            start = self.first

        sentence += f'{start} '

        keys = list(self[start].keys())
        keys.remove('count')
        
        chances = self.get_transition_percent(start, keys)

        word = random.choices(keys, cum_weights=chances)[0]

        if word is  not None:
        
            if self.stop not in word:
                sentence = self.walk(word, sentence=sentence)

        return sentence
    
if(__name__ == '__main__'):
    chain = Markov(['I', 'like', 'dogs', 'and', 'you', 'like', 'dogs.', 'I', 'like', 'cats', 'but', 'you', 'hate', 'cats.'])

    print(chain.walk())
    