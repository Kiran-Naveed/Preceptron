# Preceptron
The method of perceptron is that we first randomly initialize the weights, threshold values, and the alpha values. 
The threshold value is updated by biased input.
Then we multiply the weights with the inputs and if the input is greater then the threshold the output is one and 
if it is lesser then threshold the output is zero.
The activation function is threshold function. If the predicted and actual inputs are same the error is zero and no weights are 
updated the weights are updated after every example run. And not update if the error of example is zero. 
And we fix the number of iterations and weights are stored in the file which are updated weights.
And the epocts will store in datafile.txt a the weights which we use in prediction are store in new file “weights.txt” .
And then use for input predictions.
The error function which we use is
(actual-predicted).
