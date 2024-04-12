from scipy.optimize import minimize
import pandas as pd

def read_stock_csv(fp_stocks):
    """
    Parse a csv file into a dictionary with
    key = stock name
    value = numpy array of historical daily stock prices
    The csv file has the following format:

    date, aaa, bbb, ccc, ...
    2019-01-02, $$$, $$$, $$$, ...
    2019-01-03, $$$, $$$, $$$, ...
    ...

    where aaa, bbb, ccc, ... are stock names
    
    Parameters
    ----------
    fp_stocks : str
        File path to the csv file

    Returns
    -------
    historical_data : dict
        Dict with key = stock name, value = numpy array of historical daily stock prices
    
    dates : numpy ndarray
        Corresponding dates of the historical prices

    Notes
    -----
    Read more about the pandas library here: https://pandas.pydata.org/docs/reference/index.html
    """

    try:
        df = pd.read_csv(fp_stocks, index_col='date')
        dates = df.index.to_numpy()
        historical_data = {name: df[name].values for name in df.columns}
        return dates, historical_data
    except FileNotFoundError:
        raise FileNotFoundError(f"No valid file at {fp_stocks}")
    except Exception as e:
        raise Exception(f"Unexpected {e=}, {type(e)=}")

def get_optimized_weights(initial_weights, mean_returns, cov_matrix, target_return):

    """
    Get optimized weights with miminized risk given desired target DAILY return
    
    Parameters
    ----------
    initial_weights : pandas Series
        Initial weights of the stocks in the port.

    mean_returns : pandas Series
        Mean DAILY returns of the stocks in the port. Index = stock name, Value = mean daily return
    
    cov_matrix : pandas DataFrame
        Covariance matrix of the stocks in the port.

    target_return : float
        Desired DAILY return. e.g. 0.001 means you want 0.1% daily return

    Returns
    -------
    pandas Series
        Optimized weights of the stocks in the port. Index = stock name, Value = weight
        If optimized weights can't be found, initial_weights is returned.
    """

    def get_port_variance(weights):
        return weights.dot(cov_matrix).dot(weights)
    
    def target_return_constraint(weights, target_return):
        return weights.dot(mean_returns) - target_return
    
    def port_constraint(weights):
        return weights.sum() - 1
    
    constraints = [
        {
            'type': 'eq',
            'fun': target_return_constraint,
            'args': [target_return], # will be updated in loop
        },
        {
            'type': 'eq',
            'fun': port_constraint,
        }
    ]

    result = minimize(
        fun=get_port_variance,
        x0=initial_weights, # uniform
        method='SLSQP',
        constraints=constraints,
        bounds=[(0, 1)]*len(initial_weights),
    )
    if result.success:
        print("Managed to find the weights for expected return of {:.3%}".format(target_return))
        return pd.Series(result.x, index=initial_weights.index)
    else:
        print("Failed to find the optimized weight for expected return of {:.3%}".format(target_return))
        return initial_weights
