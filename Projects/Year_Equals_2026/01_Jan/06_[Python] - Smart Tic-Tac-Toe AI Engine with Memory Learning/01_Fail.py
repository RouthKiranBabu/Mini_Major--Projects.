import os
def chooseSign():
    playerSign = ""
    while (playerSign != "o" and playerSign != "x"):
        playerSign = input("Choose your sign(x or o): ")
    aiSign = "o" if (playerSign == "x") else "x"
    return playerSign, aiSign

def checkBoard(brd):
    if len(brd) != 3:
        print("Number of rows: " + str(len(brd)) + ", Make to 3!")
        return False
    for rowi in range(len(brd)):
        if len(brd[rowi]) != 3: 
            print("Number of columns: " + str(len(brd[rowi])) + ", Make to 3!")
            return False
    return True

def checkFilled(brd, pyr_sign, opo_sign):
    # print(checkFilled(brd, "x", "o"))
    if not checkBoard(brd): return False
    for row in range(len(brd)):
        for col in range(len(brd[0])):
            if (brd[row][col] != pyr_sign and brd[row][col] != opo_sign): return False
    return True

def winCondition(brd, sign):
    # print(winCondition("x", brd))
    if not checkBoard(brd): return False
    for ar in brd:
        if ar.count(sign) == 3: return True
    for c in range(len(brd[0])):
        if (brd[0][c] == sign and brd[1][c] == sign and brd[2][c] == sign): return True
    if (brd[0][0] == sign and brd[1][1] == sign and brd[2][2] == sign): return True
    if (brd[0][2] == sign and brd[1][1] == sign and brd[2][0] == sign): return True
    return False

def scoreBoard(your_won_times = 0, oppo_won_times = 0, draws = 0, rounds = 0):
    if not checkBoard(brd): return False
    print("\n" + 2 * "=====" + "=")
    print("Score Board\t\t")
    print(2 * "-----" + "-")
    print(f"You Won({your_won_times}/{rounds}).\nOpponent Won({oppo_won_times}/{rounds}).")
    print(f"Draws({draws})")
    print(2 * "=====" + "=\n")

def mirrorTransposes(str_pyr, str_opo):
    pyr1, pyr2, pyr3, pyr4, pyr5, pyr6, pyr7 = "", "", "", "", "", "", ""
    for c in str_pyr:
        if c == "1": 
            pyr1 += "3"
            pyr2 += "7"
            pyr3 += "9"
            pyr4 += "1"
            pyr5 += "3"
            pyr6 += "7"
            pyr7 += "9"
        elif c == "2": 
            pyr1 += "2"
            pyr2 += "8"
            pyr3 += "8"
            pyr4 += "4"
            pyr5 += "6"
            pyr6 += "4"
            pyr7 += "6"
        elif c == "3": 
            pyr1 += "1"
            pyr2 += "9"
            pyr3 += "7"
            pyr4 += "7"
            pyr5 += "9"
            pyr6 += "1"
            pyr7 += "3"
        elif c == "4": 
            pyr1 += "6"
            pyr2 += "4"
            pyr3 += "6"
            pyr4 += "2"
            pyr5 += "2"
            pyr6 += "8"
            pyr7 += "8"
        elif c == "5": 
            pyr1 += "5"
            pyr2 += "5"
            pyr3 += "5"
            pyr4 += "5"
            pyr5 += "5"
            pyr6 += "5"
            pyr7 += "5"
        elif c == "6": 
            pyr1 += "4"
            pyr2 += "6"
            pyr3 += "4"
            pyr4 += "8"
            pyr5 += "8"
            pyr6 += "2"
            pyr7 += "2"
        elif c == "7": 
            pyr1 += "9"
            pyr2 += "1"
            pyr3 += "3"
            pyr4 += "3"
            pyr5 += "1"
            pyr6 += "9"
            pyr7 += "7"
        elif c == "8": 
            pyr1 += "8"
            pyr2 += "2"
            pyr3 += "2"
            pyr4 += "6"
            pyr5 += "4"
            pyr6 += "6"
            pyr7 += "4"
        elif c == "9": 
            pyr1 += "7"
            pyr2 += "3"
            pyr3 += "1"
            pyr4 += "9"
            pyr5 += "7"
            pyr6 += "3"
            pyr7 += "1"
    opo1, opo2, opo3, opo4, opo5, opo6, opo7 = "", "", "", "", "", "", ""
    for c in str_opo:
        if c == "1": 
            opo1 += "3"
            opo2 += "7"
            opo3 += "9"
            opo4 += "1"
            opo5 += "3"
            opo6 += "7"
            opo7 += "9"
        elif (c == "2"):
            opo1 += "2"
            opo2 += "8"
            opo3 += "8"
            opo4 += "4"
            opo5 += "6"
            opo6 += "4"
            opo7 += "6"
        elif (c == "3"):
            opo1 += "1"
            opo2 += "9"
            opo3 += "7"
            opo4 += "7"
            opo5 += "9"
            opo6 += "1"
            opo7 += "3"
        elif (c == "4"):
            opo1 += "6"
            opo2 += "4"
            opo3 += "6"
            opo4 += "2"
            opo5 += "2"
            opo6 += "8"
            opo7 += "8"
        elif (c == "5"):
            opo1 += "5"
            opo2 += "5"
            opo3 += "5"
            opo4 += "5"
            opo5 += "5"
            opo6 += "5"
            opo7 += "5"
        elif (c == "6"):
            opo1 += "4"
            opo2 += "6"
            opo3 += "4"
            opo4 += "8"
            opo5 += "8"
            opo6 += "2"
            opo7 += "2"
        elif (c == "7"):
            opo1 += "9"
            opo2 += "1"
            opo3 += "3"
            opo4 += "3"
            opo5 += "1"
            opo6 += "9"
            opo7 += "7"
        elif (c == "8"):
            opo1 += "8"
            opo2 += "2"
            opo3 += "2"
            opo4 += "6"
            opo5 += "4"
            opo6 += "6"
            opo7 += "4"
        elif (c == "9"):
            opo1 += "7"
            opo2 += "3"
            opo3 += "1"
            opo4 += "9"
            opo5 += "7"
            opo6 += "3"
            opo7 += "1"
    pyr, opo = [str_pyr, pyr1, pyr2, pyr3, pyr4, pyr5, pyr6, pyr7], [str_opo, opo1, opo2, opo3, opo4, opo5, opo6, opo7]
    return pyr, opo

def save_memory(str_pyr, str_opo):
    file_path = "memory.txt"
    pyr, opo = mirrorTransposes(str_pyr, str_opo)
    for i in range(len(pyr)):
        player, opponent = pyr[i], opo[i]
        if not os.path.exists(file_path):
            open(file_path, "w").close()
            print("File created")
            with open(file_path, "a") as f:
                f.write(player + "\n")
                f.write(opponent + "\n\n")
        else:
            with open(file_path, "a") as f:
                f.write(player + "\n")
                f.write(opponent + "\n\n")

# Study the txt file analysis and return cordinate
# def oppo_mind(brd, pyr_cord) -> "Cordinate":
#     cords = [num for row in range(len(brd)) for num in brd[row] if num != "x" and num != "o" and num != pyr_cord]
#     #print(cords)
#     if (len(cords) != 0):
#         import random
#         index = random.randint(0, len(cords) - 1)
#         cord = cords[index]
#         return cord
#     else: return False

def oppo_mind(ply, brd, pyr_cord):
    file_path = "memory.txt"
    if not os.path.exists(file_path):
        open(file_path, "w").close()
        print("File created")
    cords = [num for row in range(len(brd)) for num in brd[row] if num != "x" and num != "o" and num != pyr_cord]
    # if (len(ply) == 0):
    #     import random
    #     index = random.randint(0, len(cords) - 1)
    #     cord = cords[index]
    #     return cord
    arr = []
    with open(file_path) as f:
        strs = f.read()
        arr = strs.split("\n")
    if (ply == ""): return int(arr[0][0])
    for i in range(0, len(arr) - 3, 3):
        if (arr[i + 1].find(ply) == 0):
            if (int(arr[i][len(ply) - 1]) in cords):
                return int(arr[i][len(ply) - 1])
    for row in brd:
        for num in row:
            if num != "x" and num != "o" and num != pyr_cord:
                return num
    else: return False

def update_cordinate(brd, cord, sign):
    bol1 = sign == "x" or sign == "o"
    bol2 = cord > 0 and cord < 10
    if (bol1 != True or bol2 != True): return False 
    if not checkBoard(brd): return False
    if (checkFilled(brd, "x", "o")): return False
    for row in range(len(brd)):
        for col in range(len(brd[0])):
            if (brd[row][col] == cord):
                brd[row][col] = sign 
                return brd
    return False

def update_board(brd, pyr_cord, pyr_sign, opo_cord, opo_sign):
    if (opo_cord == False): 
        break_cod = False
        for row in range(len(brd)):
            for col in range(len(brd[0])):
                # if (brd[row][col] == pyr_sign or brd[row][col] == opo_sign): return False
                if (brd[row][col] == pyr_cord and brd[row][col] != pyr_sign):
                    brd[row][col] = pyr_sign
                    break_cod = True
                    break 
            if (break_cod): break
        return brd
    bol1 = pyr_sign == "x" and opo_sign == "o"
    bol2 = pyr_sign == "o" and opo_sign == "x"
    if (bol1 != True and bol2 != True): return False 
    bol3 = pyr_cord > 0 and pyr_cord < 10
    bol4 = opo_cord > 0 and opo_cord < 10
    if (bol3 != True and bol4 != True): return False 
    
    cords = [num for row in range(len(brd)) for num in brd[row] if num != "x" and num != "o" and num != pyr_cord]
    if (pyr_cord == opo_cord and len(cords) > 1): return brd
    
    if not checkBoard(brd): return False
    if (checkFilled(brd, pyr_sign, opo_sign)): return False
    pyr_applied, opo_applied = False, False
    for row in range(len(brd)):
        for col in range(len(brd[0])):
            # if (brd[row][col] == pyr_sign or brd[row][col] == opo_sign): return False
            if (brd[row][col] == pyr_cord and brd[row][col] != pyr_sign):
                brd[row][col] = pyr_sign
                pyr_applied = True
            elif (brd[row][col] == opo_cord and brd[row][col] != opo_sign):
                brd[row][col] = opo_sign
                opo_applied = True
        if (pyr_applied and opo_applied): return brd
    while(not pyr_applied):
        pyr_cord = int(input("Choose player cordinate: "))
        for row in range(len(brd)):
            for col in range(len(brd[0])):
                # if (brd[row][col] == pyr_sign or brd[row][col] == opo_sign): return False
                if (brd[row][col] == pyr_cord and brd[row][col] != pyr_sign):
                    brd[row][col] = pyr_sign
                    pyr_applied = True
                    break
            if(pyr_applied): break
    while(not opo_applied):
        opo_cord = int(input("Choose opponent cordinate: "))
        for row in range(len(brd)):
            for col in range(len(brd[0])):
                # if (brd[row][col] == pyr_sign or brd[row][col] == opo_sign): return False
                if (brd[row][col] == opo_cord and brd[row][col] != opo_sign):
                    brd[row][col] = opo_sign
                    opo_applied = True
                    break
            if(opo_applied): break
    return brd

def round_run_time(your_won_times = 0, oppo_won_times = 0, draws = 0, rounds = 0, brd = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]):
    pyr_sign, opo_sign = chooseSign()
    str_pyr, str_opo = "", ""
    print("Your Sign\t:'"+ pyr_sign + "'.\nOpponent Sign\t:'" + opo_sign + "'.")

    filled = False
    cycle = 0
    
    while(not filled):
        print("\nYour Board")
        for row in brd: print(row)
        cords_available = [num for row in range(len(brd)) for num in brd[row] if num != "x" and num != "o"]
        pyr_cord, opo_cord = 1, 1
        applied_number = False

        if (rounds % 2 == 0):
            while(not applied_number):
                try:
                    pyr_cord = input("\nchoose number: ")
                    while(int(pyr_cord) not in cords_available):
                        pyr_cord = input("choose number: ")
                    pyr_cord = int(pyr_cord)
                    applied_number = True
                except Exception as e: print("Choose Number[" + str(cords_available) + "].\n" + str(e))
            str_pyr += str(pyr_cord)
            opo_cord = oppo_mind(str_pyr, brd, pyr_cord)
            str_opo += str(opo_cord)
            brd = update_board(brd, pyr_cord, pyr_sign, opo_cord, opo_sign)
        else: 
            opo_cord = oppo_mind(str_pyr, brd, pyr_cord)
            str_opo += str(opo_cord)
            print("Opponent Chosen: " + str(opo_cord), end = "")
            while(not applied_number):
                try:
                    pyr_cord = input("\nchoose number: ")
                    while(int(pyr_cord) not in cords_available):
                        pyr_cord = input("choose number: ")
                    pyr_cord = int(pyr_cord)
                    applied_number = True
                except Exception as e: print("Choose Number[" + str(cords_available) + "].\n" + str(e))
            str_pyr += str(pyr_cord)
            brd = update_board(brd, pyr_cord, pyr_sign, opo_cord, opo_sign)
        if (cycle > 1):
            if (winCondition(brd, pyr_sign)):
                your_won_times += 1
                rounds += 1
                scoreBoard(your_won_times, oppo_won_times, draws, rounds)
                
                save_memory(str_pyr, str_opo)

                return your_won_times, oppo_won_times, draws, rounds
            elif(winCondition(brd, opo_sign)):
                oppo_won_times += 1
                rounds += 1
                scoreBoard(your_won_times, oppo_won_times, draws, rounds)
                return your_won_times, oppo_won_times, draws, rounds
        filled = checkFilled(brd, "x", "o")
        if (filled):
            draws += 1
            rounds += 1
            scoreBoard(your_won_times, oppo_won_times, draws, rounds)
            return your_won_times, oppo_won_times, draws, rounds
        cycle += 1

def ask_quit():
    inp = input("Want to Quit(q): ")
    if (inp == "q"): return True

quit = False
your_won_times, oppo_won_times, draws, rounds = 0, 0, 0, 0
while(not quit):
    brd = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    your_won_times, oppo_won_times, draws, rounds = round_run_time(your_won_times, oppo_won_times, draws, rounds, brd)
    quit = ask_quit()