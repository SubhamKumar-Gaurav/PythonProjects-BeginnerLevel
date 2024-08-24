# Flames Game : 

print("FLAMES me aapka swagat hai ")
print("If the relationship between you and your crush turns out to be siblings,")
print("I am not responsible. Play at your own risk ")
name1=input("Enter your name : ")
name1=name1.lower().replace(" ","")
name2=input("Enter your crush's name : ") 
name2=name2.lower().replace(" ","")
list1=list(name1.strip()) 
list2=list(name2.strip()) 

def remove_common_character(l1,l2) : 
    for char in l1[:] :
        if char in l2 : 
            l1.remove(char) 
            l2.remove(char) 
    return len(l1+l2) 

count=remove_common_character(list1,list2) 
flames=['F', 'L', 'A', 'M', 'E', 'S']

while len(flames)>1 :
    index=(count%len(flames))-1
    if index>=0 :
        flames = flames[index+1:] + flames[:index]
    else :
        flames = flames[:len(flames)-1] 
        
result=  {  'F' : "Friends" ,
            'L' : "Love" ,
            'A' : "Affection" ,
            'M' : "Marriage" ,
            'E' : "Enemies" , 
            'S' : "Siblings"    }      

print(f"Your relationship status : {result[flames[0]]}") 
