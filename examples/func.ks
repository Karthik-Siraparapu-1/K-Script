print:'--- FUNCTION TEST ---'

# 1. Define a simple greeting function
def: greet do:
    print:'Hello from the K Script!'
    
# 2. Define a math helper function
# Note: Functions in K-Script use global variables
def: double_x do:
    x = x * 2
    print:'Doubled X is now:'
    print:x

# --- MAIN PROGRAM ---
x = 5

print:'1. Running Greet Function:'
run: greet

print:' '
print:'2. Testing Variable Scope:'
print:'Original X is:'
print:x

run: double_x
run: double_x

print:' '
print:'--- END OF TEST ---'