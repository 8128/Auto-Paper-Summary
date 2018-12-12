# Copyright 2018 Tianyi Tang tty8128@Bu.edu
from gensim.summarization import summarize


class long_text_summary(object):

    def __init__(self, file):
        self.file = file
        self.result = ''
        self.text = self.file.read().decode('utf-8')
        if len(self.text) < 3000:
            self.errormessage = 'Your input is too short for long text summary.'
        else:
            try:
                self.long_summarize()
            except ValueError:
                self.errormessage = 'input must have more than one sentence'
        self.file.close()

    def long_summarize(self):
        self.result = summarize(self.text, ratio=0.02)


class short_text_summary(object):

    def __init__(self, text):
        self.text = text
        self.result = ''
        try:
            self.short_summarize()
        except ValueError:
            self.errormessage = 'input must have more than one sentence'

    def short_summarize(self):
        self.result = summarize(self.text, ratio=0.4)
