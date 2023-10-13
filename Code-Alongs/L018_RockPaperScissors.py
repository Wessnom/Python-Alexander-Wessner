# Cap letters signify constant that will not be changed, i.e Global variable
SIGNS = ["rock", "paper", "scissors"]

def main():
    print(f"Welcome to the {', '.join(SIGNS)} game! ")
    print_rules()
    

def print_rules():
    print("\nThese are the RULES: Each player picks a sign:")
    for winner, loser in zip([0, 1, 2], [2, 0, 1]):
        print(f"{winner} wins over {loser}. ")




main()