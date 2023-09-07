import pandas as pd

def rmse(y_hat: pd.Series, y: pd.Series) -> float:
    """
    Function to calculate the root-mean-squared-error(rmse)
    """
    assert(y_hat.size == y.size)
    assert(y_hat.size > 0)
    return ((y-y_hat)**2).mean()**0.5
    


def mae(y_hat: pd.Series, y: pd.Series) -> float:
    """
    Function to calculate the mean-absolute-error(mae)
    """
    assert(y_hat.size == y.size)
    assert(y_hat.size > 0)
    return abs(y-y_hat).mean()