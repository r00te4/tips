#! /usr/bin/python
#coding=utf8

from twisted.internet.defer import Deferred

#新建了一个新的deferred,然后用addCallbacks加入了一对callback/errback.然后callback触发了正常结果的callback.当然这里并没有一个callback 链,只有一个callback
#向deferred 中加入的callback一次接收一个参数,或者一个正常的结果或者一个错误的结果.
#实际上deferred支持callback和errback带有多个参数,但是最少一个.但第一个参数永远是callback 或者errback 
#增加callbacks和errbacks的时候是一对对的
#callback方法用一个正常的结果触发deferred 
#触发defferred之后立即调用了callback.这里根本没有异步,因为没有用reactor.
#要触发errback 链只要调用errback方法 就可以了,这个方法参数是一个错误的返回结果.就像之前的callback一样,errback在触发之后立即被调用了.

def got_poem(res):
    print 'Your poem is served:'
    print res

def poem_failed(err):
    print 'No poetry for you.'

d = Deferred()

# add a callback/errback pair to the chain
d.addCallbacks(got_poem, poem_failed)

# fire the chain with a normal result
d.callback('This poem is short.')


