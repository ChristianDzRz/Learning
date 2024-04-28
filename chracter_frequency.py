import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter

class Document():
    """Stores document and contains visualization methods"""

    ALLOWED_FILE_EXTENSIONS = ("txt",)
    WHITE_SPACES = (" ", "\n")

    def __init__(self,file_name):
        self._file_name = file_name
        file_extensiondf= file_name.rsplit('.',1)[-1]
        if file_name.rsplit('.',1)[-1] in self.ALLOWED_FILE_EXTENSIONS:
            self._file_extension = file_name.rsplit('.',1)[-1]
        else:
            return ValueError("The file extension is not supported")
        self._document = None
        self._char_frequency = None

    
    def _read_document(self):
        with open(self._file_name) as f:
            while True:
                char = f.read(1)
                if char in self.WHITE_SPACES:
                   pass 
                elif char:
                    yield char
                else:
                    return

    
    def _calculate_char_frequency(self):
        counter = Counter()
        for char in self._read_document():
            counter.update(char)
        self._char_frequency = dict(counter)

    def plot_histogram(self):
        self._calculate_char_frequency()
        plt.bar(range(len(self._char_frequency)), list(self._char_frequency.values()), tick_label = list(self._char_frequency.keys()))
        plt.show()



if __name__ =="__main__":
    document1 = Document("test.txt")
    document1.plot_histogram()




