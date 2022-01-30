import random

def playings2(stop1, dic, count):
    comp2_score = 0
    for key in dic:
        if dic[key+count] != 1:
            comp2_score += dic[key]
            count += 1
        elif dic[key+count] == 1:
            comp2_score = 0
            return comp2_score
        if comp2_score >= stop1:
            return comp2_score

def playings1(stop1, dic):
    count = 0
    comp2_score = 0
    for key in dic:
        if dic[key] != 1:
            comp2_score += dic[key]
            count += 1
        elif dic[key] == 1:
            comp2_score = 0
            return comp2_score, count
        if comp2_score >= stop1:
            return comp2_score, count

def main():
    AMOUNT_OF_SIMS = 1000
    dic = {}
    playing = True
    comp1_score = 0
    comp2_score = 0
    stop1 = 15
    stop2 = 5
    total1_score = 0
    total2_score = 0
    comp1_win = 0
    comp2_win = 0
    wins = 0
    count = 0
    while wins != AMOUNT_OF_SIMS:
        playing = True
        total1_score = 0
        total2_score = 0
        while playing:
            for num in range(0,25):
                ran = random.randint(1,6)
                dic[num] = ran
            total1_score, count = playings1(stop1, dic)
            total1_score += total1_score
            if total1_score < 100:
                total2_score += playings2(stop2, dic, count)
            if total1_score>=100 or total2_score >=100:
                playing = False
                if total1_score >= 100:
                    comp1_win += 1
                    wins +=1
                elif total2_score >= 100:
                    comp2_win += 1
                    wins += 1
    print(comp1_win)
    print(comp2_win)
main()