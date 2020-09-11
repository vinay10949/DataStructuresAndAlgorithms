import sys
adj=[[0 for i in range(100)] for j in range(100)]
def createGraph(n):
    max_edges=0
    max_edges=(n*(n-1))
    for i in range(max_edges):
        print("enter orgin=-1 and destination=-1 to break the loop")
        origin=int(input())
        destination=int(input())
        if(origin ==-1 and destination ==-1):
            break
        if(origin>=n or destination>=n or origin<0 or destination<0):
            print("invalid graph")
            break
        
        else:
            adj[origin][destination]=1

def addEdge(origin,destination,n):
    if(origin>=n or destination>=n or origin<0 or destination<0):
        print("invalid graph")
        return
    adj[origin][destination]=1

def delEdge(origin,destination,n):
    if(origin>=n or destination>=n or origin<0 or destination<0):
        print("invalid deletion")
        return
    adj[origin][destination]=0
    
def display(n):
    for i in range(n):
        for j in range(n):
            print(adj[i][j]),
        print("\n")
    
if __name__=='__main__':
    print("enter number of vertices")
    n=int(input())
    createGraph(n)
    origin,destination=0,0
    while(1):
        print("1.Insert an edge\n")
        print("2.Delete an edge\n")
        print("3.Display\n")
        print("4.Exit\n")
        print("Enter your choice : ")
        choice=int(input())
        
        if choice==1:
            print("Enter orgin and destination to insert Edge")
            origin=int(input())
            destination=int(input())
            addEdge(origin,destination,n)
            
        elif choice==2:
            print("Enter orgin and destination to delete Edge")
            origin=int(input())
            destination=int(input())
            delEdge(origin,destination,n)
        elif choice==3:
            print("Display")
            display(n)
        elif choice==4:
            sys.exit(0)

