#Copyright 2018 Tianyi Tang tty8128@Bu.edu
from gensim.summarization import summarize

class short_text_summary(object):

    def __init__(self,text):
        self.text = text
        if len(self.text)>3000:
            print('Your input is too long for short text summary.')
            exit(1)
        self.short_summarize(self.text)

    def short_summarize(self,text):
        self.result = summarize(text, ratio=0.2)

    def __str__(self):
        print(self.text)
        print('-----------------------')
        print(self.result)

if __name__ == "__main__":
    text = "Thomas A. Anderson is a man living two lives. By day he is an " + \
    "average computer programmer and by night a hacker known as " + \
    "Neo. Neo has always questioned his reality, but the truth is " + \
    "far beyond his imagination. Neo finds himself targeted by the " + \
    "police when he is contacted by Morpheus, a legendary computer " + \
    "hacker branded a terrorist by the government. Morpheus awakens " + \
    "Neo to the real world, a ravaged wasteland where most of " + \
    "humanity have been captured by a race of machines that live " + \
    "off of the humans' body heat and electrochemical energy and " + \
    "who imprison their minds within an artificial reality known as " + \
    "the Matrix. As a rebel against the machines, Neo must return to " + \
    "the Matrix and confront the agents: super-powerful computer " + \
    "programs devoted to snuffing out Neo and the entire human " + \
    "rebellion. "
    new_obj = short_text_summary(text)
    new_obj.__str__()