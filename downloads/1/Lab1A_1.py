import numpy as np
import pylab as plt



def convertEnthalpyToDistribution_1(E,k,T):
        return((k*T)/E)

def convertEnthalpyToDistribution_2(E,k,T):
        return(np.exp(-E/(k*T)))

def convertEnthalpyToDistribution_3(E,k,T):
	return(np.exp(-(k*T)/E))

def convertEnthalpyToDistribution_4(E,k,T):
	return(np.exp(-(E+10)/(k*T)))

def convertEnthalpyToDistribution_5(E,k,T):
	return( np.exp(-E/(k*(T-10))))





def sampleStates(stateEnergies, numberOfObservations, k, T):
    Nstates = len(stateEnergies)
    Probs = np.zeros(Nstates)
    PartitionFunction = 0.0

    for i in np.arange(Nstates):
        Probs[i]            =  convertEnthalpyToDistribution_2(energies[i],k,T)

        PartitionFunction   = PartitionFunction + Probs[i]


    Probs = Probs /  PartitionFunction

    ProbThresholds=np.cumsum(Probs)


    print("The probabilites of the states are")
    print(Probs)
    print("And the thresholds of the states we will use are")
    print(ProbThresholds)

    states = np.zeros(numberOfObservations)


    for i in np.arange(numberOfObservations):
        current = np.random.rand()

        while current>ProbThresholds[int(states[i])]:
                states[i]+=1

    bins=np.arange(Nstates+1)+0.5
    y,dummy = plt.histogram(states+1, bins=bins, normed=True)
    
    plt.bar(np.arange(len(energies))+0.9, y, width=0.4, fc='blue',alpha=0.5, label='sampled states')





k = 8.6e-5
T = 1000.0

energies=[-0.30, -0.35, -0.25]

steps = 200

predictedDistribution = np.zeros(len(energies))
PartitionFunction = 0.0
N=len(energies)
for i in np.arange(N):
    predictedDistribution[i]  =  convertEnthalpyToDistribution_2(energies[i],k,T)
    PartitionFunction = PartitionFunction + predictedDistribution[i] 
predictedDistribution = predictedDistribution / PartitionFunction




# Prepare figure
f = plt.figure(figsize=(20,10))
fs = f.add_subplot(111)
fs.set_ylim([0,1.1])
fs.set_xlabel('State')
fs.set_ylabel('Population/Distribution')

fs.bar(np.arange(len(energies))+0.5, predictedDistribution, width=0.4, fc='red',alpha=0.5, label='predicted Distribution from chosen conversion formula')


sampleStates(energies,steps,k,T)

fs.legend(loc='upper center')
plt.show()
