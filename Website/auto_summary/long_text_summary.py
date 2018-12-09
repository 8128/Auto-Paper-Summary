#Copyright 2018 Tianyi Tang tty8128@Bu.edu
from gensim.summarization import summarize

class long_text_summary(object):

    def __init__(self,file):
        self.file = open(file,'r')
        self.result = ''
        self.text = self.file.read()
        if len(self.text)<3000:
            print('Your input is too short for long text summary.')
            exit(1)
        self.file.close()
        self.long_summarize(self.text)

    def long_summarize(self,text):
        self.result = summarize(text, ratio=0.01)

    def __str__(self):
        print(self.text)
        print('-----------------------')
        print(self.result)

if __name__ == "__main__":
    new_obj = long_text_summary('the_matrix_synopsis.txt')
    new_obj.__str__()