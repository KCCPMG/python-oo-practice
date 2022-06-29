"""Word Finder: finds random words from a dictionary."""
from random import randint as rand

class WordFinder:
    """
    Class to return random words from a given file of words
    """
    def __init__(self, path):
        """Create instance with path to a file on disk that contains words, one per line, read the file at that path, make an attribute list of those words, print word list length
        
        >>> wf = WordFinder("words.txt")
        235886 words read
        
        >>> wf.random() in wf.words
        True

        >>> wf.random() in wf.words
        True

        >>> wf.random() in wf.words
        True

        >>> wf.random() in wf.words
        True


        """
        self.path = path
        self.words = []
        fhand = open(self.path, 'r')
        for line in fhand.readlines():
            self.words.append(line.strip())
        fhand.close()
        self.print_word_list_length()

    
    def print_word_list_length(self):
        """Print length of self.words"""
        print(f"{len(self.words)} words read")
    

    def random(self):
        """Return a random word from the instance's list of words"""
        randint = rand(0, len(self.words))
        return self.words[randint]



class SpecialWordFinder(WordFinder):
    def __init__(self, path):
        """Create instance with path to a file on disk that contains words, one per line, read the file at that path, make an attribute list of those words if they aren't common or blank, print word list length
        
        >>> swf = SpecialWordFinder("words.txt")
        235886 words read

        >>> swf.random() in swf.words
        True

        >>> swf.random() in swf.words
        True

        >>> swf.random() in swf.words
        True

        >>> swf.random() in swf.words
        True
        
        """
        self.path = path
        self.words = []
        fhand = open(self.path, 'r')
        for line in fhand.readlines():
            if not line.startswith("#") and not line.strip() == "":
                self.words.append(line.strip())
        fhand.close()
        self.print_word_list_length()
