from mininet.topo import Topo

# Topologia de la primera red
class Interconectados(Topo):

    def __init__(self):
        # Usar constructor de la clase padre
        Topo.__init__(self)

        # Crea la topologia de red
        host_uno = self.addHost('h1')
        host_dos = self.addHost('h2')
        host_tres = self.addHost('h3')
        host_cuatro = self.addHost('h4')

        switch_uno = self.addSwitch('s1')
        switch_dos = self.addSwitch('s2')
        switch_tres = self.addSwitch('s3')
        switch_cuatro = self.addSwitch('s4')

        # Crea los links entre los host correspondientes

		# Host 1 y Host 2
        self.addLink(host_uno, switch_uno)
        self.addLink(switch_uno, switch_dos)
        self.addLink(switch_dos, host_dos)
		# Host 1 y Host 3
        self.addLink(host_uno, switch_uno)
        self.addLink(switch_uno, switch_tres)
        self.addLink(switch_tres, host_tres)
		# Host 1 y Host 4
        self.addLink(host_uno, switch_uno)
        self.addLink(switch_uno, switch_cuatro)
        self.addLink(switch_cuatro, host_cuatro)

topos = {'interconectado': (lambda: Interconectados())}

