# pytorch-earlystop
Earlystopping for Pytorch. Compares the lowest recorded loss to the latest loss. If the new loss larger than the lowest recorded for a given set of epochs (persistence) the model is not improving and we can terminate it.

# Requirements
Pytorch

# Usage
```
from EarlyStop import EarlyStop

path = 'some/path/checkpoint.pt' # Path to store checkpoints
model = Model() # Pytorch model
persistence = 5

es_criterion = EarlyStop(persistence, path)

# The following is called during training
stop = es_criterion(model, loss) # Evaluates to True or False
```

