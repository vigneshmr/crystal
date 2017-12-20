# -*- coding: utf-8 -*
import os


def clear_screen():
    os.system('clear')


def get_line():
    lstr = ''
    for i in xrange(80):
        lstr = lstr + '―'
    return lstr
