package main

import "fmt"

type Graph struct{
	data [][]int
}

func NewGraph(size int ) *Graph{
	g:=Graph{}
	g.data=make([][]int,size)
	for k,i :=range g.data{
		for j:=0;j<size;j++{
			i=append(i,0 )
		}
		g.data[k]=i
	}
	return &g
}

func(g *Graph)add_edge(v1 int,v2 int){
	if v1>=len(g.data) ||v2>=len(g.data){
		fmt.Println("Vertices doesnt exist ,Size exceeded")
	}
	if v1==v2{
		fmt.Println("Both Vertices are same ")
	}
	g.data[v1][v2]=1
	g.data[v2][v1]=1
}
func(g *Graph)printGraph(){
	for _,i :=range g.data{
		fmt.Println(i)
	}
}


func(g *Graph)remove_edge(v1 int,v2 int){
	if v1>=len(g.data) ||v2>=len(g.data){
		fmt.Println("Vertices doesnt exist ,Size exceeded")
	}
	if 	g.data[v1][v2]==0 || g.data[v2][v1]==0{
		fmt.Println("Cannot remove eddge between ",v1,v2," Since No Edge exist between two vertices")
	}
	g.data[v1][v2]=0
	g.data[v2][v1]=0
}

func main(){
	g:=NewGraph(5)
	fmt.Println("Graph Data using Adjanceny matrix ")
	g.add_edge(1,4)
	g.add_edge(2,0)
	g.remove_edge(1,2)
	g.printGraph()
}