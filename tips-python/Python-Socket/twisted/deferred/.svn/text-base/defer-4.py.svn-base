#! /usr/bin/python
#coding=utf8

#启动reactor之后,用callWhenRunning来触发defferred.
#我们利用callWhenRunning 接收额外的参数然后传递给callback.
#在twisted 中有很多注册callback 的api都遵守这个规则,包括吧callback 加进deferred 的api.

from twisted.internet.defer import Deferred
from twisted.internet import reactor

def poem_get(res):
    print res
    reactor.stop()

def poem_err(err):
    print err
    reactor.stop()

d = Deferred()

d.addCallbacks(poem_get, poem_err)

reactor.callWhenRunning(d.callback, "Another short poem")

reactor.run()

