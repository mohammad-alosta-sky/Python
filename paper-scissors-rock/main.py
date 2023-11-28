import random

psr = ["Paper", "Scissors", "Rock"]


def pc_player():
    return psr[random.randint(0,2)]


def winner(player):
    pc = pc_player()

    print(f"You: {player} vs Pc: {pc}")
    if pc == player:
        return "Draw!"
    elif (player == "Paper" and pc == "Rock") or (player == "Rock" and pc == "Scissors") or (player == "Scissors" and pc == "Paper"):
        return "You Won!"
    else:
        return "You Lost!"



def main():
    print(" 1-Paper \n 2-Scissors \n 3-Rock")
    player = int(input("Please enter 1, 2 or 3: ")) - 1
    if player > 2:
        print("Invalid input!")
        exit()
    score = winner(psr[player])
    print(score)

    
if __name__ == "__main__":
    main()