def Administrative():
    admin=input('Enter your name: ')
    pas=input('enter password to login: ')
    if admin == 'Ayesha' and pas == '123456':
        task=input('select options:\n'
                   '1.Manage words file\n'
                   '2.Reset highscore')
        if task == '1':
            print('Use space between words incase of entering more than one word!!!')
            word=input('Enter any word to add that in wordslist!')
            with open('words.txt','a+') as file:
                file.write(' '+word)
                print('Word added!!')
        if task== '2':
            with open('score.txt','w+') as reset:
                print('Highscore reset!!!')

    elif admin != ' Amanay' or pas != '123456':
         print('You have entered incorrect Admin name or password!!!')