import os, random
from time import sleep
from json import load

def clear():
    os.system('cls' if os.name == 'nt' else 'clear') #CLEAR TERMINAL, WORKS IN LINUX AND WINDOWS


def timer(textBegin, textEnd):
    for x in range(5, -1, -1):
        clear()
        print(f'{textBegin}{x}{textEnd}')
        sleep(1)


def newGame(samePlayer = True):
    clear()
    print('Seja Bem-Vindo ao Quiz de Manutenção e Algoritmos, ', end = '')

    #VERIFY IF THERE'S A NEW PLAYER
    if samePlayer:
        player = input('Para Iniciarmos, Digite Seu Nome:\n\n--> ')
        clear()
    
    #VERIFY CHOSEN THEME
    theme = input('Informe a Matéria ao qual deseja fazer primeiro:\n\n[1] Para Manutenção\n[2] Para Algoritmo\n\n--> ')
    altsLetter = ['a', 'b', 'c', 'd']

    if theme == '1': #MANUTENÇÃO QUIZ
        themeSelector('questions_manutencao', int(theme), altsLetter)
        timer('Aguarde para poder responder as questões de Algoritmos --> 00:0', 's')
        themeSelector('questions_algoritmos', int(theme)+1, altsLetter)
        sleep(3)


    elif theme == '2': #ALGORITMOS QUIZ
            themeSelector('questions_algoritmos', theme, altsLetter)
            timer('Aguarde para poder responder as questões de Manutenção --> 00:0', 's')
            themeSelector('questions_manutencao', int(theme)-1, altsLetter)
            sleep(3)


    else: #RESTART QUIZ
        timer('O valor digitado é inválido, por favor espere 00:0', 's para reiniciar o quiz!')
        newGame(False)
    
    playAgain(player)


def themeSelector(themeChosen, themeIndex, altsLetter):
    score = qNumber = 0

    for i in questions[themeChosen]:
        print(score)

        #RANDOMIZING ALTERNATIVES
        alts = []
        altIndex = random.randint(0, 3)
        [alts.append(x) for x in i['other_alternatives']]    
        
        random.shuffle(alts)
        alts.insert(altIndex, i['right_answer'])

        #PRINTING EACH QUESTION
        clear()
        #print(altsLetter[altIndex])
        print('QUESTÃO ' + str(qNumber + 1) + '.', i['text'], '\n\n')
        for x in range(4):
            print(f'{altsLetter[x]}) {alts[x]}')
        guess = input('\n\n--> ')
        qNumber += 1

        #VERIFY ANSWER AND CALCULATING SCORE
        score += verifyAnswer(guess, altsLetter, altIndex)
    scoreCalc(themeIndex, score)

def verifyAnswer(guess, altsLetter, altIndex):
    if guess == altsLetter[altIndex]:
        clear()
        print('\nResposta correta, aguarde para a próxima questão...')
        sleep(2)
        return 1
    else:
        clear()
        print('\nResposta incorreta, aguarde para a próxima questão...')
        sleep(2)
        return 0


def scoreCalc(themeIndex, points):
    clear()
    if themeIndex == 1:
        print(f'Sua pontuação na matéria de manutenção foi {int(points * 100 / 15)}%')
        finalScore[0] = int(points * 100 / 15)
    else:
        print(f'Sua pontuação na matéria de algoritmos foi {int(points * 100 / 5)}%')
        finalScore[1] = int(points * 100 / 5)
    sleep(3)


def playAgain(p):
    clear()
    print(f'Nome do Jogador: {p}\nPontuação Quiz de Algoritmos: {finalScore[1]}%\nPontuação Quiz de Manutenção: {finalScore[0]}%\n\n')
    again = input('Deseja Iniciar o Jogo Novamente?\n\n[Y] Para Sim\n[N] Para Não\n\n--> ').upper()
    print(again)
    if again == 'Y':
        clear()
        index = input('Deseja Reiniciar Como Um Novo Jogador?\n\n[Y] Para Sim\n[N] Para Não\n\n--> ').upper()
        if index == 'Y':
            newGame(True)
        elif index == 'N':
            newGame(False)
        else:
            clear()
            print('Valor Inserido Inválido, Aguarde para Tentar Novamente...')
            sleep(3)
            playAgain(p)
    elif again == 'N':
        clear()
        print('Obrigado Por Ter Participado Desse Projeto!')
    else:
        clear()
        print('Valor Inserido Inválido, Aguarde para Tentar Novamente...')
        sleep(3)
        playAgain(p)


#OPENING QUESTIONS.JSON
with open('questions.json', encoding = 'UTF-8') as questions_json:
    questions = load(questions_json)

finalScore = [0, 0]

newGame()