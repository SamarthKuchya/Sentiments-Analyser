from keras.models import load_model
import numpy as np

model=load_model('model.h5')

output_dict={0:['Negative 😢 ','/static/img/negative.png'],1:['Neutral 😐','/static/img/neutral.png'],2:['Positive 😊 ','/static/img/positive.png']}

f=open('D:/Skills/Emoji Classifier/glove.6B.50d.txt',encoding='utf-8')
embedding_index={}

for line in f:
    values=line.split()
    word=values[0]
    coefs=np.asarray(values[1:],dtype='float')
    embedding_index[word]=coefs
    
f.close()

def embedding_output(X):
    maxLen=50 #max words in sentence
    embedding_out=np.zeros((X.shape[0],maxLen,50))
    for ix in range(X.shape[0]):
        # print(ix)
        try:
            X[ix]=X[ix].split()
        except:
            pass
        
        for ij in range(maxLen):
            # print(ix,ij)
            # print(X[ij:ix])
            # go to every word in the current (ix) sentence
            try:
                embedding_out[ix][ij]=embedding_index[X[ix][ij].lower()]
                # print(X[ix][ij])
            except:
                embedding_out[ix][ij]=np.zeros((50,))
    # print(embedding_out)
    return embedding_out

# model prediction 
def predict(X):
    X=np.asarray([X])
    print(X.shape)
    X=embedding_output(X)
    print(model.predict(X))
    return output_dict[np.argmax(model.predict(X))]

if __name__=='__main__':
    print(predict('Lately, doesnt sync between web app and Android reminders well. Still a nice app, but that is an inconvenience.'))