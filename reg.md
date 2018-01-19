## Regularization 

| Technique | What? | How? | Links |
|-----------------------------|:--------------------------------:|:------:|:-------------------------------------------------------------------|
| L1 | Minimize weight values | ```from keras import regularizers``` | [http](http://www.chioka.in/differences-between-l1-and-l2-as-loss-function-and-regularization/)|
| L2 | Minimize weight values. Bigger Values are heavier penalized compared to L1| ```from keras import regularizers``` |[http](http://www.chioka.in/differences-between-l1-and-l2-as-loss-function-and-regularization/) |
| Dropout | Drop random neurons from a layer. Information needs to be encoded in multiple pathways. | ```from keras.layers import Dropout``` | [http](https://www.cs.toronto.edu/~hinton/absps/JMLRdropout.pdf)|
| Early-Stopping | Stops the learning process if the score on the validation set stops improving. |```from keras.callbacks import EarlyStopping ``` | [http](https://en.wikipedia.org/wiki/Early_stopping)|
| Limit layer size | Reduce the complexity of the model to force abstraction of information.  | Reduce model size | [http](http://ufldl.stanford.edu/wiki/index.php/Autoencoders_and_Sparsity) |
| Data augmentation | Augment the data to have a broader statistical variance and/or more data.  | E.g. adding noise, rotating images, handle punctuation, segmentation, annotate data, ...  | |
