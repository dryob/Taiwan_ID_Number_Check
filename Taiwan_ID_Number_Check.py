def Taiwan_ID_Number_Check(ID):

    first = {'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15, 'g':16, 'h':17, 'j':18, 'k':19, 'l':20, 'm':21, 'n':22, 'p':23, 'q':24, 'r':25, 's':26, 't':27, 'u':28, 'v':29, 'w':32, 'x':30, 'y':31, 'z':33, 'i':34, 'o':35 }
    sec = [1,9,8,7,6,5,4,3,2,1,1]

    if len(ID) != 10:               #字數檢查 length check
        return False
    if not ID[1:9].isnumeric():   #2～10碼檢查 [1:9] not str check 
        return False

    if ID[0].isnumeric():         #1碼檢查 [0] not int check
        return False
    ID = ID.lower()
    ID = list(ID)
    if ID[1] != 1 or 2:         #2碼檢查 [1] check
        return False
    if len(ID) == 10:             #驗證 (N0 十位數 + (N0 個位數 x 9) + (N1 x 8) + (N2 x 7) +  (N3 x 6) +  (N4 x 5) +  (N5 x 4) +  (N6 x 3) +  (N7 x 2) + N8 + N9)

        ID[0] = first[ID[0]]
        ID00 = ID[0]
        del ID[0]

        ID.insert(0,int(ID00 % 10))
        ID.insert(0,int(ID00 / 10))

        total = 0
        
        for x,y in zip(ID,sec):
            s = int(x) * int(y)
            total+=s
            
        if total%10 ==0:
            return True
        else:
            return False
