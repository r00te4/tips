from twisted.internet import epollreactor
epollreactor.install()

from twisted.internet.protocol import Factory, Protocol
from twisted.internet import reactor

class my_protocol(Protocol):
    def __init__(self):
        print 'init'

    def __del__(self):
        print 'del'

    def connectionMade(self):
        print 'connectionMade'

    def connectionLost(self, reason):
        print 'connectionLost'

    def dataReceived(self, data):
        print 'dataReceived:%s' % (data)

if __name__=='__main__':

    f = Factory()
    f.protocol = my_protocol

    reactor.listenTCP(50000, f)
    reactor.run()


