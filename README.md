# Data Engineering task

Problem => We need to represent implicit dependencies between database tables
Solution => represent it as a directed graph where the table is the vertex itself
and its dependencies is the adjacency list ()

#### Python version (3.7.3)

### To compile and execute the script

#### Note: Add the tables folder under the data directory (folder) then run the following commands from the terminal

```
git clone https://github.com/AmiraDowidar/data-challenge.git
cd data-challege
chmod ugo+x run_script.sh
./run_script.sh
```

### If problem occured with python for matplotlib (Mac OSX), Run the following commands from the terminal

```
touch ~/.matplotlib/matplotlibrc
echo "backend: TkAgg" >> ~/.matplotlib/matplotlibrc
```

### Libraries used:
- glob
- json
- re
- networkx
- matplotlib.pyplot

### Validated regex using Pythex and Regex as references
https://pythex.org/
https://regexr.com/