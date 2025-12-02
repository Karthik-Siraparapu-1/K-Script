print:'--- Guess the Number (1-10) ---'
secret = 7
guess = 0

loop: guess < secret do:
    guess = input:'Enter guess:'
    
    if: guess = secret do:
        print:'YOU WIN!'
    
    if: guess > secret do:
        print:'Too High'

    if: guess < secret do:
        print:'Too Low'