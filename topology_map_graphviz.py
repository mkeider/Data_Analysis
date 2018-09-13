from graphviz import Digraph
import json

topology = [
{
  "neighbor": "R3#",
  "local_interface": "Fas 0/1",
  "capability": "R S I",
  "platform": "3725",
  "neighbor_interface": "Fas 0/1",
  "local_host": "R1#"
},
{
  "neighbor": "R2#",
  "local_interface": "Fas 0/0",
  "capability": "R S I",
  "platform": "3725",
  "neighbor_interface": "Fas 0/0",
  "local_host": "R1#"
},
{
  "neighbor": "R1#",
  "local_interface": "Fas 0/0",
  "capability": "R S I",
  "platform": "3725",
  "neighbor_interface": "Fas 0/0",
  "local_host": "R2#"
},
{
  "neighbor": "R3#",
  "local_interface": "Fas 0/1",
  "capability": "R S I",
  "platform": "3725",
  "neighbor_interface": "Fas 0/0",
  "local_host": "R2#"
},
{
  "neighbor": "R2#",
  "local_interface": "Fas 1/0",
  "capability": "R S I",
  "platform": "3725",
  "neighbor_interface": "Fas 0/0",
  "local_host": "R4#"
},
{
  "neighbor": "R4#",
  "local_interface": "Fas 0/0",
  "capability": "R S I",
  "platform": "3725",
  "neighbor_interface": "Fas 1/0",
  "local_host": "R2#"
},
{
  "neighbor": "R2#",
  "local_interface": "Fas 0/1",
  "capability": "R S I",
  "platform": "3725",
  "neighbor_interface": "Fas 0/0",
  "local_host": "R3#"
},
{
  "neighbor": "R2#",
  "local_interface": "Fas 1/1",
  "capability": "R S I",
  "platform": "3725",
  "neighbor_interface": "Fas 1/2",
  "local_host": "R3#"
}
  ]


neighbor = topology

def create_topo(neigh_list):
    nodes = []
    edges = []
    for neighbors in neigh_list:
        if neighbors['local_host'] not in nodes:

            nodes.append(neighbors['local_host'])

            if neighbors ['neighbor']and ['local_interfaces'] not in edges:

             edges.append([neighbors['local_host'], neighbors['neighbor'],neighbors['local_interface']+ "-" + neighbors['neighbor_interface']])

    return [nodes,edges]


my_topo = create_topo(neighbor)

print(my_topo)



dot = Digraph(comment='My Network')

def make_topology(network_name, mytopo):
    dot = Digraph(comment=network_name, format='pdf')
    dot.attr('node', shape='ellipse', color='lightblue2',style='filled',fontsize='5',height='.1',fixedsiz='true')
    dot.attr('edge', weight='2',fontsize='4')
    dot.attr('edge', arrowhead='none')
    dot.body.append(r'label = "\n\nKeider Test Network Diagram"')
    dot.body.append('fontsize=10')
    for i in mytopo[0]:
        dot.node(i)
    for i in mytopo[1]:
        dot.edge(i[0], i[1], i[2])
    return dot


dot = make_topology("My New Network", my_topo)
dot.render(filename='SimpleTopo')
