#! /usr/bin/python

#from twisted.internet import epollreactor
#epollreactor.install()

from twisted.internet import reactor,protocol
from twisted.protocols import basic

class EchoProtocol(basic.LineReceiver):
    def lineReceived(self,line):
        if line=='quit':
            self.sendLine("Goodbye.")
            self.transport.loseConnection()
        else:
            print line
            self.sendLine("You said: "+line)

class EchoServerFactory(protocol.ServerFactory):
    protocol=EchoProtocol

if __name__=="__main__":
    port=50000
    reactor.listenTCP(port,EchoServerFactory())
    reactor.run()
