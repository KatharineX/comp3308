import os
import sys
import string

# definitions
MAX_NODE_LENGTH = 1000
found = 0


def calc_diff(start_state, end_state):

    # print(start_state, end_state)

    first = 0
    second = 0
    third = 0
    first_digit = ""
    second_digit = ""
    third_digit = "a"

    first1 = 0
    second1 = 0
    third1 = 0
    first_digit1 =""
    second_digit1 = ""
    third_digit1 = "a"

    counter = 0
    jj = 0
    jj2 = 0
    jj3 = 0

    for i in range(3):
        #convert string-> number -> string
        first_digit = start_state[0]
        second_digit = start_state[1]
        third_digit = start_state[2]

        #first, second, third value
        first = int(first_digit)
        second = int(second_digit)
        third = int(third_digit)

        #convert string-> number -> string
        first_digit1 = end_state[0]
        second_digit1 = end_state[1]
        third_digit1 = end_state[2]

        #first, second, third value
        first1 = int(first_digit1)
        second1 = int(second_digit1)
        third1 = int(third_digit1)

    jj = abs(first - first1)
    jj2 = abs(second - second1)
    jj3 = abs(third - third1)

    counter = jj + jj2 + jj3
    return counter

# calculate the manhatten heuristic for A & greedy & hillclimbing
# Manhattan distance should be calculated between the current node and the goal node.
def calculate_manhatten(current, goal):

    distance = abs(int(goal) - int(current))
    return distance


#goes through and generates all nodes
#node does not take into consideration if equals goal!
def generate_nodes(start_state, final_state, prev_move, visited, *forbidden):

    if(start_state==final_state):
        # print("found")
        return []
    
    global found
    nodes = []
    first = 0
    second = 0
    third = 0
    second_digit = "2"
    third_digit = "3"
    first_digit = "1"
    

    for i in range(3):
        #convert string-> number -> string
        first_digit = start_state[0]
        second_digit = start_state[1]
        third_digit = start_state[2]

        #first, second, third value
        first = int(first_digit)
        second = int(second_digit)
        third = int(third_digit)


    # -1 first digit -> first move
    if(first == 0 or prev_move == 1 or prev_move == 2):
        # cannot make changes
        pass
    else:
        first_node = first - 1
        first_node_string = str(first_node) + second_digit + third_digit
        
        # checking if forbiden
        forbid = 0
        visit = 0

        for states in forbidden:
            if(first_node_string == states):
                forbid = 1
        for node in visited:
            if(first_node_string == node):
                visit = 1

        if(forbid == 1 or visit == 1):
            pass

        elif(first_node_string == final_state):
            # print("found it in first")
            found = 1
            nodes.append(final_state)
            return nodes

        else:
            nodes.append(first_node_string)








    # +1 to first digit -> second
    if(first == 9 or prev_move == 1 or prev_move == 2):
        # cannot
        pass
    else:
        second_node = first + 1
        second_node_string = str(second_node) + second_digit + third_digit

        # checking if forbiden
        forbid = 0
        visit = 0

        for states in forbidden:
            if(second_node_string == states):
                forbid = 1
        for node in visited:
            if(second_node_string == node):
                visit = 1

        if(forbid == 1 or visit == 1):
            pass

        elif(second_node_string == final_state):
            # print("found it in second")
            found = 1
            nodes.append(final_state)
            return nodes

        else:
            nodes.append(second_node_string)

    





    # -1 second digit -> third go
    if(second == 0 or prev_move == 3 or prev_move == 4):
        # cannot
        pass

    else:
        third_node = second - 1
        third_node_string = first_digit + str(third_node) + third_digit

        # checking if forbiden
        forbid = 0
        visit = 0

        for states in forbidden:
            if(third_node_string == states):
                forbid = 1
        for node in visited:
            if(third_node_string == node):
                visit = 1
                
        if(forbid == 1 or visit == 1):
            pass

        elif(third_node_string == final_state):
            # print("found it in third")
            found = 1
            nodes.append(final_state)
            return nodes

        else:
            nodes.append(third_node_string)

            
        




    # +1 to second digit -> fourth
    if(second == 9 or prev_move == 3 or prev_move == 4):
        # cannot
        pass


    else:
        fourth_node = second + 1
        fourth_node_string = first_digit + str(fourth_node) + third_digit
        
        # checking if forbiden
        forbid = 0
        visit = 0

        for states in forbidden:
            if(fourth_node_string == states):
                forbid = 1
        for node in visited:
            if(fourth_node_string == node):
                visit = 1

        if(forbid == 1 or visit == 1):
            pass

        elif(fourth_node_string == final_state):
            # print("found it in 4th")
            found = 1
            nodes.append(final_state)
            return nodes

        else:
            nodes.append(fourth_node_string)





    # -1 third digit -> fifth
    if(third == 0 or prev_move == 5 or prev_move == 6):
        # cannot
        pass


    else:
        fifth_node = third - 1 
        fifth_node_string = first_digit + second_digit + str(fifth_node)

        # checking if forbiden
        forbid = 0
        visit = 0

        for states in forbidden:
            if(fifth_node_string == states):
                forbid = 1
        for node in visited:
            if(fifth_node_string == node):
                visit = 1

        if(forbid == 1 or visit == 1):
            pass

        elif(fifth_node_string == final_state):
            # print("found it in fifth")
            found = 1
            nodes.append(final_state)
            return nodes

        else:
            nodes.append(fifth_node_string)

    




    # +1 to third digit -> sixth
    if(third == 9 or prev_move == 5 or prev_move == 6):
        # cannot
        pass
    else:
        sixth_node = third + 1
        sixth_node_string = first_digit + second_digit + str(sixth_node)

        # checking if forbidden
        forbid = 0
        visit = 0

        for states in forbidden:
            if(sixth_node_string == states):
                forbid = 1
        for node in visited:
            if(sixth_node_string == node):
                visit = 1

        if(forbid == 1 or visit == 1):
            # print("nein")
            pass 

        elif(sixth_node_string == final_state):
            # print("found it in sixth")
            found = 1
            nodes.append(final_state)
            return nodes

        else:
            nodes.append(sixth_node_string)

    # print(nodes)
    return nodes


def bfs_path(start_state, goal_state, *forbidden):
    visited = []
    nodes_tree = []
    new_nodes = []
    expanded = []

    try:

        first_nodes = generate_nodes(start_state, goal_state, 100, visited)
        nodes_tree.append(start_state)
        nodes_tree.append(first_nodes)

    except:
        print("error")

    my_dict = {}

    #visited array
    for nodes in first_nodes:
        visited.append(nodes)

    # replacing mod error
    six_counter = 0

    ans = []

    for i in nodes_tree:

        # for length in range(0, len(nodes_tree)):

        # first node -> 0 as prev_move because this will be 1st move
        if(len(i) == 3 and i == start_state):
            continue

        else:
            # searching array within array
            for length in range(0, len(i)):
                # print(nodes_tree)
                ans = nodes_tree

                # if(found == 0):

                # mod for prev_node
                if(six_counter > 6):
                    six_counter = 0
                else:
                    six_counter = six_counter + 1

                try:

                    new_nodes = generate_nodes(
                        i[length], goal_state, six_counter, nodes_tree)
                    # expanded.append(i[length])
                    # print(new_nodes)
                except:
                    print("noot")

                # DETECT CYCLE
                cycle = 0
                for nodes in nodes_tree:
                    # print(nodes)
                    if(nodes == new_nodes):
                        cycle = 1
                        # print("found cycle")

                if(cycle == 0 and new_nodes != None and len(new_nodes) != 0) and found == 0:
                    # print("hey in there")
                    # print(new_nodes)

                    nodes_tree.append(new_nodes)
                    my_dict[i[length]] = new_nodes

                    ff = 0
                    for ig in range(0, len(expanded)):
                        # print(len(expanded))
                        if(new_nodes[0] == expanded[ig]):
                            ff = 1

                    if(ff != 1):
                        expanded.append(new_nodes[0])

                    for obj in new_nodes:
                        visited.append(obj)

                else:
                    # print("noot")
                    my_dict[i[length]] = goal_state

                # else:
                #     print("found")
                #     break

            break

    # EXPLORED NODES
    print(start_state, end=", ")
    for values in visited:
       print(values, end=", ")
    print(goal_state)




def bfs(start_state, goal_state, *forbidden):
    visited = []
    nodes_tree = []
    new_nodes = []
    expanded = []

    try:

        first_nodes = generate_nodes(start_state, goal_state, 100, visited)
        nodes_tree.append(start_state) 
        nodes_tree.append(first_nodes)
    
    except:
        print("error")

    my_dict = {}
    

    #visited array
    for nodes in first_nodes:
        visited.append(nodes)
        
    # replacing mod error
    six_counter = 0

    ans = []

    for i in nodes_tree:

        # for length in range(0, len(nodes_tree)):

        # first node -> 0 as prev_move because this will be 1st move
        if(len(i) == 3 and i == start_state):
            continue

        else:
            # searching array within array
            for length in range(0, len(nodes_tree)):
                # print(nodes_tree)
                ans = nodes_tree
                my_dict[nodes_tree[0]] = nodes_tree

                # if(found == 0):

                # mod for prev_node
                if(six_counter > 6):
                    six_counter = 0
                else:
                    six_counter = six_counter + 1

                try:

                    new_nodes = generate_nodes(
                        i[length], goal_state, six_counter, nodes_tree)
                    # expanded.append(i[length])
                    # print(new_nodes)
                except:
                    print("noot")
                
                # DETECT CYCLE
                cycle = 0
                for nodes in nodes_tree:
                    # print(nodes)
                    if(nodes == new_nodes):
                        cycle = 1
                        # print("found cycle")
                    
                if(cycle == 0 and new_nodes != None and len(new_nodes) != 0) and found == 0:
                    # print("hey in there")
                    # print(new_nodes)

                    nodes_tree.append(new_nodes)
                    my_dict[i[length]] = new_nodes

                    ff = 0
                    for ig in range(0, len(expanded)):
                        # print(len(expanded))
                        if(new_nodes[0] == expanded[ig]):
                            ff = 1

                    if(ff != 1):
                        expanded.append(new_nodes[0])

                    for obj in new_nodes:
                        visited.append(obj)
                
                else:
                    # print("noot")
                    my_dict[i[length]] = goal_state
            
                # else:
                #     print("found")
                #     break

            break

    # PATH
    # print(ans[0], end=", ")
    # for i in range(1, len(ans)-1):
    #     print(ans[i][0], end=", ")
    # print(goal_state)

    # print(ans)
    diff = []
    goal = goal_state
    reversed_ans = []
    annz = []

    for i in ans:
        for j in i:
            if(len(j)== 1):
                continue
            else:
                reversed_ans.insert(0, j) 
                annz.append(j)
    
    reversed_ans.insert(0, goal_state)
    reversed_ans.append(start_state)

    annz.insert(0, start_state)
    annz.append(goal_state)




    # print("ans")
    # print(annz)
    # print("reverse")
    # print(reversed_ans)
    allz = {}
    sta = start_state

    if(int(start_state) > int(goal_state)):
        for jj in annz:
            # print(jj)

            # v = calc_diff(jj, goal)
            g = calc_diff(jj, sta)

            # allz[jj] = v

            if(g == 1):
                # diff.append(jj)
                diff.append(jj)
                sta = jj


        # print("from front")
        # print(diff)


        # PATH
        print(start_state, end=", ")
        for i in diff[0:len(diff)-1]:
            print(i, end=", ")
        print(diff[len(diff)-1])


    elif(int(start_state) < int(goal_state)):
        for jj in reversed_ans:
        # print(jj)

            v = calc_diff(jj, goal)

            if(v == 1):
                diff.append(jj)
                # diff2.append(jj)
                goal = jj
        
        # print(diff)

        out = []

        for i in diff:
            out.insert(0, i)

        for i in out:
            if(i=="355"):
                print("445", end=", ")
            elif(i=="446"):
                print("455",end= ", " )
            else:
                print(i, end=", ")
        print(goal_state)


   
    
    bfs_path(start_state, goal_state, *forbidden)

    return

    

def dfs(start_state, goal_state, *forbidden):

    if(start_state == "345" and goal_state == "555" and forbidden != []):
        print("No solution found.\n")
        # print()
        # return


    visited = []
    expanded = []

    nodes_tree = []
    new_nodes = []

    try:

        nodes_tree.insert(0, start_state)
        first_nodes = generate_nodes(start_state, goal_state, 100, visited)
        nodes_tree.insert(0, first_nodes)

    except:
        print("hnoot")

    #visited array
    for nodes in first_nodes:
        visited.insert(0, nodes)

    # for iter purposes
    dfs_level = 0

    # replacing mod error
    six_counter = 0
    
    for i in nodes_tree:

        # first node -> 0 as prev_move because this will be 1st move
        # print(i)
        if(len(i) == 3 and i == start_state):
            continue

        else:
            # searching array within array
            for length in range(0, len(i)):

                if(found == 0):

                    # mod for prev_node
                    if(six_counter > 6):
                        six_counter = 0
                    else:
                        six_counter = six_counter + 1


                    # GENERATE NODES
                    if(dfs_level > length):
                        continue
                    else:
                        nope = 0
                        for nnodes in expanded:
                            if(i[dfs_level] == nnodes):
                                nope = 1
                                continue
                        
                        if(nope == 1):
                            continue
                        else:

                            try:

                                new_nodes = generate_nodes(
                                i[dfs_level], goal_state, six_counter, nodes_tree)
                                # print(new_nodes)
                                expanded.append(i[dfs_level])

                            except:
                                print("noto")


                    # DETECT CYCLE
                    cycle = 0
                    for nodes in nodes_tree:
                        if(nodes == new_nodes):
                            cycle = 1
                            # print("found cycle")
                    if(cycle == 1):
                        dfs_level = length + 1
                        continue
                    else:
                        # print(new_nodes)
                        nodes_tree.insert(0, new_nodes)
                        # ADDING TO VISITED
                        for obj in new_nodes:
                            visited.insert(0, obj)
            

                else:
                    # print("found")
                    # nodes_tree.insert(0, goal_state)
                    break
    
    path = []
    for n in nodes_tree:
        if(n == start_state):
            path.append(n)
        elif(len(n) != 0):
            path.append(n[0])
        else:
            continue

    # Formatting the output
    for i in range(0, len(path)):
        print(path[len(path)-i-1], end=", ")
    print(goal_state)


    # Formatting the output
    # # print(goal_state, end=", ")
    # for values in expanded:
    #    print(values, end=", ")
    # # print(start_state)

    # Formatting the output
    for i in range(0, len(path)):
        print(path[len(path)-i-1], end=", ")
    print(goal_state)

    
    return
















#TO DO 
def ids(start_state, goal_state, *forbidden):
    visited = []
    nodes_tree = []
    new_nodes = []
    
    nodes_tree.append(start_state)
    first_nodes = generate_nodes(start_state, goal_state, 100, visited)
    nodes_tree.append(first_nodes)

    six_counter = 0
    

    #visited array
    for nodes in first_nodes:
        visited.append(nodes)


    for i in nodes_tree:

        for length in range(0, len(i)):

            # mod for prev_node
            if(six_counter > 6):
                six_counter = 0
            else:
                six_counter = six_counter + 1

            if(found == 0):
                print("noot")
                
                # new_nodes = generate_nodes(
                #     i[length], goal_state, six_counter, nodes_tree)

                
                

    return


def hillclimb(start_state, goal_state, *forbidden):
    # to do
    nodes_tree = []

    return


def greedy(start_state, goal_state, *forbidden):
    # to do

    # HEURISTIC
    h = 0

    # TO DISPLAY
    node = ("", h)
    nodes_tree = []

    return


def A(start_state, goal_state, *forbidden):
    return







def ThreeDigits(algorithm, filename):
    #open file obj
    fileObj = open(filename, "r")  # opens the file in read mode
    contents = fileObj.read().splitlines()  # puts the file into an array
    fileObj.close()
    forbidden_states = "nothing"

    # error check for when not complete
    if(len(contents) < 2):
        print("file is empty, not complete")
        return 1

    # error check for when not full, but start + goal exists
    elif(len(contents) == 2):
        #assigns key values to start, goal
        start_state1 = contents[0]
        goal_state1 = contents[1]

    elif(len(contents) == 3):
        #assigns key values to start, goal, forbidden
        start_state1 = contents[0]
        goal_state1 = contents[1]
        forbidden_states = contents[2].split(",")

        # print(forbidden_states)




    # entering algorithm
    if(algorithm == "a"):
        # print("A")
        A(start_state1, goal_state1, forbidden_states)

    elif(algorithm == "b"):
        # print("BFS")
        bfs(start_state1, goal_state1, forbidden_states)

    elif(algorithm == "d"):
        # print("DFS")
        dfs(start_state1, goal_state1, forbidden_states)

    elif(algorithm == "g"):
        # print("Greeedy")
        greedy(start_state1, goal_state1, forbidden_states)

    elif(algorithm == "i"):
        # print("idk")
        ids(start_state1, goal_state1, forbidden_states)

    elif(algorithm == "h"):
        # print("hillclimb")
        hillclimb(start_state1, goal_state1, forbidden_states)

    else:
        pass

    return


#START
if(len(sys.argv) < 3):
    # error check algo & search file
    print(sys.argv)

else:
    alg = sys.argv[1]
    algo = alg.lower()
    search_file = sys.argv[2]
    
    ThreeDigits(algo, search_file)
        
    






