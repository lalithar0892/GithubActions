import pickle

data = {'name': 'Jenny', 'age': 25}  
pickle.dump(data,open('data.pkl', 'wb'))
loaded = pickle.load(open('data.pkl', 'rb'))
print(loaded)



