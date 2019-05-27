#-*-coding:utf-8-*-
stress_type = ["학습/진로","친구","연애","스트레스"]
Course= \
["1. 나는 중요한 결정을 할 때 매우 체계적으로 한다.",
"2. 나는 충분한 시간을 두고 생각을 한 후에 결정을 한다.",
"3. 나는 어떤 결정을 할 때 그것이 나중에 미칠 결과까지도 고려한다.",
"4. 나는 내가 내린 결정을 하나하나가 최종 목표를 향해 발전해 나가는 단계라고 곧잘 생각한다.",
"5. 나는 참으로 올바른 결정을 하고 싶기 때문에 성급하게 결정을 하지 않는다"
]
friends =\
["1.나의 가치는 남을 도울 때 높아진다.",
"2. 나를 기쁘게 하거나 나만을 위한 일을 하면 이기적이라고 생각하지 않는다.",
"3. 나는 사랑스럽거나 가치 있는 사람이다.",
"4. 누군가와 너와 나 단 둘이라는 친밀한 관계가 형성되어 있다고 생각한다.",
"5. 평소 자신의 감정을 솔직하게 표현하는 편이다."
]
love = \
["1.자주 싸우는거 같다.",
"2.자주 만나는거 같다.",
"3.싸움은 연애의 과정이라고 생각한다.",
"4.자기가 힘들 때 연인에게 도와달라고 할 수 있다.",
"5.질투는 관계 유지에 있어 도움이 된다고 생각한다."
]

stress = \
["1. 매사에 걱정하는 편이다.",
"2. 아주 사소한 결정도 잘 내린다.",
"3. 새로운 자료에 흥미를 집중시키는데 어려움이 없다.",
"4. 평소 편안하게 휴식을 취하지 못 한다.",
"5. 편안하게 쉴 수가 있다."
]

#while True:
#    print("분야를 고르시오:")
for i in stress_type:
    print(i, end =" ")
print()
#    choose_type = input()
print("설문조사를 시작합니다.")
#print("1:전혀아니다. 2:그렇지않다. 3:보통이다. 4:그렇다. 5:상당히 그렇다.")
score_study = 0
score_friend = 0
score_love = 0
score_stress = 0
score_total = 0
#    if choose_type == "학습/진로":
print("-------------------학습/진로--------------------")
print("1:전혀아니다. 2:그렇지않다. 3:보통이다. 4:그렇다. 5:상당히 그렇다.")
for i in Course:
    print(i)
    sum = int(input())
    if sum > 5 or sum < 0:
        print("해당되지 않는 문항입니다.")

    else:
        print("저장되었습니다.\n")
        score_study = score_study + sum
score_total += score_study
print("점수 : " + str(score_study) + "\n")

#    elif choose_type == "친구":
print("-------------------친구--------------------")
print("1:전혀아니다. 2:그렇지않다. 3:보통이다. 4:그렇다. 5:상당히 그렇다.")
for i in friends:
    print(i)
    sum = int(input())
    if sum > 5 or sum < 0:
        print("해당되지 않는 문항입니다.")

    else:
        print("저장되었습니다.\n")
        score_friend = score_friend + sum
score_total += score_study
print("점수 : " + str(score_friend) + "\n")

#    elif choose_type == "연애":
print("-------------------연애--------------------")
print("1:전혀아니다. 2:그렇지않다. 3:보통이다. 4:그렇다. 5:상당히 그렇다.")
for i in love:
    print(i)
    sum = int(input())
    if sum > 5 or sum < 0:
        print("해당되지 않는 문항입니다.")
    else:
        print("저장되었습니다.\n")
        score_love = score_love + sum
score_total += score_study
print("점수 : " + str(score_love) + "\n")

#elif choose_type == "스트레스":
print("-------------------스트레스--------------------")                
print("1:전혀아니다. 2:그렇지않다. 3:보통이다. 4:그렇다. 5:상당히 그렇다.")
for i in stress:
    print(i)
    sum = int(input())
    if sum > 5 or sum < 0:
        print("해당되지 않는 문항입니다.")
    else:
        print("저장되었습니다.\n")
        score_stress = score_stress + sum
score_total += score_study
print("점수 : " + str(score_stress) + "\n")

print("총점 : " + str(score_total))

#    elif choose_type =="quit":
#        break
#    else:
#        print("다시 고르시오.")

fr = open("설문조사결과물.txt", 'r', encoding='utf-8')
fw = open("output.txt", 'w', encoding='utf-8')

lines = fr.readlines()

fw.write("학습/진로\n")
fw.write("당신의 점수는 {}점입니다\n".format(score_study))
if(0 < score_study and score_study <= 7):
    fw.write(lines[2])
    fw.write(lines[3])
    fw.write("\n")
elif (7 < score_study and score_study <=13):
    fw.write(lines[6])
    fw.write(lines[7])
    fw.write("\n")
elif (13 < score_study and score_study <=25):
    fw.write(lines[10])
    fw.write(lines[11])
    fw.write("\n")
elif (19 < score_study and score_study <=25):
    fw.write(lines[14])
    fw.write(lines[15])
    fw.write("\n")

fw.write("친구\n")
fw.write("당신의 점수는 {}점입니다\n".format(score_love))
if(0 < score_love and score_love <= 7):
    fw.write(lines[19])
    fw.write(lines[20])
    fw.write("\n")
elif (7 < score_love and score_love <=13):
    fw.write(lines[23])
    fw.write(lines[24])
    fw.write("\n")
elif (13 < score_love and score_love <=25):
    fw.write(lines[27])
    fw.write(lines[28])
    fw.write("\n")
elif (19 < score_love and score_love <=25):
    fw.write(lines[31])
    fw.write(lines[32])
    fw.write("\n")

fw.write("연애\n")
fw.write("당신의 점수는 {}점입니다\n".format(score_love))
if(0 < score_love and score_love <= 7):
    fw.write(lines[36])
    fw.write(lines[37])
    fw.write("\n")
elif (7 < score_love and score_love <=13):
    fw.write(lines[40])
    fw.write(lines[41])
    fw.write("\n")
elif (13 < score_love and score_love <=25):
    fw.write(lines[44])
    fw.write(lines[45])
    fw.write("\n")
elif (19 < score_love and score_love <=25):
    fw.write(lines[48])
    fw.write(lines[49])
    fw.write("\n")

fw.write("스트레스\n")
fw.write("당신의 점수는 {}점입니다\n".format(score_stress))
if(0 < score_stress and score_stress <= 7):
    fw.write(lines[53])
    fw.write(lines[54])
    fw.write("\n")
elif (7 < score_stress and score_stress <=13):
    fw.write(lines[57])
    fw.write(lines[58])
    fw.write("\n")
elif (13 < score_stress and score_stress <=25):
    fw.write(lines[61])
    fw.write(lines[62])
    fw.write("\n")
elif (19 < score_stress and score_stress <=25):
    fw.write(lines[65])
    fw.write(lines[66])
    fw.write("\n")

fr.close()
fw.close()