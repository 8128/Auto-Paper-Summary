# Copyright 2018 Tianyi Tang tty8128@Bu.edu
from gensim.summarization import summarize
import logging


class long_text_summary(object):

    def __init__(self, file):
        self.file = open(file, 'r')
        self.result = ''
        self.text = self.file.read()
        if len(self.text) < 3000:
            print('Your input is too short for long text summary.')
            exit(1)
        self.file.close()
        try:
            self.long_summarize()
        except ValueError:
            self.errormessage = 'input must have more than one sentence'

    def long_summarize(self):
        self.result = summarize(self.text, ratio=0.05)


class short_text_summary(object):

    def __init__(self, text):
        self.text = text
        self.result = ''
        if len(self.text) > 3000:
            print('Your input is too long for short text summary.')
            exit(1)
        try:
            self.short_summarize()
        except ValueError:
            self.errormessage = 'input must have more than one sentence'

    def short_summarize(self):
        self.result = summarize(self.text, ratio=0.25)

