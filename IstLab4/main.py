respondentsNum = 5
candidatesNum = 3
candidatesZa = [0] * candidatesNum
candidatesProtiv = [0] * candidatesNum

candidatesBord = [0] * candidatesNum

def majorityMethod():
    for i in range(respondentsNum):
        tmp = int(input("Какого кандидата вы выбираете? (1 - 3) "))
        tmp2 = int(input("Против какого кандидата вы очень сильно против? (1 - 3) "))
        candidatesZa[tmp - 1] += 1
        candidatesProtiv[tmp2 - 1] += 1
    max = 0
    winner = 0
    for i in range(len(candidatesZa)):
        if candidatesZa[i] > max:
            max = candidatesZa[i]
            winner = i

    print("Наибольшее количество голосов ЗА (" + str(max) + ") было отдано кандидату " + str(winner + 1) + " при этом ОЧЕНЬ ПРОТИВ него - " + str(candidatesProtiv[winner]))

def boardMethod():
    for i in range(respondentsNum):
        tmp = int(input("Какое место для 1 кандидата? (1 - 3) "))
        tmp2 = int(input("Какое место для 2 кандидата? (1 - 3) "))
        tmp3 = int(input("Какое место для 3 кандидата? (1 - 3) "))

        candidatesBord[0] += (candidatesNum + 1) - tmp
        candidatesBord[1] += (candidatesNum + 1) - tmp2
        candidatesBord[2] += (candidatesNum + 1) - tmp3

    max = 0
    winner = 0
    for i in range(len(candidatesBord)):
        if candidatesBord[i] > max:
            max = candidatesBord[i]
            winner = i

    print("Наибольшее количество баллов (" + str(max) + ") получил кандидат " + str(winner + 1))

model = input("Выберите модель принятия решения (1 - относительно большинства; 2 - модель Борда): ")

if model == "1":
    majorityMethod()

if model == "2":
    boardMethod()





