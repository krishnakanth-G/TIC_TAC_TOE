table = {'1': ' ', '2': ' ', '3': ' ', '4': ' ',
         '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}


def printTable(table):
    print(table['1'] + '|' + table['2'] + '|' + table['3'])
    print('-----')
    print(table['4'] + '|' + table['5'] + '|' + table['6'])
    print('-----')
    print(table['7'] + '|' + table['8'] + '|' + table['9'])


def Main():
    cho = 'X'
    count = 0

    while count != 9:
        printTable(table)
        move = input("It's "+cho+" choice \n Select one place :")
        if table[move] == ' ':
            table[move] = cho
            count += 1
        else:
            print("This place is occupied")
            continue

        if count > 4:
            if table['1'] == table['2'] == table['3'] != ' ':
                printTable(table)
                print(" -------- " + cho + " won --------")
                break
            elif table['4'] == table['5'] == table['6'] != ' ':
                printTable(table)
                print(" -------- " + cho + " won --------")
                break
            elif table['7'] == table['8'] == table['9'] != ' ':
                printTable(table)
                print(" -------- " + cho + " won --------")
                break
            elif table['1'] == table['4'] == table['7'] != ' ':
                printTable(table)
                print(" -------- " + cho + " won --------")
                break
            elif table['2'] == table['5'] == table['8'] != ' ':
                printTable(table)
                print(" -------- " + cho + " won --------")
                break
            elif table['3'] == table['6'] == table['9'] != ' ':
                printTable(table)
                print(" -------- " + cho + " won --------")
                break
            elif table['7'] == table['5'] == table['3'] != ' ':
                printTable(table)
                print(" -------- " + cho + " won --------")
                break
            elif table['1'] == table['5'] == table['9'] != ' ':
                printTable(table)
                print(" -------- " + cho + " won --------")
                break

        if count == 9:
            print("\n------- TIE -------\n")

        if cho == 'X':
            cho = 'O'
        else:
            cho = 'X'

    play = input("WANT TO TRY AGAIN?(y/n):")
    if play == "y" or play == "Y":
        for x in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            table[x] = " "
        Main()


Main()
