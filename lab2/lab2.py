import sys

class Edge:
    def __init__(self, f_, t_, i_):
        self.m_nFrom = f_
        self.m_nTo = t_
        self.m_sInput = i_
    def print(self):
        print("%d,%d,%s" % (self.m_nFrom, self.m_nTo, self.m_sInput))

class Graph:
    def __init__(self, fp_=0):
        self.m_lEdges = []
        if(fp_ != 0):
            for line in fp_:
                elem = line[0:-1].split(',')
                self.m_lEdges.append(Edge(int(elem[0]), int(elem[1]), elem[2]))

    
    def getEClosureS(self, s_):
        r = set()
        r.add(s_)
        que = [s_]

        while len(que)>0:
            tmp = que.pop(0)
            for edge in self.m_lEdges:
                if edge.m_nFrom == tmp and edge.m_sInput == '' and edge.m_nTo not in r:
                    r.add(edge.m_nTo)
                    que.append(edge.m_nTo)
        return r
    
    
    def getEClosureT(self, t_):
        r = set()
        for state in t_:
            r |= self.getEClosureS(state)
        return r
    
    def getMove(self, t_, a_):
        r = set()
        for state in t_:
            for edge in self.m_lEdges:
                if edge.m_nFrom == state and edge.m_sInput == a_:
                    r.add(edge.m_nTo)
        return r
    
    def addEdge(self, f_, t_, i_):
        self.m_lEdges.append(Edge(f_, t_, i_))
        
    def print(self):
        for e in self.m_lEdges:
            e.print()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit("Usage: python %s <input file>" % sys.argv[0])
    fp = open(sys.argv[1], "r")
    NFA = Graph(fp)
    DFA = Graph()
    Dstate = []

    Dstate.append(NFA.getEClosureS(0))
    sigma = sorted({i.m_sInput for i in NFA.m_lEdges if i.m_sInput})    #to get same result always

    for idx, state in enumerate(Dstate):
        for a in sigma:
            s = NFA.getEClosureT(NFA.getMove(state,a))
            if s not in Dstate:
                Dstate.append(s)
            DFA.addEdge(idx,Dstate.index(s),a)
            
    DFA.print()
