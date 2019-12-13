def filetoList():
    import requests
    import pandas as pd
    
    nameCSV = '/home/simonbak/patentprojweb/proj/static/csv/ARGoogle.csv'
    csvValue = pd.read_csv(nameCSV, skiprows=1)
    patentList = csvValue[['id', 'title', 'assignee', 'inventor/author', 'priority date', 'filing/creation date', 'publication date', 'grant date', 'representative figure link']].as_matrix()
    return patentList

def GrantNum(patentList):
    numOfGrant = 0
    for i in range(0, len(patentList)):
        if len(str(patentList[i][7])) == 10:
               numOfGrant +=1
    return numOfGrant

def GrantYear(patentList):
    import numpy as np
    
    Year = []
    for i in range(0, len(patentList)):
        if len(str(patentList[i][7])) == 10:
            Year.append(int(str(patentList[i][7])[:4]))
    
    Year.sort()
    
    Max = int(max(Year))
    Min = int(min(Year))
    size = Max - Min + 1
    
    YearOfGrant = np.empty((size,2), dtype=np.int64)
    
    index = 0
    
    for i in range(Min, Max+1):
        j = int(i - Min)
        count = Year.count(i)
        
        YearOfGrant[j][0] = i
        YearOfGrant[j][1] = count
    
    return YearOfGrant

def GrantPerson(patentList):
    import numpy as np
    Person = []
    count = []

    for i in range(0, len(patentList)):
        if Person.count(str(patentList[i][2])) == 0:
            Person.append(str(patentList[i][2]))
            temp = Person.index(str(patentList[i][2]))
            count.append([temp, 1])
        else:
            temp = Person.index(str(patentList[i][2]))
            count[temp][1] = int(int(count[temp][1]) + 1)

    for i in range(0, len(count)):
        count[i][0] = Person[i]
        
    count.sort(key=lambda x:-x[1])
    
    return count

def Portfolio(X):
    import numpy as np
    import matplotlib.pyplot as plt
    from django.utils import timezone

    pltname = str(timezone.now())+'.png'
    
    Year = []
    YearIndex = []
    YearPerson = []

    for i in range(0, len(X)):
        temp = X[i][5]
        temp = temp[:4]
        X[i][5] = temp

    for i in range(0, len(X)):
        if YearIndex.count(int(X[i][5])) == 0:
            Year.append([int(X[i][5]), [X[i][2]]])
            YearIndex.append(int(X[i][5]))
            YearPerson.append([int(X[i][5]),0 ,1])
        else:
            temp = YearIndex.index(int(X[i][5]))
            if Year[temp][1].count(X[i][2]) == 0:
                Year[temp][1].append(X[i][2])
                YearPerson[temp][1] = YearPerson[temp][1]+1
                YearPerson[temp][2] = YearPerson[temp][2]+1
            else:
                YearPerson[temp][2] = YearPerson[temp][2]+1
            
    YearPerson.sort(key=lambda x:x[0])
    YearIndex.sort()

    X1 = []
    Y1 = []

    X2 = []
    Y2 = []

    X3 = []
    Y3 = []

    X4 = []
    Y4 = []
    
    X5 = []
    Y5 = []

    a= int(round(len(YearPerson)/5))
    b = int(round((len(YearPerson) - a)/4))
    c = int(round((len(YearPerson) - a - b)/3))
    d = int(round((len(YearPerson) - a - b - c)/2))
    e = len(YearPerson) - a - b - c - d

    for i in range(0, a):
        X1.append(YearPerson[i][1])
        Y1.append(YearPerson[i][2])
    for i in range(a, a+b):
        X2.append(YearPerson[i][1])
        Y2.append(YearPerson[i][2])
    for i in range(a+b, a+b+c):
        X3.append(YearPerson[i][1])
        Y3.append(YearPerson[i][2])
    for i in range(a+b+c, a+b+c+d):
        X4.append(YearPerson[i][1])
        Y4.append(YearPerson[i][2])
    for i in range(a+b+c+d, len(YearPerson)):
        X5.append(YearPerson[i][1])
        Y5.append(YearPerson[i][2])
        
    Period1 = 'Period 1(~' + str(YearIndex[a]) +')'
    Period2 = 'Period 2(~' + str(YearIndex[a+b])+')'
    Period3 = 'Period 3(~' + str(YearIndex[a+b+c])+')'
    Period4 = 'Period 4(~' + str(YearIndex[a+b+c+d]) +')'
    Period5 = 'Period 5(~' + str(YearIndex[a+b+c+d+e-1])+')'
    

    plt.rcParams["figure.figsize"] = (15,10)
    plt.rcParams['lines.linewidth'] = 1
    plt.rcParams.update({'font.size': 10})
    plt.plot(X1, Y1, linestyle='--', marker='o', color='#ff6600', label = Period1)
    plt.plot(X2, Y2, linestyle='--', marker='.', color='#DD6969', label = Period2)
    plt.plot(X3, Y3, linestyle='--', marker='v', color='#0073BD', label = Period3)
    plt.plot(X4, Y4, linestyle='--', marker='p', color='#1D4E2D', label = Period4)
    plt.plot(X5, Y5, linestyle='--', marker='*', color='#000000', label = Period5)
    plt.xlabel('Num of Person')
    plt.ylabel('Num of Filing')
    plt.legend(loc=2)

    plt.title('Portfolio')
    plt.savefig('./'+pltname)

    return pltname

def grantYearGraph(array):
    import matplotlib.pyplot as plt
    from django.utils import timezone
    time = str(timezone.now())
    temp = len(time)
    timeslice = time[0:19]
    pltname = timeslice+'.png'


    X = []
    Y = []
    for i in range(0, len(array)):
        X.append(array[i][0])
    for i in range(0, len(array)):
        Y.append(array[i][1])  
    plt.rcParams["figure.figsize"] = (100,100)
    plt.rcParams['lines.linewidth'] = 10
    plt.rcParams.update({'font.size': 150})
    plt.plot(X,Y)
    plt.xlabel('Year')
    plt.ylabel('Num')
    
    plt.title('Grant Num of Year')
    plt.savefig('/home/simonbak/patentprojweb/proj/static/img/'+pltname)
    return pltname

def grantPersonGraph(array, i):
    import matplotlib.pyplot as plt
    from matplotlib import font_manager, rc
    import platform
    from django.utils import timezone

    pltname = str(timezone.now())+'.png'

    
    top = []

    if platform.system() == 'Windows':
# 윈도우인 경우
        font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
        rc('font', family=font_name)
    else:    
# Mac 인 경우
        rc('font', family='AppleGothic')
    
    plt.rcParams['axes.unicode_minus'] = False
    
    a = 0
    while a < i:
        top.append(array[a])
        a = a + 1
        
    X = []
    Y = []
    for i in range(0, len(top)):
        X.append(top[i][0])
    for i in range(0, len(top)):
        Y.append(top[i][1])
    
    plt.rcParams["figure.figsize"] = (50,50)
    plt.rcParams['lines.linewidth'] = 10
    plt.rcParams.update({'font.size': 30})
    plt.bar(X, Y, width = 0.7, color="blue")
    plt.title('주요 출원인 출원수')
    plt.savefig('./'+pltname)
    return pltname

def findCitationNoHead(patentURL):
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    from selenium import webdriver
    import time
    
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    
    driver = webdriver.Chrome('proj/chromedriver', options=options)
    driver.get(patentURL)
    
    time.sleep(2)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    body = soup.find('body')
    
    a = body.find('search-app')
    b = a.find('search-result')
    c = b.find('search-ui')
    d = c.find('div', id='content')
    e = d.find('div', class_='layout horizontal style-scope search-ui')
    f = e.find('div', id='main')
    g = f.find('div', class_='style-scope search-result')
    h = g.find('div', id='mainContainer')
    i = h.find('result-container')
    j = i.find('patent-result')
    k = j.find('div', class_='layout horizontal style-scope patent-result')
    l = k.find('div', id='wrapper')
    m = l.find('div', class_='footer style-scope patent-result')

    #인용
    citation1 = m.find('div', class_="responsive-table style-scope patent-result")
    citation2 = citation1.find('div', class_='table style-scope patent-result')

    citation3 = citation2.findAll('a', id='link')

    CitationID = []
    num1 = 0
    num2 = 0

    for i in range(0, len(citation3)):
        patentID = str(citation3[i])
        for j in range(1,len(patentID)-1):
        
            if patentID[j] == '>':
                num1 = j
            elif patentID[j] == '<':
                num2 = j
                CitationID.append(patentID[num1+1:num2])
            
    #피인용
    cited1 = m.findAll('div', class_="responsive-table style-scope patent-result")
    cited2 = cited1[1].find('div', class_='table style-scope patent-result')
    cited3 = cited2.findAll('a', id='link')

    CitedID = []
    num1 = 0
    num2 = 0

    for i in range(0, len(cited3)):
        patentID = str(cited3[i])
        for j in range(1,len(patentID)-1):
        
            if patentID[j] == '>':
                num1 = j
            elif patentID[j] == '<':
                num2 = j
                CitedID.append(patentID[num1+1:num2])
    return CitationID, CitedID

def citationCSV(patentURL, CitationID, CitedID):
    import pandas as pd
    import numpy as np
    prefileName = input('파일명을 입력하세요')
    
    fileName = prefileName+".csv"
    tocsv = np.array([[patentURL, CitationID, CitedID]])
    df = pd.DataFrame(tocsv)
    df.to_csv(fileName, mode='a', header=False, index=False)

def citedGraph(patentList):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib import font_manager, rc
    import platform
    from django.utils import timezone

    pltname = str(timezone.now())+'.png'
    
    Person = []
    count = []
    realCount = []
    radius = []
    X = []
    Y = []
    x = []
    y = []
    YearCount = []

    PersonSearch = input('검색하고 싶은 출원인을 입력하세요')
    PersonCount = 0
    
    for i in range(0, len(patentList)):
        if patentList[i][2] == PersonSearch:
            PersonCount = PersonCount + 1

    for i in range(0, len(patentList)):
        if patentList[i][2] == PersonSearch:
            count.append([patentList[i][0], int(patentList[i][5][:4]), patentList[i][8]])
    
    print("Loading... 총 " + str(PersonCount)+'개')
    NUM = PersonCount
    for i in range(0, NUM):
        patentURL = count[i][2]
        temp = findCitationNoHead(patentURL)
        cited = len(temp[1])
        realCount.append([count[i][1], count[i][0], cited])
        print(str(i+1)+'/'+str(NUM))

    realCount.sort(key=lambda x:-x[0])


    for i in range(0, len(realCount)):
        radius.append(realCount[i][2]*100)
        X.append(realCount[i][0])
        Y.append(realCount[i][2])

    # plt 한글 입력 지정
    if platform.system() == 'Windows':
    # 윈도우인 경우
        font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
        rc('font', family=font_name)
    else:    
    # Mac 인 경우
        rc('font', family='AppleGothic')
    
    plt.rcParams['axes.unicode_minus'] = False


    for i in range(0, len(realCount)):
        if x.count(realCount[i][0]) == 0:
            x.append(realCount[i][0])
            y.append(realCount[i][2])
        else:
            index = x.index(realCount[i][0])
            y[index] = int(y[index] + realCount[i][2])

    for i in range(0, len(YearCount)):
        x.append(YearCount[i][0])
        y.append(YearCount[i][1])

    plt.rcParams["figure.figsize"] = (50,50)
    plt.rcParams.update({'font.size': 80})
    plt.scatter(X, Y, s=radius)
    plt.title(PersonSearch+' 특허 인용 지수 분석')
    plt.show()

    realCount.sort(key=lambda x:-x[2])
    print("TOP 3 인용")
    for i in range(0,3):
        print(realCount[i])


    plt.rcParams["figure.figsize"] = (50,50)
    plt.rcParams['lines.linewidth'] = 10
    plt.rcParams.update({'font.size': 80})
    plt.plot(x,y)
    plt.xlabel('Year')
    plt.ylabel('Num')
    
    plt.title(PersonSearch+' 연도별 인용건수 분석')
    plt.savefig('./'+pltname)
    return pltname