#kwargs = key word args

# def hello(first, last):
#     print("Hello " + first + " " + last)
    
# hello(first="Nico", last="Finstad")



def hello(**kwargs):
    
    # print("Hello " + kwargs["first"] + " " + kwargs["last"])
    print("Hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")
    
hello(title="Mr.", first="Nico", middle="Dude", last="Finstad")