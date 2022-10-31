quit = False
data = list()
names = list()
while not quit:
    print("----Welcome-------")
    print("1. Self introduction")
    print("2. Input score")
    print("3. check your score grade")
    print("4. Print the Average/Max/Min data for the scores")
    print("5. End the program")
    print("------------------")
    res = input("Please input your choice:")
    if res == "1":
        print("here are the codes for Self introduction")
        name = input("請問你的名字是:")
        color = input("你喜歡的顏色是:")
        age = input("你的年紀是:")
        print("你好，", "聽說您今年", age, "歲")
        print("你喜歡", color, "色")
    elif res == "2":
        print("here are the codes for Input score")
        scores = list()
        for i in range(1,11):
            score = int(input("請輸入{}號同學的成績:".format(i)))
            scores.append((i, score))
        fp = open("scores.dat", "w")
        fp.write(str(scores))
        fp.close ()
    elif res == "3":
        print("here are the codes for check your score grade")
        score = int(input("請輸入你的成績:"))
        print("成績是", score, "分")
        print("你的等級是:", end="")
        if score < 60:
            print("F")
        else:
            if score >=90:
                print("A")
            elif score >=80:
                print("B")
            elif score >=70:
                print("C")
            else:
                print("D")
    elif res == "4":
        print("here are the codes for print the summary of the data")
        data = list()
        n = input("num=")
        for i in range( int(n) ):
            n = input("name=")
            s = input("score=")
            data.append( int(s) )
        print("最高分：",max(data))
        print("最低分：",min(data))
        print("平均：", sum(data)/len(data))
    elif res == "5":
        quit = True
    else:
        print("I can't recognize your command!")