from keras import backend as K

def count_parameters_keras(model):
    return int(np.sum([K.count_params(p) for p in set(model.trainable_weights)]))

def count_parameters_pytorch(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)
