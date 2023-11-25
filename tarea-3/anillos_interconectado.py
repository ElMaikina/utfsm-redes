from mininet.topo import Topo

# Topologia de prueba
class MyTopo(Topo):

    def __init__(self):
        # Usar constructor de la clase padre
        Topo.__init__(self)

        # Crea la topologia de red
        host_izq = self.addHost('h1')
        host_der = self.addHost('h2')
        swch_izq = self.addSwitch('s1')
        swch_der = self.addSwitch('s2')

        # Crea los links
        self.addLink(host_izq, swch_izq)
        self.addLink(host_der, swch_der)
        self.addLink(swch_izq, swch_der)

topos = {'topitos': (lambda: MyTopo())}

