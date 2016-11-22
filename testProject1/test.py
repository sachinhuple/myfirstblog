vol=80
girls=['mona','rina','tina','natasha','neeta']
count = len(girls)
def fun(name):
    for g1 in girls:
        for i in range (0,count):
            if(girls[i]==g1):  
                print(g1 +" says "+ " hey "+ name +" you are hott !!! I give you " +str(100-((i+1)*(100/count)))+" % discount" )
    if vol < 30:
        print("less than 30")
    elif vol >30 and vol <43:
        print("greater than 30 and less than 43")
    elif vol==43:
        print("number is 43. function test")
    else:
        print("unknown number")
    
name = raw_input("What is your name ?")
fun(name);
    