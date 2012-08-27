#! /usr/bin/python
#coding=utf8

#callback 和 errback 都可以停止reactor
#既然defferred 支持callback 链和errback链, 则可以使用: addBoth 方法向callback和errback 链中加入了相同的函数,不论如果我们完成了重构.
#[注]: poem_done同样需要指定一个参数

from twisted.internet.defer import Deferred
from twisted.internet import reactor

def poem_get(res):
    print res

def poem_err(err):
    print err

def poem_done(_):
    reactor.stop()

d = Deferred()

d.addCallbacks(poem_get, poem_err)

d.addBoth(poem_done)

reactor.callWhenRunning(d.callback, "Another short poem.")

reactor.run()

#1. 我们不能无视errbacks.deferred内置对errback 的支持
#2. 多次触发callback可能导致很难调试的bug,Deferred只能被触发一次,你可以把他想象成try/except
#3. 用deferred,我们可以通过向链中增加新的callback和errback,并在各callback 和errback中移动代码完成重构

