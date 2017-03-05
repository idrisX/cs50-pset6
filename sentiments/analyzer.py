import nltk
import helpers
class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives="positive-words.txt", negatives="negative-words.txt"):
        """Initialize Analyzer."""
        #open positive and negative text file
        positive_file=open(positives, "r")
        negative_file=open(negatives, "r")
        #establish two empty lists for positive and negative words
        self.positive_list=[]
        self.negative_list=[]
        #add words into each list line by line making it part of the object
        for line in positive_file:
            if line[0]!=";":
                self.positive_list.append(line.rstrip("\n"))
        for line in negative_file:
            if line[0]!=";":
                self.negative_list.append(line.rstrip("\n"))
            
        

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        #establish counter for determening whether a tweet is positive or negative
        score=0
        #make the tweet a list of seperate words
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)
        #iterate over every word in each tweet and either add or subtract a pont
        for word in tokens:
            word=word.lower()
            if word in self.positive_list:
                score+=1
            elif word in self.negative_list:
                score-=1
        return score
      
        
        
