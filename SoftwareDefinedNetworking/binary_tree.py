from mininet.topo import Topo

class MyTopo( Topo ):
        "binary tree topology example"

        def __init__( self ):
                "create custom topo"

                Topo.__init__( self )

                hostOne = self.addHost( 'h1' )
                hostTwo = self.addHost( 'h2' )
                hostThree = self.addHost( 'h3' )
                hostFour = self.addHost( 'h4' )
                hostFive = self.addHost( 'h5' )
                hostSix = self.addHost( 'h6' )
                hostSeven = self.addHost( 'h7' )
                hostEight = self.addHost( 'h8' )

                switchOne = self.addSwitch( 's1' )
                switchTwo = self.addSwitch( 's2' )
                switchThree = self.addSwitch( 's3' )
                switchFour = self.addSwitch( 's4' )
                switchFive = self.addSwitch( 's5' )
                switchSix = self.addSwitch( 's6' )
                switchSeven = self.addSwitch( 's7' )

                self.addLink( hostOne, switchOne )
                self.addLink( hostTwo, switchOne )
                self.addLink( hostThree, switchTwo )
                self.addLink( hostFour, switchTwo )
                self.addLink( hostFive, switchThree )
                self.addLink( hostSix, switchThree )
                self.addLink( hostSeven, switchFour )
                self.addLink( hostEight, switchFour )
                self.addLink( switchOne, switchFive )
                self.addLink( switchTwo, switchFive )
                self.addLink( switchThree, switchSix )
                self.addLink( switchFour, switchSix )
                self.addLink( switchFive, switchSeven )
                self.addLink( switchSix, switchSeven )


topos = { 'mytopo': ( lambda: MyTopo() ) }