def initURL():
    searchURL = ''
    keywordArr = []
    
    keywordArr.append(input('검색 키워드를 입력해주세요 : '))
        
    while True:
        orType = input('or 검색식을 이용하시겠습니까? Y/N')
        
        if orType == 'N':
            if len(keywordArr) == 1:
                searchURL = 'https://patents.google.com/?q='+keywordArr[0]
                break
            elif len(keywordArr) == 0:
                print("다시 입력해주세요")
            elif len(keywordArr) > 1:
                for i in range(0, len(keywordArr)):
                    if i == 0:
                        searchURL = 'https://patents.google.com/?q='+keywordArr[i]+','
                    elif i < (len(keywordArr)-1):
                        searchURL = searchURL+keywordArr[i]+','
                    else:
                        searchURL = searchURL+keywordArr[i]
                        break
                break
        elif orType == 'Y':
            continue
        else:
            print('잘못입력하셨습니다')
    return searchURL

def inputAnd(URL):
    while True:
        andType = input('and 검색식을 이용하시겠습니까? Y/N')
        if andType == 'N':
            return URL
            break
        elif andType == 'Y':
            keyword = input('추가할 검색어를 입력해주세요 : ')
            URL = URL + '&q=' + keyword
        else:
            print('잘못입력하셨습니다')

def inputOr(URL):
    while True:
        orType = input('or 검색식을 이용하시겠습니까? Y/N')
        if orType == 'N':
            return URL
            break
        elif orType == 'Y':
            keyword = input('추가할 검색어를 입력해주세요 : ')
            URL = URL + ',' + keyword
        else:
            print('잘못입력하셨습니다')
    
def AndOR(URL):
     while True:
        TypeSearch = input('추가하고 싶은 검색어를 입력해주세요. 만약 없다면 N을 입력해주세요(And/Or/N)')
        
        if TypeSearch == 'And':
            URL = inputAnd(URL)
        elif TypeSearch == 'Or':
            URL = inputOr(URL)
        elif TypeSearch == 'N':
            return URL
            break
        else:
            print('잘못입력되었습니다. 다시 폼을 확인하고 입력해주세요')

def URL():
    URL = initURL()
    frontURL = ''
    bakcURL = ''
    country = ''
    status = ''
    person = ''
    keyword= ''
    
    while True:
        Search = input('추가하고 싶은 검색어를 입력해주세요. 만약 없다면 N을 입력해주세요(검색어/출원상태/출원국/출원인/N)')
        if Search == '검색어':
            keyword = AndOR(keyword)
        elif Search == '출원상태':
            while True:
                statusType = input('출원상태를 입력해주세요. (출원/등록)')
                if statusType == '출원':
                    status = '&status=APPLICATION'
                    break
                elif statusType == '등록':
                    status = '&status=GRAND'
                    break
                else:
                    print('정확하게 입력해주세요')
        elif Search == '출원국':
            while True:
                countryType = input('출원국을 입력해주세요. (KR/US/둘다)')
                if countryType == 'KR':
                    country = '&country=KR'
                    break
                elif countryType == 'US':
                    country = '&country=US'
                    break
                elif countryType == '둘다':
                    country = '&country=US,KR'
                    break
                else:
                    print('정확하게 입력해주세요')
        elif Search == '출원인':
            while True:
                personStatus = input('출원인을 추가하시겠습니까?(Y/N) : ')
                if personStatus == "N":
                    break
                elif personStatus == "Y":
                    person = '&inventor='+input("추가할 출원인을 입력해주세요 : ")
                    inputOr(person)
                else:
                    print('정확하게 입력해주세요')
        elif Search == "N":
            URL = URL+keyword+status+country+person
            return URL
        else:
            print("정확하게 입력해주세요")
    return URL+keyword+status+country+person

def getCSVURL(URL):
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    from selenium import webdriver
    import time

    driver = webdriver.Chrome('./chromedriver')
    driver.get(URL)
    
    time.sleep(5)
    URL = driver.find_element_by_xpath('//*[@id="count"]/div[1]/span[2]/a').get_attribute('href')
    
    return URL

def filetoList(url):
    import requests
    import pandas as pd
    
    #파일 이름지정
    name = input('파일이름 입력')
    nameCSV = name+'.csv'
    
    while True:
        a = input("1. 파일이 로컬에 있습니다. 2. Googlepatent로 다운받아야 합니다.")
        
        if a == '2':
        #Google Patent
            URL = getCSVURL(url)
            file = open(nameCSV, 'wb')
            value = requests.get(URL)
            file.write(value.content)
            file.close()
        
            csvValue = pd.read_csv(nameCSV, skiprows=1)
            patentList = csvValue[['id', 'title', 'assignee', 'inventor/author', 'priority date', 'filing/creation date', 'publication date', 'grant date', 'representative figure link']].as_matrix()
            return patentList
        elif a == '1':
            csvValue = pd.read_csv(nameCSV, skiprows=1)
            patentList = csvValue[['id', 'title', 'assignee', 'inventor/author', 'priority date', 'filing/creation date', 'publication date', 'grant date', 'representative figure link']].as_matrix()
            return patentList
