import random
from collections import defaultdict

class MarkovChainTextGenerator:
    def __init__(self, n = 3):
        self.model = defaultdict(list)
        self.n = n
    
    def train(self, text):
        words = text.split()
        if(len(words) - self.n <= 0):
            print("Training text too low!")
            return
        
        for i in range(len(words) - self.n):
            key = tuple(words[i:i + self.n])
            next_word = words[i + self.n]
            self.model[key].append(next_word)

    def generate_text(self, seed_text, num_words = 20):
        words = seed_text.split()
        if len(words) < self.n:
            key = random.choice(list(self.model.keys()))
        else:
            key = tuple(words[-self.n:])
            if key not in self.model:
                key = random.choice(list(self.model.keys()))

        result = list(key)

        for _ in range(num_words):
            next_words = self.model.get(key)
            if not next_words:
                break
            next_word = random.choice(next_words)
            result.append(next_word)
            key = tuple(result[-self.n:])
            
        return " ".join(result)