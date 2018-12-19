"""
파이썬 dictionary 활용 기초!
"""

# 1. 평균을 구하세요.
iu_score = {
    "m": 80,
    "k": 90,
    "u": 100
}

# 답변 코드는 아래에 작성해주세요.
print("=====Q1=====")
sum = iu_score["m"] + iu_score["k"] + iu_score["u"]
avg = sum / len(iu_score)
print(avg)


#-------------------------1--------------------------
#total_score = 0
#count = 0
#for score in iu_score:
    #total_score = total_score + iu_score[score]
    #count = count + 1
#print(total_score/count)
#-------------------------2--------------------------
#scores = list(iu_score.values())
#print(sum(scores)/len(scores)



# 2. 반 평균을 구하세요.
scores = {
    "iu": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    },
    "ui": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    }
}
# 답변 코드는 아래에 작성해주세요.

print("=====Q2=====")

#sum_iu = score["iu"]["수학"] + score["iu"]["국어"] + score["iu"]["음악"]
#sum_ui = score["ui"]["수학"] + score["ui"]["국어"] + score["ui"]["음악"]
#sum = sum_iu + sum_ui
#lensum = len(score["iu"]) + len(score["ui"])
#avg = sum / lensum

#print(avg)

#for cl in scores:
#    tmp = list(scores[cl].values())
#    print("{}: {}".format(cl, sum(tmp)/len(tmp)))


# 3. 도시별 최근 3일의 온도 평균은?
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""
# 3-1. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
city = {
    "서울": [-6, -10, 5],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9],
}

# 답변 코드는 아래에 작성해주세요.






# 답변 코드는 아래에 작성해주세요.

print("=====Q3=====")

#for cit in city:
#    temp = city[cit]
#    print('{}의 평균기온: {}'.format(cit, round(sum(temp)/len(temp),1)))
#    print('{}의 평균기온: {:0.1f}'.format(cit, sum(temp)/len(temp)))






print("=====Q3-1=====")

#low = []
#high = []
#for ci in city:
#    low.append(min(city[ci]))
#    high.append(max(city[ci]))

#lowlow = min(low)
#highhigh = max(high)

#print()

#for ci in city:
    #for temp in city[ci]:
    
    
    
    
    
#print("최고 기온은 {}의 {}도이며, 최저기온은 {}의 {}도이다".format(maximum[0],maximum[1],minimum[0],minimum[1]))

# 4. 위에서 서울은 영상 2도였던 적이 있나요?
# 답변 코드는 아래에 작성해주세요.
print("=====Q4=====")
if '2' in city["서울"]:
    print("yes")
else:
    print("no")