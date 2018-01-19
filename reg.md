## Regularization 

| Technique | What? | How? | Links |
|-----------------------------|:--------------------------------:|:------:|:-------------------------------------------------------------------|
| L1 | Minimize weight values | ```from keras import regularizers<br/> model.add(Dense(64, input_dim=64, kernel_regularizer=regularizers.l2(0.01), activity_regularizer=regularizers.l1(0.01)))``` | [http](http://www.chioka.in/differences-between-l1-and-l2-as-loss-function-and-regularization/)|
| L2 | Minimize weight values. Bigger Values are heavier penalized compared to L1|  |[http](http://www.chioka.in/differences-between-l1-and-l2-as-loss-function-and-regularization/) |
| Dropout | |  | |
| Early-Stopping | |  | |
| Limit layer size | |  | |
| Data augmentation | |  | |
