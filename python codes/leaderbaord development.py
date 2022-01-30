def leaderboard(top_1, top_2, top_3, top_4, top_5, count_ulti, top_1_name, top_2_name, top_3_name, top_4_name, top_5_name):
    if count_ulti < top_1 or count_ulti == top_1:
        top_5 = top_4
        top_4 = top_3
        top_3 = top_2
        top_2 = top_1
        top_1 = count_ulti
        top_5_name = top_4_name
        top_4_name = top_3_name
        top_3_name = top_2_name
        top_2_name = top_1_name
        top_1_name = input("enter your name for first palce ")
    elif count_ulti < top_2 or count_ulti == top_2:
        top_5 = top_4
        top_4 = top_3
        top_3 = top_2
        top_2 = count_ulti
        top_1 = top_1
        top_5_name = top_4_name
        top_4_name = top_3_name
        top_3_name = top_2_name
        top_2_name = input("enter your name for first palce ")
        top_1_name = top_1_name
    elif count_ulti < top_3 or count_ulti == top_3:
        top_5 = top_4
        top_4 = top_3
        top_3 = count_ulti
        top_2 = top_2
        top_1 = top_1
        top_5_name = top_4_name
        top_4_name = top_3_name
        top_3_name = input("enter your name for first palce ")
        top_2_name = top_2_name
        top_1_name = top_1_name
    elif count_ulti < top_4 or count_ulti == top_4:
        top_5 = top_4
        top_4 = count_ulti
        top_3 = top_3
        top_2 = top_2
        top_1 = top_1
        top_5_name = top_4_name
        top_4_name = input("enter your name for first palce ")
        top_3_name = top_3_name
        top_2_name = top_2_name
        top_1_name = top_1_name
    elif count_ulti < top_5 or count_ulti == top_5:
        top_5 = count_ulti
        top_4 = top_4
        top_3 = top_3
        top_2 = top_2
        top_1 = top_1
        top_5_name = input("enter your name for first palce ")
        top_4_name = top_4_name
        top_3_name = top_3_name
        top_2_name = top_2_name
        top_1_name = top_1_name
    print('  ')
    print('Title\t\t\t\tName:\t\t\tScore:')

    print(f'The top scorer is \t\t{top_1_name}\t\t\t{top_1}')

    print(f'In second place is \t\t{top_2_name}\t\t\t{top_2}')

    print(f'In third place is \t\t{top_3_name}\t\t\t{top_3}')

    print(f'In fourth place is \t\t{top_4_name}\t\t\t{top_4}')

    print(f'In fifth place we have \t\t{top_5_name}\t\t\t{top_5}')
    print('  ')

    return top_1, top_2, top_3, top_4, top_5, top_1_name, top_2_name, top_3_name, top_4_name, top_5_name



def main():
    top_1 = 1000
    top_2 = 1000
    top_3 = 1000
    top_4 = 1000
    top_5 = 1000
    count_ulti = 0
    top_1_name = 'N/A '
    top_2_name = 'N/A '
    top_3_name = "N/A "
    top_4_name = "N/A "
    top_5_name = "N/A "
    top_1, top_2, top_3, top_4, top_5, top_1_name, top_2_name, top_3_name, top_4_name, top_5_name = leaderboard(top_1, top_2, top_3, top_4, top_5, count_ulti, top_1_name, top_2_name, top_3_name, top_4_name, top_5_name)
main()