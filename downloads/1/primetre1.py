
import numpy as np
import pylab as plt

def convertEnthalpyToDistribution(E,k,T):
        return(np.exp(-E/(k*T)))


def BoltzmannRule(st_at, st_to):

    at_state = convertEnthalpyToDistribution(energies[st_at],k,T)
    to_state = convertEnthalpyToDistribution(energies[st_to],k,T)

    if at_state / (at_state + to_state) > np.random.rand():
        return False
    else:
        return True


def simulate_rule(Energies,Nsteps):
        Nstates = len(Energies)
        statesOverTime = np.zeros(Nsteps)
        statesOverTime[0] = np.random.randint(0,Nstates)
        for i in np.arange(Nsteps-1):
            currentState = statesOverTime[i].astype(int)
            newState = currentState.astype(int)
            while newState == currentState:
                newState = np.random.randint(0,Nstates)

            move=False
            move=BoltzmannRule(currentState, newState)

            if(move):
                statesOverTime[i+1] = newState
            else:
                statesOverTime[i+1] = currentState


        bins=np.arange(Nstates+1)+0.5
        y,dummy = plt.histogram(statesOverTime+1, bins=bins, normed=True)
        plt.bar(np.arange(len(energies))+0.9, y, width=0.4, fc='blue',alpha=0.5, label='sampledByRule')
        return statesOverTime


global k
global T 
global N_hops
k = 8.6e-5
T = 1000.0
N_hops = 10000


energies=[-0.30, -0.35, -0.25, -0.30, -0.20 ]


predictedDistribution = np.zeros(len(energies))
PartitionFunction = 0.0
for i in np.arange(len(energies)):
    predictedDistribution[i]  = convertEnthalpyToDistribution(energies[i],k,T)
    PartitionFunction         = PartitionFunction + predictedDistribution[i]
predictedDistribution = predictedDistribution / PartitionFunction
plt.bar(np.arange(len(energies))+0.5, predictedDistribution, width=0.4, fc='red',alpha=0.5, label='prediction')


output = simulate_rule(energies,N_hops)
plt.legend()

plt.figure()
plt.plot(output[::int(N_hops/200)])
plt.show()
