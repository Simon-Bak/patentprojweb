word0 = request.POST['word0']
        word1 = request.POST['word1']
        word2 = request.POST['word2']
        wordandor01 = request.POST['wordandor01']
        wordandor02 = request.POST['wordandor02']
        
        status = request.POST['status']
        country = request.POST['country']

        person0 = request.POST['person0']
        person1 = request.POST['person1']
        person2 = request.POST['person2']

        if wordandor01 == '없음':
            wordurl = word0
        elif wordandor01 == 'AND':
            wordurl = word0+'&q='+word1
            if wordandor02 == '없음':
                wordurl = wordurl
            elif wordandor02 == 'AND':
                wordurl = wordurl + '&q=' + word2
            elif wordandor02 == 'OR':
                wordurl = wordurl + ',' + word2
        elif wordandor01 == 'OR':
            wordurl = word0+','+word1
            if wordandor02 == '없음':
                wordurl = wordurl
            elif wordandor02 == 'AND':
                wordurl = wordurl + '&q=' + word2
            elif wordandor02 == 'OR':
                wordurl = wordurl + ',' + word2

        personurl = '&inventor=' + person0 + ',' + person1 + ',' + person2

        if status == '둘다':
            status = ''

        URL = 'https://patents.google.com/?q=' + wordurl + personurl + '&country='+country+'&status='+status
        request.session['URL'] = URL