
from dfs_iterative import dfs_iterative as DFSiter
from bfs import bfs as BFS
from dfs_path import dfs_path as DFSpath
from bfs_path import bfs_path as BFSpath
from dfs_findSCC import dfs_findSCC as SCC
from dijkstraAlgo import dijk
#import kruskal

def main():
    while True:
        sel = input("Select which question you would like to test (1, 2, 3, 4, 5) (Any other key to quit)")


        if sel == "1":
            print("Question 1: ")
            sel = input("DFS or BFS? ")
            if sel.upper() == "DFS":
               DFSiter()
            else: 
               BFS()

        elif sel == "2":
            print("Question 2: ")
            sel = input("DFS or BFS? ")
            if sel.upper() == "DFS":
               dfs_path()
            else: 
               BFSpath()

        elif sel == "3":
            print("Question 3: ")
            SCC()

        elif sel == "4":
            print("Question 4: ")
            dijk()

        elif sel == "5":
            print("Question 5: ")
            #kruskal
        else:
            break


main()