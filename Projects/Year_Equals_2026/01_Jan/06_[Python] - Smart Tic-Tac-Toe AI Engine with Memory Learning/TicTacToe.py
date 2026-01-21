def checkBoard(brd):
    if len(brd) != 3:
        print("Number of rows: " + str(len(brd)) + ", Make to 3!")
        return False
    for rowi in range(len(brd)):
        if len(brd[rowi]) != 3: 
            print("Number of columns: " + str(len(brd[rowi])) + ", Make to 3!")
            return False
    for row in range(len(brd)):
        for col in range(len(brd[row])):
            if not (brd[row][col] == "x" or brd[row][col] == "o" or str(brd[row][col]) in "123456789"):
                print("Unexpected data Exists | " + str(brd[row][col]))
                return False
    return True

def checkFilled(brd, pyr_sign, opo_sign):
    if not checkBoard(brd): return False
    for row in range(len(brd)):
        for col in range(len(brd[0])):
            if (brd[row][col] != pyr_sign and brd[row][col] != opo_sign): return False
    # print("Filled:", brd)
    return True

def scoreBoard(your_won_times = 0, oppo_won_times = 0, draws = 0, rounds = 0):
    # if not checkBoard(brd): return False
    print("\n" + 2 * "=====" + "=")
    print("Score Board\t\t")
    print(2 * "-----" + "-")
    print(f"You Won({your_won_times}/{rounds}).\nOpponent Won({oppo_won_times}/{rounds}).")
    print(f"Draws({draws})")
    print(2 * "=====" + "=\n")

def winCondition(brd, sign):
    if not checkBoard(brd): return False
    for ar in brd:
        if ar.count(sign) == 3: return True
    for c in range(len(brd[0])):
        if (brd[0][c] == sign and brd[1][c] == sign and brd[2][c] == sign): return True
    if (brd[0][0] == sign and brd[1][1] == sign and brd[2][2] == sign): return True
    if (brd[0][2] == sign and brd[1][1] == sign and brd[2][0] == sign): return True
    return False

def update_board(brd, cord, sign):
    if not isinstance(brd, list):
        print("Provide list of dimension (3, 3) | " + str(brd))
        return brd, False
    if not isinstance(sign, str): 
        print("Provide String | " + str(sign))
        return brd, False 
    if not isinstance(cord, int):
        print("Provide Integer | " + str(cord))
        return brd, False
    if sign != "x" and sign != "o":
        print("[Choose x or o] - " + str(sign))
        return brd, False
    if not (cord > 0 and cord < 10):
        print("[Choose 1 - 9] - " + str(cord))
        return brd, False
    opo_sign = "o" if sign == "x" else "x"
    if checkFilled(brd, sign, opo_sign): return brd, False
    old_brd = [brd[r] for r in range(len(brd))]
    for row in range(len(brd)):
        for col in range(len(brd[row])):
            if brd[row][col] == cord and str(brd[row][col]) != sign and str(brd[row][col]) != opo_sign:
                brd[row][col] = sign
                return brd, True
    print("Sign exists at " + str(cord))
    return brd, False

# any one starts first
# if one cord is not provided meaning matrix has one vacant space to fill
def run_step(brd, pyr_cord = -1, opo_cord = -1, pyr_sign = "", opo_sign = ""):    
    if (pyr_sign != "x" and pyr_sign != "o" and pyr_sign != ""):
        print("Invalid Player sign | " + str(pyr_sign))
        return brd, "Invalid Player sign"
    if (opo_sign != "x" and opo_sign != "o" and opo_sign != ""):
        print("Invalid Opponent sign | " + str(opo_sign))
        return brd, "Invalid Opponent sign"
    if (pyr_sign == opo_sign):
        print("Player sign and Opponent sign must be different!")
        return brd, "Sign must be different!"
    
    cords = []
    for row in range(len(brd)):
        for col in range(len(brd[row])):
            if (brd[row][col] != pyr_sign and brd[row][col] != opo_sign):
                cords.append(brd[row][col])
    if (pyr_cord not in cords and pyr_cord != -1):
        print(f"Don't Choose: {pyr_cord}, Choose player Cordinate: {cords}.")
        return brd, cords
    if (opo_cord not in cords and opo_cord != -1):
        print(f"Don't Choose: {opo_cord}, Choose Opponent cordinate: {cords}.")
        return brd, cords
    if (pyr_cord == -1 and opo_cord in cords):
        brd, isupdated = update_board(brd, opo_cord, opo_sign)
        if (isupdated): cords.remove(opo_cord)
        return brd, isupdated
    if (opo_cord == -1 and pyr_cord in cords):
        # print("updated")
        brd, isupdated = update_board(brd, pyr_cord, pyr_sign)
        if (isupdated): cords.remove(pyr_cord)
        return brd, isupdated

    # print(f"You choose({pyr_sign}): {str(pyr_cord)}.\nCordinates: {cords}.")
    isupdated = 0
    if (len(cords) > 1):
        brd, isupdated = update_board(brd, pyr_cord, pyr_sign)
        if (isupdated): cords.remove(pyr_cord)
        brd, isupdated = update_board(brd, opo_cord, opo_sign)
        if (isupdated): cords.remove(opo_cord)
        # print(cords)
        return brd, isupdated

def check_instances(brd, your_won_times = 0, oppo_won_times = 0, draws = 0, rounds = 1):
    if not isinstance(your_won_times, int):
        print("Provide Integer(your_won_times) | " + str(your_won_times))
        return brd, "Provide Integer"
    elif(your_won_times < 0):
        print("Provide Positive Integer(your_won_times) | " + str(your_won_times))
        return brd, "Provide Positive Integer"

    if not isinstance(oppo_won_times, int):
        print("Provide Integer(oppo_won_times) | " + str(oppo_won_times))
        return brd, "Provide Integer"
    elif(oppo_won_times < 0):
        print("Provide Positive Integer(oppo_won_times) | " + str(oppo_won_times))
        return brd, "Provide Positive Integer"

    if not isinstance(draws, int):
        print("Provide Integer(draws) | " + str(draws))
        return brd, "Provide Integer"
    elif(draws < 0):
        print("Provide Positive Integer(draws) | " + str(draws))
        return brd, "Provide Positive Integer"

    if not isinstance(rounds, int):
        print("Provide Integer(rounds) | " + str(rounds))
        return brd, "Provide Integer"
    elif(rounds < 0):
        print("Provide Positive Integer(rounds) | " + str(rounds))
        return brd, "Provide Positive Integer"
    return brd, ""

def save_memory(strplyr, stroppo):
    import os
    file_path = "memory.txt"
    if not os.path.exists(file_path):
        open(file_path, "w").close()
        # print("File created")
        with open(file_path, "a") as f:
            f.write(strplyr + "\n")
            f.write(stroppo + "\n")
    else:
        with open(file_path, "a") as f:
            f.write(strplyr + "\n")
            f.write(stroppo + "\n")

def opo_mind(strplyr, cords):
    if len(cords) == 0:
        print("Given empty cords:", cords)
        return -1, cords
    if not isinstance(strplyr, str):
        print("Provide String (strplyr) | " + str(strplyr))
        return -1, cords
    if not strplyr.isdigit() and strplyr != "":
        print(f"{strplyr} contains non-digit.")
        return -1, cords
    import os
    import random
    file_path = "memory.txt"
    if strplyr == "" and len(cords) != 0:
        # index = random.randint(0, len(cords) - 1)
        # opo_cord = cords[index]
        # cords.remove(opo_cord)
        # return opo_cord, cords
        if os.path.exists(file_path):
            # print("File does exist")
            with open(file_path, "r") as f:
                content = f.read()
                arr = content.split("\n")[:-1]
                least_int = -1
                for i in range(0, len(arr), 2):
                    win = arr[i]
                    if len(str(win)) == 3 and int(str(win[0])) in cords:
                        print("win: " + str(win))
                        least_int = int(str(win[0]))
                        break
                    elif int(str(win[0])) in cords:
                        least_int = int(str(win[0]))
                if (least_int != -1):
                    cords.remove(least_int)
                    return least_int, cords

    if os.path.exists(file_path):
        # print("File does exist")
        with open(file_path, "r") as f:
            content = f.read()
            arr = content.split("\n")
            # print(arr)
            for i in range(0, len(arr), 2):
                if i + 1 >= len(arr): break 
                win, fail = arr[i], arr[i + 1]
                if (fail.find(strplyr) == 0 or win.find(strplyr) == 0):
                    if int(str(win)[len(strplyr)]) in cords: 
                        cords.remove(int(str(win)[len(strplyr)]))
                        return int(str(win)[len(strplyr)]), cords
    
    index = random.randint(0, len(cords) - 1)
    opo_cord = cords[index]
    cords.remove(opo_cord)
    return opo_cord, cords

def run_round_odd(your_won_times = 0, oppo_won_times = 0, draws = 0, rounds = 1):  
    print(f"...Round {rounds} begins...")
    brd = [
        [1, 2, 3], 
        [4, 5, 6],
        [7, 8, 9]
    ]
    brd, msg = check_instances(brd, your_won_times = 0, oppo_won_times = 0, draws = 0, rounds = 1)
    if (rounds == 1):
        print("\nWin Conditions")
        print(len("Win Conditions") * "=")
        print(f"Given Board:\n{brd[0]}\n{brd[1]}\n{brd[2]}")
        print("Choose Cordinates:\n(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9),\n(1, 4, 7), (2, 5, 8), (3, 6, 9) and (3, 5 ,7).")
    
    strplyr, stroppo = "", ""
    
    pyr_sign = input("\nChoose Sign(x/o): ")
    while(pyr_sign != "x" and pyr_sign != "o"):
        pyr_sign = input("Choose Sign(x/o): ")
    opo_sign = "o" if pyr_sign == "x" else "x"
    print(f"\nYou Choose: {pyr_sign}.\nOpponent Choose: {opo_sign}.")

    step, pyr_cord, opo_cord = 1, -1, -1
    while (step <= 4):
        cords = [num for row in range(len(brd)) for num in brd[row] if num !="x" and num != "o"]
        print(f"\nGiven Board:\n{brd[0]}\n{brd[1]}\n{brd[2]}")
        while (pyr_cord not in cords):
            try:
                pyr_cord = int(input("Enter Cordinate: "))
                if (pyr_cord not in cords): raise Exception(cords)

                strplyr += str(pyr_cord)

            except Exception as e:
                print("Choose codinates:", cords)
        cords.remove(pyr_cord)

        # import random
        # index = random.randint(0, len(cords) - 1)
        # opo_cord = cords[index]
        opo_cord, cords = opo_mind(strplyr, cords)

        stroppo += str(opo_cord)

        # cords.remove(opo_cord)
        print(f"Opponent's Cordinate: {opo_cord}.")

        brd, isupdated = run_step(brd, pyr_cord, opo_cord, pyr_sign, opo_sign)
        # if (isupdated): 
        #     print(brd)
        # print(pyr_cord, opo_cord)
        # print(f"Remaining Cordinates: {cords}.")
        pyr_cord, opo_cord = -1, -1
        step += 2

    
    while (step > 4 and step <= 9):
        cords = [num for row in range(len(brd)) for num in brd[row] if num !="x" and num != "o"]
        print(f"\nGiven Board:\n{brd[0]}\n{brd[1]}\n{brd[2]}")
        while (pyr_cord not in cords):
            try:
                pyr_cord = int(input("Enter Cordinate: "))
                if (pyr_cord not in cords): raise Exception(cords)

                strplyr += str(pyr_cord)

            except Exception as e:
                print("Choose codinates:", cords)
        cords.remove(pyr_cord)

        brd, isupdated = run_step(brd = brd, pyr_cord = pyr_cord, pyr_sign = pyr_sign)

        pyr_won = winCondition(brd, pyr_sign)
        if pyr_won:
            your_won_times += 1
            rounds += 1
            save_memory(strplyr, stroppo)
            return your_won_times, oppo_won_times, draws, rounds
        is_filled = checkFilled(brd, pyr_sign, opo_sign)
        if is_filled:
            draws += 1
            rounds += 1
            return your_won_times, oppo_won_times, draws, rounds
        
        # import random
        # index = random.randint(0, len(cords) - 1)
        # opo_cord = cords[index]
        opo_cord, cords = opo_mind(strplyr, cords)

        stroppo += str(opo_cord)

        # cords.remove(opo_cord)
        print(f"Opponent's Cordinate: {opo_cord}.")

        brd, isupdated = run_step(brd, opo_cord = opo_cord, opo_sign = opo_sign)

        opo_won = winCondition(brd, opo_sign)
        if opo_won:
            oppo_won_times += 1
            rounds += 1
            save_memory(stroppo, strplyr)
            return your_won_times, oppo_won_times, draws, rounds
        is_filled = checkFilled(brd, pyr_sign, opo_sign)
        if is_filled:
            draws += 1
            rounds += 1
            return your_won_times, oppo_won_times, draws, rounds

        # if (isupdated): print(brd)
        # print(pyr_cord, opo_cord)
        # print(f"Remaining Cordinates: {cords}.")
        pyr_cord, opo_cord = -1, -1
        step += 1

def run_round_even(your_won_times = 0, oppo_won_times = 0, draws = 0, rounds = 2):  
    print(f"...Round {rounds} begins...")
    brd = [
        [1, 2, 3], 
        [4, 5, 6],
        [7, 8, 9]
    ]

    brd, msg = check_instances(brd, your_won_times = 0, oppo_won_times = 0, draws = 0, rounds = 1)

    strplyr, stroppo = "", ""

    import random
    signs = ["x", "o"]
    pyr_sign = signs[random.randint(0, len(signs) - 1)]
    opo_sign = "x" if pyr_sign == "o" else "o"
    print(f"\nOpponent Choose: {opo_sign}.\nYou Choose: {pyr_sign}.")

    step, pyr_cord, opo_cord = 1, -1, -1
    while (step <= 4):
        cords = [num for row in range(len(brd)) for num in brd[row] if num !="x" and num != "o"]
        # print(f"\nGiven Board:\n{brd[0]}\n{brd[1]}\n{brd[2]}")
        
        # import random
        # index = random.randint(0, len(cords) - 1)
        # opo_cord = cords[index]
        opo_cord, cords = opo_mind(strplyr, cords)

        stroppo += str(opo_cord)

        # cords.remove(opo_cord)
        print(f"\nOpponent's Cordinate: {opo_cord}.")
        # print(f"\nGiven Board:\n{brd[0]}\n{brd[1]}\n{brd[2]}")
        dup_brd = []
        for row in range(len(brd)):
            row_ = []
            for col in range(len(brd[row])):
                if brd[row][col] == opo_cord: row_.append(opo_sign)
                else: row_.append(brd[row][col])
            dup_brd.append(row_)
            
        print(f"Given Board:\n{dup_brd[0]}\n{dup_brd[1]}\n{dup_brd[2]}")
        # print(brd)
        while (pyr_cord not in cords):
            try:
                pyr_cord = int(input("Enter Cordinate: "))
                if (pyr_cord not in cords): raise Exception(cords)

                strplyr += str(pyr_cord)

            except Exception as e:
                print("Choose codinates:", cords)
        cords.remove(pyr_cord)

        brd, isupdated = run_step(brd, pyr_cord, opo_cord, pyr_sign, opo_sign)
        # if (isupdated): 
        #     print(brd)
        # print(pyr_cord, opo_cord)
        # print(f"Remaining Cordinates: {cords}.")
        pyr_cord, opo_cord = -1, -1
        step += 2

    
    while (step > 4 and step <= 9):
        cords = [num for row in range(len(brd)) for num in brd[row] if num !="x" and num != "o"]
        # print(f"\nGiven Board:\n{brd[0]}\n{brd[1]}\n{brd[2]}")
        
        # import random
        # index = random.randint(0, len(cords) - 1)
        # opo_cord = cords[index]
        opo_cord, cords = opo_mind(strplyr, cords)

        stroppo += str(opo_cord)

        # cords.remove(opo_cord)
        print(f"\nOpponent's Cordinate: {opo_cord}.")

        brd, isupdated = run_step(brd, opo_cord = opo_cord, opo_sign = opo_sign)
        print(f"Given Board:\n{brd[0]}\n{brd[1]}\n{brd[2]}")

        opo_won = winCondition(brd, opo_sign)
        if opo_won:
            oppo_won_times += 1
            rounds += 1
            save_memory(stroppo, strplyr)
            return your_won_times, oppo_won_times, draws, rounds
        is_filled = checkFilled(brd, pyr_sign, opo_sign)
        if is_filled:
            draws += 1
            rounds += 1
            return your_won_times, oppo_won_times, draws, rounds

        while (pyr_cord not in cords):
            try:
                pyr_cord = int(input("Enter Cordinate: "))
                if (pyr_cord not in cords): raise Exception(cords)

                strplyr += str(pyr_cord)

            except Exception as e:
                print("Choose codinates:", cords)
        cords.remove(pyr_cord)

        brd, isupdated = run_step(brd = brd, pyr_cord = pyr_cord, pyr_sign = pyr_sign)

        pyr_won = winCondition(brd, pyr_sign)
        if pyr_won:
            your_won_times += 1
            rounds += 1
            save_memory(strplyr, stroppo)
            return your_won_times, oppo_won_times, draws, rounds
        is_filled = checkFilled(brd, pyr_sign, opo_sign)
        if is_filled:
            draws += 1
            rounds += 1
            return your_won_times, oppo_won_times, draws, rounds

        # if (isupdated): print(brd)
        # print(pyr_cord, opo_cord)
        # print(f"Remaining Cordinates: {cords}.")
        pyr_cord, opo_cord = -1, -1
        step += 1

quit = False
your_won_times, oppo_won_times, draws, rounds = 0, 0, 0, 1
while (not quit):
    if (rounds % 2 != 0):
        your_won_times, oppo_won_times, draws, rounds = run_round_odd(your_won_times, oppo_won_times, draws, rounds)
    else:
        your_won_times, oppo_won_times, draws, rounds = run_round_even(your_won_times, oppo_won_times, draws, rounds)
    scoreBoard(your_won_times, oppo_won_times, draws, rounds - 1)
    quits = input("Want to Quit(q): ")
    if (quits == "q"): quit = True