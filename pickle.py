#PICKLE FILES TO SAVE MODELS
import pickle

with open('movies.bin','wb') as file: 
    pickle.dump(movies,file)

with open("movies.bin",'rb') as file:
    new=load.file()
    pickle.load(new)
