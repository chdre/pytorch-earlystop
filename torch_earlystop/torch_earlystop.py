import torch


class EarlyStop:
    """Stops training if the validation loss does not decrease within a given
    range of epochs.

    Compared the lowest recorded loss to the latest loss. If the new loss is
    larger than the lowest recorded for a given set of epochs (persistence)
    the model is not improving and we can terminate it.
    """

    def __init__(self, persistence, path):
        """
        Arguments:
            persistence (int): Maximum checks
            path (str): Path to save checkpoints
        """
        self.lowest_loss = np.Inf
        self.counter = 0
        self.persistence = persistence
        self.criterion = False

    def __call__(self, model, loss):
        """
        Arguments:
            model (pytorch object): Model to save state from
            loss (float): Running loss (validation or test) for comparison
        """
        if self.lowest_loss > loss:
            # If the new loss < lowest loss the model is still improving
            self.lowest_loss = loss
            self.counter = 0  # Start counting over
        elif self.lowest_loss <= loss:
            if self.counter == 1:
                torch.save(model.state_dict(), 'checkpoint.pt')
            # If the existing lowest loss is smaller than the new loss the model has not improved
            self.counter += 1

        self.criterion = self.counter == self.persistence
