print:'--- K-Script Calculator ---'

def: add_func do:
    res = n1 + n2
    print:'Result:'
    print:res

def: sub_func do:
    res = n1 - n2
    print:'Result:'
    print:res

running = 1

loop: running = 1 do:
    print:' '
    print:'1. Add'
    print:'2. Subtract'
    print:'3. Exit'
    choice = input:'Select Option:'
    
    if: choice = 3 do:
        print:'Goodbye'
        running = 0
    
    if: choice < 3 do:
        n1 = input:'First Number:'
        n2 = input:'Second Number:'
        
        if: choice = 1 do:
            run: add_func
        if: choice = 2 do:
            run: sub_func