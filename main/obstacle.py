import yaml
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate


def compute_obstacles(reso):
    stream = open("/home/gianmarco/Desktop/el2425/svea_starter/src/svea_core/resources/params/obstacles.yaml")
    val = yaml.safe_load(stream)

    fin_ox = []
    fin_oy = []

    for rig in range(len(val['obstacles'])): #range(len(val['obstacles']))
        for col in range(len(val['obstacles'][rig])-1):#range(len(val['obstacles'][rig])-1):
            pre_x = val['obstacles'][rig][col][0]
            pre_y = val['obstacles'][rig][col][1]
            succ_x = val['obstacles'][rig][col+1][0]
            succ_y = val['obstacles'][rig][col+1][1]
            
            lin_x = list(np.linspace(pre_x, succ_x, abs(pre_x - succ_x)/reso))
            f = interpolate.interp1d([pre_x, succ_x], [pre_y, succ_y], kind="slinear")
            lin_y = list(f(lin_x))
            
            fin_ox += lin_x
            fin_oy += lin_y
        
        
        lin_x = list(np.linspace(succ_x, val['obstacles'][rig][0][0], abs(succ_x - val['obstacles'][rig][0][0])/reso))
        f = interpolate.interp1d([succ_x, val['obstacles'][rig][0][0]], [succ_y, val['obstacles'][rig][0][1]], kind="slinear")
        lin_y = list(f(lin_x))
        fin_ox += lin_x
        fin_oy += lin_y

    # print(len(fin_ox) == len(fin_oy))
    plt.figure("Check")
    plt.plot(fin_ox, fin_oy, 'bo')
    plt.show()

    return fin_ox, fin_oy


compute_obstacles(0.1)