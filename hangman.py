import random
def hangman(word):
    wrong = 0
    stages = ["",
              "_____",
              "|   |",
              "|   0",
              "|  /|\ ",
              "|  / \ ",
              "|"]
    valid_characters = "abcdefghijklmnopqrstuvwxyz"
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "１文字を予想してね"
        while True:
            char = input(msg)
            if len(char) != 1:
                print("一文字だけ入力してください")
            elif char not in valid_characters:
                print("英字を入れてください")
            else:
                break
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        print("\n".join(stages[:wrong + 1]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("You lose!")
        print("正解は{}".format(word))

answer_list = ["apple", "acorn", "death", "greet", "train", "night"]
hangman(answer_list[random.randint(0, len(answer_list) - 1)])
