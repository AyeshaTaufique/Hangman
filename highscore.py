
def highscore(score):
    D = []
    with open('score.txt', 'r+') as m:
        d = m.read()
        if d == '':
            D.append(score)
            m.write('Highscore ' + str(score))
        else:
            l = (d).split()
            if score >= int(l[1]):
                b = score
                m.seek(0)
                m.write('Highscore' + ' ' + str(b))