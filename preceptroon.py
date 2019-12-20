import pandas as pd
import numpy as np
def Learning():
    datafile = pd.read_csv('datafile.csv')
    inputs = np.array(datafile[['x1', 'x2', 'x3']])
    inputs.tolist()
    labels = datafile["y"]
    labels.tolist()

    alpha = 0.1
    threshold = 0.2
    iterations = 20
    f=open("datafile.txt", "w")
    f.close()
    f = open("weights.txt", "w")
    f.close()
    w = [0.5]*(len(inputs[0]))

    n=0
    while n<iterations:
        with open("datafile.txt", "a") as text_file:
            text_file.write('%s\n' % "x1\t\tx2\t\tx3\t\tw1\t\t\tw2\t\t\tw3\t\tError\t\t\t\n")
        for i in range(0, len(inputs)):
             # predicted_output = np.dot(inputs[i], w)
             # print(predicted_output)
             output=0
             for x in range(len(inputs)-1):
                 output=output+inputs[i][x]*w[x]
             if output > threshold:
                yhat = 1.
             else:
                yhat = 0.
             listt=[]
             for j in range (0,len(w)):
                 # err=(0.5/4)*(labels[i]-yhat)**2
                 error=labels[i]-yhat
                 w[j]=w[j]+alpha*(error)*inputs[i][j]
             listt.append(w)
             listt.append(threshold)

             with open("datafile.txt", "a") as text_file:
                for x in inputs[i]:
                    text_file.write('%s\t' % x+"\t")
                for weight in w:
                    text_file.write('%0.2f\t' % weight+"\t")
                text_file.write(str(error))
                text_file.write('\n')




        n=n+1

    with open("weights.txt", "a") as text_file:
        for x in listt[0]:
            text_file.write('%s\n' % x)
        text_file.write('%s'%listt[1])
    print("I am Learning")

def prediction():
    datafile = pd.read_csv('C:/Users/Kiran/OneDrive/Desktop/datafile.csv')
    inputs = np.array(datafile[['x1', 'x2', 'x3']])
    inputs.tolist()
    labels = datafile["y"]
    labels.tolist()
    results=[]
    listt=[]
    file = open("weights.txt", "r")
    file = [x.rstrip("\n") for x in file.readlines()]
    for i in range(len(inputs)-1):
        listt.append(float(file[i]))
    threshold=float(file[len(inputs)-1])
    for i in range(0, len(inputs)):
        predicted_output = np.dot(inputs[i], listt)
        # activation function
        if predicted_output > threshold:
            yhat = 1.
        else:
            yhat = 0.
        results.append(yhat)
    return results


if __name__== "__main__" :

    Learning()
    print(prediction())




