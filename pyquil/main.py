from grove.pyqaoa.maxcut_qaoa import maxcut_qaoa
import pyquil.api as api
qvm_instance = api.QVMConnection()

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

n = 2 #min number of nodes

'''     Uncomment for demo
input_graph = nx.complete_graph(n)
nx.draw(input_graph)
plt.show()
'''

for i in range(2,15):
    input_graph = nx.complete_graph(i)

    steps = 2
    inst = maxcut_qaoa(graph=input_graph, steps=steps)
    betas, gammas = inst.get_angles()

    t = np.hstack((betas, gammas))
    param_prog = inst.get_parameterized_program()
    prog = param_prog(t)
    wf = qvm_instance.wavefunction(prog)
    wf = wf.amplitudes

    max_amp = 0
    max_amp_ref = -1

    for state_index in range(2**inst.n_qubits):
        print(inst.states[state_index], np.conj(wf[state_index])*wf[state_index])
        if np.conj(wf[state_index])*wf[state_index] > max_amp:
            max_amp = np.conj(wf[state_index])*wf[state_index]
            max_amp_ref = state_index

    print("Best: ", inst.states[max_amp_ref], max_amp)

    node_colors = []
    for i in input_graph:
        if int(str(inst.states[max_amp_ref])[i]) == 1:
            node_colors.append('green')
        else:
            node_colors.append('blue')

    nx.draw(input_graph, node_color=node_colors, with_labels=True)
    plt.show()
    plt.cla()
