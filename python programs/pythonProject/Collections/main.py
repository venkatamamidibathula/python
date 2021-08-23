from collections import namedtuple, defaultdict, Counter

# Counter counts the occurance of a particular word in the sentence
a = "New England College is a premier institute"
b = Counter(a.lower().split())
print(b)
print(type(b))

# Named tuple is for giving custom names to indexed positions

Dog = namedtuple('Dog',['name','age','color'])
sammy = Dog(name='nima',age=90,color='black')
print(sammy.name)

# default dictionary have a default value for dictionaries

dict={'name':'Vikas','Age':45}
dict=defaultdict(lambda : "Not yet disclosed")
print(dict['Marital Status'])
