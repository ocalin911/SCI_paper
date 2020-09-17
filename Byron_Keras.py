#This script generated text from Byron's writings.


from __future__ import print_function
from tensorflow.keras.callbacks import LambdaCallback
print("loading LambdaCallback...")
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import LSTM
from tensorflow.keras.optimizers import RMSprop
print("loading Keras...")
import numpy as np
print("loading numpy...")
import random
import io
import sys

#import byron volume I
with io.open('Byron1.txt') as f:
    text = f.read().lower()

#prints the length of text
print('text length:', len(text))

#collects the characters in the text
chars = sorted(list(set(text)))
print('total chars:', len(chars))
char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))

# cut the text in sequences of maxlen characters
maxlen = 70 

#set the translation step
step = 3

#define two arrays
sentences = []
next_chars = []
for i in range(0, len(text) - maxlen, step):
    sentences.append(text[i: i + maxlen])
    next_chars.append(text[i + maxlen])
print('nb sequences:', len(sentences))

print('Vectorization...')
x = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)
y = np.zeros((len(sentences), len(chars)), dtype=np.bool)
for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        x[i, t, char_indices[char]] = 1
    y[i, char_indices[next_chars[i]]] = 1

#print th enumber of characters found
print('chars:', len(chars))

# build the model: RNN with one LSTM layer with 70 cells
print('Build model...')
model = Sequential()
model.add(LSTM(70, input_shape=(maxlen, len(chars))))

#add dropout for regularization purposses
model.add(Dropout(0.04))

#add a dense layer with ReLu activation function
model.add(Dense(50, activation='relu'))

#add dropout for regularization purposses
model.add(Dropout(0.04))

#add the output layer with softmax activation
model.add(Dense(len(chars), activation='softmax'))

#train the model using cross entropy and Adam optimizer
model.compile(loss='categorical_crossentropy', optimizer='adam')

#define an auxiary function 
def sample(preds, temperature=1.0):
    # helper function to sample an index from a probability array
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

#generating text from a seed
def on_epoch_end(epoch, _):
    # Function invoked at end of each epoch. Prints generated text.
    print()
    print('----- Generating text after Epoch: %d' % epoch)

    start_index = random.randint(0, len(text) - maxlen - 1)
    for diversity in [0.5]:   #, 1.0, 1.2]:
        print('----- diversity:', diversity)

        generated = ''
        sentence = text[start_index: start_index + maxlen]
        #sentence = text[0: maxlen]
        
        generated += sentence
        print('----- Generating with seed: "' + sentence + '"')
        sys.stdout.write(generated)

        for i in range(400):
            x_pred = np.zeros((1, maxlen, len(chars)))
            for t, char in enumerate(sentence):
                x_pred[0, t, char_indices[char]] = 1.

            preds = model.predict(x_pred, verbose=0)[0]
            next_index = sample(preds, diversity)
            next_char = indices_char[next_index]

            sentence = sentence[1:] + next_char

            sys.stdout.write(next_char)
            sys.stdout.flush()
        print()

print_callback = LambdaCallback(on_epoch_end=on_epoch_end)


model.fit(x, y,
          batch_size=80,
          epochs=150,
          callbacks=[print_callback])
