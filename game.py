print("Hello,Welcome to my quiz game:")
yourname=input('what is your name?')
ans=input('Are you in?(yes/no)')
score=0
if ans.lower()=='yes':
    ans=input('1.What is my favorite programming language?')
    if ans.lower()=='java':
        score+=1
        print('Correct!your score:'+str(score))
    else:
        score-=1
        print('wrong answer!your score:'+str(score))
    ans=input('2.what is my nickname?')
    if ans.lower()=='shivam':
        score+=3
        print('Correct!your score:'+str(score))
    else:
        score-=3
        print('wrong answer!your score:'+str(score))
    ans=input('3.what is my favorite pet animal?')
    if ans.lower()=='tiger':
        score+=5
        print('Correct!your score:'+str(score))
    else:
        score-=5
        print('wrong answer!your score:'+str(score))
    ans=input('4.Do i like intel i7 processor?')
    if ans.lower()=='yes':
        score+=2
        print('Correct!your score:'+str(score))
    else:
        score-=2
        print('wrong answer!your score:'+str(score))
    print('gameover')
    print(yourname +'your score: '+str(score))
    if(score>5):
        print('you are my best friend!' + yourname)
    else:
        print('Hate you!'+ yourname)
        
