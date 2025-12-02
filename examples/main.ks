print:'--- K-SCRIPT MAIN MENU ---'

# 1. Define a helper function
def: greet_user do:
    print:'Hello! Welcome to the K-Script environment.'
    print:'This language was built by Siraparapu.karthik.'

# 2. Setup variables
running = 1
name = input:'First, what is your name?'

print:'Welcome,'
print:name

# 3. Start the application loop
loop: running = 1 do:
    print:' '
    print:'--- SELECT AN OPTION ---'
    print:'1. View System Info'
    print:'2. Count to 5'
    print:'3. Exit'
    
    choice = input:'Enter choice (1-3):'
    
    # Option 1: Run a function
    if: choice = 1 do:
        run: greet_user
        
    # Option 2: Run a loop inside a loop
    if: choice = 2 do:
        print:'Counting...'
        c = 1
        loop: c < 6 do:
            print:c
            c = c + 1
            
    # Option 3: Logic to break the loop
    if: choice = 3 do:
        print:'Goodbye!'
        running = 0