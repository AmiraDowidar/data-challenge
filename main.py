import glob, json, re
import networkx as nx
import matplotlib.pyplot as plt


# Change this if you added the tables folder into a different directory
TABLES_DIR  = 'data/tables/'

# Retrieve all files in the directory
files_list = glob.glob('{}*.json'.format(TABLES_DIR))

# Define a dictionary to store the graph { vertex : [adjacency,  list]}
tables_dict = dict()

# Loop through the files list, open the file and load json data
for file_path in files_list:
    with open(file_path) as f:
        try:
            data = json.load(f)
            
            vertex_name = re.search('{}(.+?).json'.format(TABLES_DIR), file_path).group(1)
            #vertex_name ='{}.{}'.format(data['schema']['S'],data['table']['S'])

            # Get from clause part of the query using regex
            processed_data = str(data).replace('"', "'")
            from_query=re.search(r'\'from\': {*\'S\'*:\s*\'(.+?)\'*},', processed_data).group(1)
            split_query = from_query.strip().split(' ')
            
            # Get from clause part of the query using dictionary indices
            # from_query = data['query']['L'][0]['M']['from']['S'] \
            #     if 'L' in data['query'] else data['query']['M']['from']['S']
            # split_query = from_query.strip().split(' ')

            # Initialize an empty list and add the first item in the query 
            # as it's a dependency and the table names after the join clause
            adjacency_list = [ split_query[i] for i in range(len(split_query)) if i == 0 or 'join'==split_query[i-1] ] 

            # Remove duplicates (self-join) from list and sort list alphabetically
            adjacency_list = sorted(list(set(adjacency_list)))
            
            # Add the data to the dictionary
            tables_dict[vertex_name] = adjacency_list
        except AttributeError:
            print("Not a valid table name or no from clause in the file: "+ file_path)

# Populate the directed graph from the dictionary
G=nx.DiGraph(tables_dict)
nx.draw(G)
plt.show()
