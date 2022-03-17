

space=5
star=1
while(space>1):
    print(space*' '+star*'*'+space*' ')
    space-=1
    star+=2
while(space<6):
    print(space*' '+star*'*'+space*' ')
    space+=1
    star-=2
    