import networkx as nx
import os

###########################################
# Change this variable to the path to 
# the folder containing all three input
# size category folders
###########################################
path_to_inputs = "./inputs"

###########################################
# Change this variable if you want
# your outputs to be put in a 
# different folder
###########################################
path_to_outputs = "./outputs"

def parse_input(folder_name):
    '''
        Parses an input and returns the corresponding graph and parameters

        Inputs:
            folder_name - a string representing the path to the input folder

        Outputs:
            (graph, num_buses, size_bus, constraints)
            graph - the graph as a NetworkX object
            num_buses - an integer representing the number of buses you can allocate to
            size_buses - an integer representing the number of students that can fit on a bus
            constraints - a list where each element is a list vertices which represents a single rowdy group
    '''
    graph = nx.read_gml(folder_name + "/graph.gml")
    parameters = open(folder_name + "/parameters.txt")
    num_buses = int(parameters.readline())
    size_bus = int(parameters.readline())
    constraints = []
    
    for line in parameters:
        line = line[1: -2]
        curr_constraint = [num.replace("'", "") for num in line.split(", ")]
        constraints.append(curr_constraint)
    return graph, num_buses, size_bus, constraints


def solve(graph, num_buses, size_bus, constraints):
    nodes = list(graph.nodes)

    bus_assignment = []
    for i in range(num_buses):
        bus_assignment.append([])
 
    for node in nodes:
        rowdy = True
        for bus in bus_assignment:
            if not len(bus) < size_bus:
                continue
            for i in range(len(constraints)):
                rowdy =  all(elem in (bus + [node]) for elem in constraints[i])
                if rowdy == False:
                    bus.append(node)
                    break
            if rowdy == False:
                break
    output = ""
    for i in range(num_buses):
        output += str(bus_assignment[i]) + '\n'
    return output

def main():
    '''
        Main method which iterates over all inputs and calls `solve` on each.
        The student should modify `solve` to return their solution and modify
        the portion which writes it to a file to make sure their output is
        formatted correctly.
    '''
    size_categories = ["small", "medium", "large"]
    if not os.path.isdir(path_to_outputs):
        os.mkdir(path_to_outputs)

    for size in size_categories:
        category_path = path_to_inputs + "/" + size
        output_category_path = path_to_outputs + "/" + size
        category_dir = os.fsencode(category_path)

        for input_folder in os.listdir(category_dir):
            input_name = os.fsdecode(input_folder)
            graph, num_buses, size_bus, constraints = parse_input(category_path)
            solution = solve(graph, num_buses, size_bus, constraints)
            output_file = open(output_category_path + ".out", "w") 
            output_file.write(solution)

            output_file.close()

if __name__ == '__main__':
    main()
