import pickle

import datetime

t = datetime.datetime.now()

handler = open('pickle.test','wb')

print(pickle.dump(t,handler))  # to bytes

handler = open('pickle.test','rb')

s = handler.read()

print(pickle.loads(s))
