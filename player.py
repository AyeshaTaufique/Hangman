
def player():
    import random
    with open("words.txt",'r') as f:
        words = f.read().split()

        secret_word = random.choice(words)
        print('loading word list from file....')
        print(len(words), 'words loaded')   # words=list of words
        print('Welcome to the game Hangman!')
        name = input('Enter your name--->')
        print('Welcome ' + name + '!')
        print(secret_word)
        len_word = len(secret_word)
        print(f'I am thinking of a word that is {len_word} letters long only')
    
        print('_'*35)
        guesses = 6
        warnings = 3
        display = '_'*len(secret_word)
        ava_letter =('a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z').split(',')
        while guesses>0:
            print(f'\nYou have {guesses} guesses')
            print(f'You have {warnings} warnings')
            print('Available letters:',''.join(ava_letter))
            g=input('Please guess a letter:').lower()
            if len(g)==1:
                if g in secret_word and g in ava_letter:
                    print('Good guess:',end=' ')
                    ava_letter.remove(g)
                    for i in range(len(secret_word)):
                        if g == secret_word[i]:
                           display = display[:i] + g + display[i+1:]
                    print(display,end=' ')
                    print('\n'+'_'*35)
                elif g in 'aeiou' and g not in secret_word:
                    guesses-=2
                    print('Oops! that letter is not in my word:'+' ',display)
                    print('_' * 35)
                elif not g.isalpha():
                    print('Oops! That is not a valid letter:'+' ',display)
                    print('_'*35)

                    if warnings> 0:
                        warnings -= 1
                    elif warnings == 0:
                        guesses -= 1
                elif g not in ava_letter:
                    if warnings>0:
                        warnings-=1
                    elif warnings==0:
                        guesses-=1
                    print('Oops! you have already guessed that letter:', display)
                    print('_' * 35)
                elif g not in secret_word:
                    guesses -= 1
                    print("Oops! that letter is not in my word:"+' ',display)
                    print('_'*35)
                    ava_letter.remove(g)
                if guesses == 5 and secret_word != display:
                    print('_______________')
                elif guesses == 4 and secret_word != display:
                    print('_______________')
                    print('       O       ')
                elif guesses == 3 and secret_word != display:
                    print('_______________')
                    print('       O       ')
                    print('       |       ')
                elif guesses == 2 and secret_word != display:
                    print('_______________')
                    print('       O       ')
                    print('       |       ')
                    print('      / \      ')
                elif guesses == 1 and secret_word != display:
                    print('_______________')
                    print('       O       ')
                    print('      /|\       ')
                    print('      / \      ')
                    print('Only 1 guess left,Hangman on his last breath!!!')
                elif guesses <= 0 and secret_word != display:
                    print('_______________')
                    print('       O_|     ')
                    print('      /|\      ')
                    print('      / \      ')
                    print('You Loose \n You let a good man die!!!')
                    break
                count=len(set(secret_word))
                score=0
                if display == secret_word:
                     score = guesses* count
                     print('Congratulations, You Won')
                     print('your total score for this game is:', score)
                     break
            else:
                print('You can only enter one letter!!!!')

    return(score)









