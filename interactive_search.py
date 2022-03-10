import pickle
import os
from index import Index

pre_index = Index()

target = "data/index_dump-small.pickle"
print("Loading Index")
print(os.path.getsize(target)) 
#GET SIZE of the document

with open(target, 'rb') as f:
    unpickler = pickle.Unpickler(f)
    print(unpickler)
    pre_index = unpickler.load()
    #load the .pickle file


print("Index Loaded")

print("Enter your search")
inp = input()

while inp:
    res = pre_index.search(inp, rank = True)
    for doc in res[:5]:
        print(doc[0].title)
    print("\n\n\n Enter words for yout next search")
    inp = input()