# number_list:list[int]=[1,2,3,4,5,6]
# even:list[int]= [n for n in number_list if n%2==0]
# print(even)
#for vowels
# text:str= 'meowcathello'
# vowels = [v for v in text if  v in 'AEIOUaeiou']
# print(vowels)
# print('vowelcount:',len(vowels))
## looping problem 
people:list[str]=['bob','James','sandra','Arzu']
for person in people.copy():
    if person=='sandra':
        people.remove('sandra')
    print(person)
print(people)
    