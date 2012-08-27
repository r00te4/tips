#! /usr/bin/python
#coding=utf8

#当我们用deferred 的时候,我们可以用正常的Exception, 而无需使用导入Failure模块;
#deferred 会自动的为我们转为Failure对象.
#defferred 会保证每一个errback被触发的时候都会被传入一个Failure 实例

from twisted.internet.defer import Deferred
from twisted.python.failure import Failure

def poem_get(res):
    print "Your poem is served:"
    print res

def poem_failed(err):
    print "No poetry for you"
    print err

d = Deferred()

d.addCallbacks(poem_get, poem_failed)

#d.errback(Failure(Exception("I have failed !")))
d.errback(Exception("I have failed !"))
