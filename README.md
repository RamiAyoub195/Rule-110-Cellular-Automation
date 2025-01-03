# Rule 110 Cellular Automaton

This project implements Rule 110, a one-dimensional cellular automaton, in Python. Rule 110 is renowned for its computational complexity and ability to exhibit intricate patterns despite its simplicity. This implementation displays the evolution of Rule 110 as a grid in the terminal.

## Features
Text-based visualization: Displays the evolution of Rule 110 as rows of alive (█) and dead ( ) cells.
Customizable parameters: Easily adjust the number of rows and the initial state.
Minimal dependencies: Runs in any Python 3.x environment with no additional libraries.

## How It Works
Initial State: The automaton starts with a single alive cell (1) surrounded by dead cells (0).
Transition Rules: The state of each cell in the next row is determined by its current state and the states of its immediate neighbors:

## Based on the Rule 110 iteration table:
111 → 0
110 → 1
101 → 1
100 → 0
011 → 1
010 → 1
001 → 1
000 → 0

## Evolution: 
The automaton iterates through the specified number of rows, updating the state of each cell according to the rules.
Code Overview
The project consists of two main functions:

display_rule110(initial_state, num_rows): Simulates and displays the evolution of Rule 110 in the terminal.
apply_rule(pattern): Determines the next state of a cell based on its current state and neighbors.

## Usage
Prerequisites
Python 3.x installed on your system.

## Running the Program
Copy the code into a file named rule110.py.
Customize the parameters:
initial_state: The starting state of the automaton (default: a single alive cell surrounded by dead cells).
num_rows: The number of rows to display (default: 100).

## Run the script:
bash
Copy code
python rule110.py
Example Output
The output will resemble the following:

                                        █                                        
                                       █ █                                       
                                      █   █                                      
                                     █ █ █ █                                     
                                    █       █                                    
                                   █ █     █ █                                   
                                  █   █   █   █                                  
                                 █ █ █ █ █ █ █ █                                 
                                █               █                 
                               █ █             █ █                
                               
## Customization
Initial State: Modify the initial_state variable to define a custom starting configuration.
Number of Rows: Adjust num_rows to change how many rows are displayed.

## License
This project is provided under the MIT License. Feel free to modify and distribute as needed.


