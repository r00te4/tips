#! /usr/bin/python
#coding=utf8

#尝试着按了callback 的按钮也尝试着按了errback 的按钮.就像任何一个好的工程师一样,你可能想要一遍一遍的按它们.
#灰常有意思,defferred 不会让我们多次触发正常的callback.实际上,不管如何defferred 都不让人触发两次,

from twisted.internet.defer import Deferred

def out(s):
    print s

d = Deferred()

d.addCallbacks(out, out)

d.callback("hello, I'm first callback'")

d.callback("hello, I'm second callback")
