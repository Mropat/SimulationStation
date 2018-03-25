import numpy as np
import pylab as plt


def convertEnthalpyToDistribution(E,k,T):
        return(np.exp(-E/(k*T)))


def rands():
   return (np.random.rand()*100)


global k
global T 
global N_hops
k = 8.6e-5
T = 1000.0
N_hops = 500
energies=[-0.30, -0.35, -0.25, -0.30, -0.20 ]
# Create a number of energy-states, in this case five of them
energies=[-0.30, -0.35, -0.25, -0.30, -0.20 ]

if __name__ == "__main__":
    for i in energies:
        print (rands() - convertEnthalpyToDistribution(i,k,T))
        convertEnthalpyToDistribution(i,k,T)