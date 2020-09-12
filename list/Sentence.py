import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    '''
    迭代器可迭代的原因就是实现了__getitem方法
    如果类实现了__iter__方法，则会调用该方法进行迭代，如果没有提供的话，
    则使用默认的__iter__方法，调用类里面的__getitem__从index为0开始迭代
    '''
    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
