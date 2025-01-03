def display_rule110(initial_state, num_rows) -> None:
    for x in range(num_rows): #Iterates through the desired number of rows that we want to display 
        row_string = '' #initializes an empty string that will represent the row 
        for cell in initial_state: #Iterates through the each cell of the specified row
            if cell == '1': #if there is an alive cell detected then display a box figuere 
                row_string += '█'
            else: #If there was no alive cell detected then display an empty character
                row_string += ' ' 
        print(row_string) #After interating though the each cell of the specified row and displaying a box for alive cell and empty string for dead cell print the row 
        next_row = '' #Initializes a string that will get us the next row based on the previous row 
        for i in range(len(initial_state)): #Iterates through each cell in the previous row
            if i > 0: #If the cell is alive then save the alive cell as our left sequence
                left = initial_state[i - 1]  
            else: 
                left = '0' #If the cell is not alive then assign our left sequence to be 0
            center = initial_state[i] #Chooses the center of the sequence as middle 
            if i < len(initial_state) - 1: #Checks to make sure that the we are in range until withing the last cell of the row and assign it as right 
                right = initial_state[i + 1] #Assigns the right cell 
            else:
                right = '0' #If we are out of range then assign it as a dead cell 
            next_row += apply_rule(left + center + right) #Calls apply rule to function to determine if the cell is alive or dead based on the sequence retrieved 
        initial_state = next_row #Assigns our next row to the initial row so it can be accessed for the next row iteration 

def apply_rule(pattern) -> str: #This function will return a living or dead cell based on the iteration table found on the rule 110 website 
    iteration_table = {'111': '0', '110': '1', '101': '1', '100': '0', '011': '1', '010': '1', '001': '1', '000': '0'} #Stored the iteration of the table in a dictionary as key value pairs that will output a 1 (alive) or 0 (dead) based on table sequence
    return iteration_table[pattern] #returns the associated value cell (dead or alive) based on the iteration sequence

initial_state = '0' * 99 + '1' #Our initial state begins with an alive cell the reason for adding the 0's is to move the cell down so it can been in the shell
num_rows = 100 #The number of rows that we print/display the cellular automation 

display_rule110(initial_state, num_rows) #Calls the function of rule 110 with the desired number or rows and our initial first alive cell 