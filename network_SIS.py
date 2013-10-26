import copy
import igraph
import random
import copy
import pylab as pl
import scipy
from scipy import random
import heapq

#model constructor
class simpleNetworkSIRModel():
    
    def __init__(self, generated_graph_input, b,  g, S, I):
        
        #parameters
        self.b = b
        self.g = g
        self.t = 0

        self.N = S + I
        
        #make a small world graph with as many nodes as we have individuals
        #self.graph = igraph.Graph.Watts_Strogatz(1, self.N, nei=nei, p = p)
        self.graph = generated_graph_input
        #we do this to get rid of multiple edges and self-loops that the 
        #randomly generated small-world graph might have
        self.graph.simplify()

    
    def graph_adj_ACC(self):
        
        # RAND pick
        #        deleted_vertex_list = scipy.random.randint(0,99,10)
        #        self.graph.delete_vertices(deleted_vertex_list)
        
        # ACC pick
        random_vertex_list = scipy.random.randint(0,99,10)
        ACC_vertex_list = []
        for random_node in random_vertex_list:
            neighbor_list = self.graph.neighbors(random_node)
            random_neighbor_id = scipy.random.randint(0, self.graph.neighborhood_size(random_node)-1, 1)
            ACC_vertex_list.append(neighbor_list[random_neighbor_id])
        
        self.graph.delete_vertices(ACC_vertex_list)
    
        print(self.graph)
        
        #        for del_vertex in deleted_vertex_list
        #            self.graph.delete_vertices(del_vertex.vs)
        
        
        #we're going to keep track of who is next to who using a list of lists
        self.adjacencyList = []
        for i in range(self.N):
            self.adjacencyList.append([])
        
        #now we're going to unpack the info from the graph
        #into a more usable format
        
        #this is an efficient way of doing it bust shows you
        #how to turn the graph into an
        #adjacency list
        for edge in self.graph.es: #looping over the graph's edge sequence
            #indexing adjacency by node ID,so we can do quick lookups
            self.adjacencyList[edge.source].append(edge.target)
            self.adjacencyList[edge.target].append(edge.source)
        
        #        print(self.graph.get_adjacency())
        
        #to use iGraph's internal method to do this, comment
        #out above and uncomment the following:
        #self.adjacencyList = graph.get_adjlist()
        
        #going to use this to store the *indices* of agents in each state
        self.sAgentList = []
        self.iAgentList = []
        self.rAgentList = []
        
        #and here we're going to store the counts of how many agents are in each
        #state @ each time step
        self.sList = []
        self.iList = []
        self.rList = []
        self.newIList = []
        
        #and we'll use this to keep track of recovery times in the more
        #efficient implementation
        self.recoveryTimesHeap = []
        
        #make a list of agent indices (easy because they're labeled 0-N)
        allAgents = range(self.N)
        
        #shuffle the list so there's no accidental correlation in agent actions
        random.shuffle(allAgents)
        
        #start with everyone susceptible
        self.sAgentList = copy.copy(allAgents)
        
        #now infect a few to infect at t = 0
        self.indexCases = []
        for i in xrange(I):
            indexCase = self.sAgentList[0]
            self.indexCases.append(indexCase)
            self.infectAgent(indexCase)
            self.iAgentList.append(indexCase)


    def graph_adj_RAND(self):
        
        # RAND pick
        deleted_vertex_list = scipy.random.randint(0,99,10)
        self.graph.delete_vertices(deleted_vertex_list)
        
        print(self.graph)
        
        
        #we're going to keep track of who is next to who using a list of lists
        self.adjacencyList = []
        for i in range(self.N):
            self.adjacencyList.append([])
    
        #now we're going to unpack the info from the graph
        #into a more usable format
    
        #this is an efficient way of doing it bust shows you
        #how to turn the graph into an
        #adjacency list
        for edge in self.graph.es: #looping over the graph's edge sequence
            #indexing adjacency by node ID,so we can do quick lookups
            self.adjacencyList[edge.source].append(edge.target)
            self.adjacencyList[edge.target].append(edge.source)
        
        #        print(self.graph.get_adjacency())
        
        #to use iGraph's internal method to do this, comment
        #out above and uncomment the following:
        #self.adjacencyList = graph.get_adjlist()
        
        #going to use this to store the *indices* of agents in each state
        self.sAgentList = []
        self.iAgentList = []
        self.rAgentList = []
        
        #and here we're going to store the counts of how many agents are in each
        #state @ each time step
        self.sList = []
        self.iList = []
        self.rList = []
        self.newIList = []
        
        #and we'll use this to keep track of recovery times in the more
        #efficient implementation
        self.recoveryTimesHeap = []
        
        #make a list of agent indices (easy because they're labeled 0-N)
        allAgents = range(self.N)
        
        #shuffle the list so there's no accidental correlation in agent actions
        random.shuffle(allAgents)
        
        #start with everyone susceptible
        self.sAgentList = copy.copy(allAgents)
        
        #now infect a few to infect at t = 0
        self.indexCases = []
        for i in xrange(I):
            indexCase = self.sAgentList[0]
            self.indexCases.append(indexCase)
            self.infectAgent(indexCase)
            self.iAgentList.append(indexCase)

    
    def graph_adj(self):
        
        print(self.graph)
        
        #we're going to keep track of who is next to who using a list of lists
        self.adjacencyList = []
        for i in range(self.N):
            self.adjacencyList.append([])
        
        #now we're going to unpack the info from the graph 
        #into a more usable format
        
        #this is an efficient way of doing it bust shows you
        #how to turn the graph into an 
        #adjacency list
        for edge in self.graph.es: #looping over the graph's edge sequence
            #indexing adjacency by node ID,so we can do quick lookups 
            self.adjacencyList[edge.source].append(edge.target) 
            self.adjacencyList[edge.target].append(edge.source)
                
#        print(self.graph.get_adjacency())
    
        #to use iGraph's internal method to do this, comment
        #out above and uncomment the following:
        #self.adjacencyList = graph.get_adjlist()
                                                                
        #going to use this to store the *indices* of agents in each state
        self.sAgentList = []
        self.iAgentList = []
        self.rAgentList = []

        #and here we're going to store the counts of how many agents are in each
        #state @ each time step
        self.sList = []
        self.iList = []
        self.rList = []
        self.newIList = []
        
        #and we'll use this to keep track of recovery times in the more
        #efficient implementation
        self.recoveryTimesHeap = []

        #make a list of agent indices (easy because they're labeled 0-N)
        allAgents = range(self.N)
        
        #shuffle the list so there's no accidental correlation in agent actions
        random.shuffle(allAgents)

        #start with everyone susceptible
        self.sAgentList = copy.copy(allAgents)
        
        #now infect a few to infect at t = 0
        self.indexCases = []
        for i in xrange(I):
            indexCase = self.sAgentList[0]
            self.indexCases.append(indexCase)
            self.infectAgent(indexCase)
            self.iAgentList.append(indexCase)

    
    def infectAgent(self,agent):
        self.sAgentList.remove(agent)
        
        #uncomment for exponentially distributed recovery times
        recoveryTime = self.t + scipy.random.exponential(1/self.g)
        
        #note that we're pushing a tuple onto the heap where the first element
        #is the recovery time and the second one is the agent's unique ID
        heapq.heappush(self.recoveryTimesHeap, (recoveryTime, agent))
        
        return 1
    
    def recoverAgents(self):
        #when we recover agents, it's similar to the previous
        #non-network implementation
        recoverList = []
        if len(self.recoveryTimesHeap) > 0:
            while self.recoveryTimesHeap[0][0] <= self.t:
                #we take advantage of python's built-in sequence sorting methods
                #which compare starting from the first element in a sequence,
                #so if these are all unique, we can sort arbitary sequences 
                #by their first element without a special comparison operator
                recoveryTuple = heapq.heappop(self.recoveryTimesHeap)
                recoverList.append(recoveryTuple[1])
                if len(self.recoveryTimesHeap) == 0:
                    break
    
        return recoverList

           
    #again, the guts of the model
    def run(self, step_num):
        #same as while I > 0
        while step_num > 0:
            step_num = step_num - 1
            tempIAgentList = []
            recoverList = []
            newI = 0
            #we only need to loop over the agents who are currently infectious
            for iAgent in self.iAgentList:
                #and then expose their network neighbors
                for agent in self.adjacencyList[iAgent]:
                    #given that the neighbor is susceptible
                    if agent in self.sAgentList:
                        if (random.random() < self.b): 
                            #and then it's the same as the other models
                            newI += self.infectAgent(agent)
                            tempIAgentList.append(agent)
                             
            
            #then get the list of who is recovering
            recoverList = self.recoverAgents()
            
            #and do the bookkeeping with agent indices
            
            #for recoveries
            for recoverAgent in recoverList:
                self.iAgentList.remove(recoverAgent)
                self.sAgentList.append(recoverAgent)
                    
            
            #and new infections
            self.iAgentList.extend(tempIAgentList)
            
            #then track the number of individuals in each state
            self.sList.append(len(self.sAgentList))
            self.iList.append(len(self.iAgentList))
                    #self.rList.append(len(self.sAgentList))
            self.newIList.append(newI)
            
            #increment the time
            self.t += 1
#            print('t', self.t, 'numS', len(self.sAgentList), 'numI', len(self.iAgentList) )
            
            #reshuffle the agent list so they step in a random order the next time
            #around
            random.shuffle(self.iAgentList)
        
        #and when we're done, return all of the relevant information
        return [self.sList, self.iList, self.rList, self.newIList]
        


if __name__=='__main__':

    
    #transmission parameters (daily rates scaled to hourly rates)
    b = .2
    g = .2
    
    #initial conditions (# of people in each state)
    S = 0
    I = 100
    
    generated_graph = igraph.Graph.Erdos_Renyi(100, 0.1)
    generated_graph_RAND = copy.deepcopy(generated_graph)
    generated_graph_ACC = copy.deepcopy(generated_graph)
    
    
    myNetworkModel = simpleNetworkSIRModel(generated_graph, b = b, g = g, S = S, I = I)
    myNetworkModel.graph_adj()
    networkResults = myNetworkModel.run(500)
    print(networkResults[1])
    
    I=90
    myNetworkModel_RAND = simpleNetworkSIRModel(generated_graph_RAND, b = b, g = g, S = S, I = I)
    myNetworkModel_RAND.graph_adj_RAND()
    networkResults_RAND= myNetworkModel_RAND.run(500)
    print(networkResults_RAND[1])
    
    I=90
    myNetworkModel_ACC = simpleNetworkSIRModel(generated_graph_ACC, b = b, g = g, S = S, I = I)
    myNetworkModel_ACC.graph_adj_ACC()
    networkResults_ACC = myNetworkModel_ACC.run(500)
    print(networkResults_ACC[1])
    
    
    
    
    pl.figure()
    pl.plot(networkResults[1], label = 'No Node Deleted')
    pl.plot(networkResults_RAND[1], label = 'RAND')
    pl.plot(networkResults_ACC[1], label = 'ACC')
    pl.xlabel('time')
    pl.ylabel('# infectious')
    pl.ylim([0, 150])
    pl.legend()
    pl.show()


    
            
