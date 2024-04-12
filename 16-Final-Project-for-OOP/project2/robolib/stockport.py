import numpy as np
import pandas as pd
pd.options.display.float_format = "{:,.3f}".format

from robolib.roboutils import get_optimized_weights

class Stock():

    all_stocks = []

    def __init__(self, name, historical_prices):
        if name in Stock.all_stocks:
            print(f"Stock with name '{name}' already exists. Please be careful!" )
        else:
            Stock.all_stocks.append(name)
        self.name = name
        self.historical_prices = np.array(historical_prices)

    def get_mean_return(self):
        daily_change = np.diff(self.historical_prices)
        daily_change_rate = daily_change/(self.historical_prices[:-1])
        return np.mean(daily_change_rate)
    
    def get_daily_change_rate(self):
        daily_change = np.diff(self.historical_prices)
        return daily_change/(self.historical_prices[:-1])

    def get_variance(self):
        return np.var(self.historical_prices)

    def __repr__(self):
        return "Stock('{}', {})".format(self.name, list(self.historical_prices))

    def __str__(self):
        return "{}: mean daily return = {:.3%}".format(self.name, self.get_mean_return())


class Portfolio():

    def __init__(self, name, stocks=dict()):
        self.name = name
        self.stocks = stocks
        self.weights = self.initialize_weights()
        self.mean_returns = self.get_mean_returns()
        self.cov_matrix = self.get_cov_matrix()

    def add_stock(self, stock):
        if stock.name in self.stocks.keys():
            print(f"Stock '{stock.name}' already exists in our port! Please remove the old one first if you want to replace it with a new one.")
        else:
            self.stocks[stock.name] = stock
            self.weights[stock.name] = 0
            self.mean_returns[stock.name] = stock.get_mean_return()
            self.cov_matrix = self.get_cov_matrix()
            print("Successfully added stock '{}'".format(stock.name))

    def remove_stock(self, name_to_remove):
        if name_to_remove in self.stocks.keys():
            removed_stock = self.stocks.pop(name_to_remove)
            self.weights = self.weights.drop(name_to_remove)
            self.mean_returns = self.mean_returns.drop(name_to_remove)
            self.cov_matrix = self.get_cov_matrix()
            print(f"Successfully removed stock '{name_to_remove}'")
        else:
            print(f"No stock with name '{name_to_remove}' in {self.name}")

    def print_stocks(self):
        if len(self.stocks) == 0:
            print("No stocks in the port!")
        else:
            print("There are {} stocks in {}.".format(len(self.stocks), self.name))
            for stock in self.stocks.values():
                print("-- " + str(stock))

    def initialize_weights(self):
        """
        Initialize weights in the port to uniform weights.

        Returns
        -------
        pandas Series
            Uniform weights of the stocks in the port.
        """
        if len(self.stocks) > 0:
            return pd.Series(1/len(self.stocks), index=self.stocks.keys())
        else:
            return pd.Series([])

    def get_mean_returns(self):
        """
        Get the mean DAILY return of each of the stocks in the port.

        Returns
        -------
        pandas Series
            Mean returns of the stocks in the port. Index = stock name, Value = mean daily return
        """
        if len(self.stocks) > 0:
            return pd.Series({name: stock.get_mean_return() for name, stock in self.stocks.items()})
        else:
            return pd.Series([])
        
    def get_cov_matrix(self):
        """
        Get the covariance matrix from the daily price changes of the stocks in the port

        Returns
        -------
        pandas DataFrame
            Covariance matrix of the stocks in the port. Returns None if no stocks in the port.
        """
        if len(self.stocks) > 0:
            all_stock_returns = dict()
            for name, stock in self.stocks.items():
                all_stock_returns[name] = stock.get_daily_change_rate()

            all_stock_returns = pd.DataFrame(all_stock_returns)
            return all_stock_returns.cov()
        else:
            return None
        
    def cal_expected_yearly_returns(self):
        """
        Calculate expected YEARLY returns from weights and mean returns of stocks in our port
        
        Parameters
        ----------
        weights : pandas Series
            Normalized weights of the stocks in our port.
        
        mean_returns : pandas Series
            Mean returns of the stocks in our port. The values must be aligned with the weights.

        Returns
        -------
        float
            Expected returns from weighted average of individual historical mean returns.
            The value is NOT converted to percentage yet! i.e. 0.5 means 50%
        """

        assert len(self.weights) == len(self.mean_returns), "weights and mean_returns must have the same length"

        return 252 * self.weights.dot(self.mean_returns) #252 trading days, this calculation is approximate
    
    def cal_optimized_weights(self, target_return):
        """
        Calculate optimized weights with miminized risk given desired target DAILY return
        
        Parameters
        ----------
        target_return : float
            Desired DAILY return. e.g. 0.001 means you want 0.1% daily return

        Returns
        -------
        pandas Series
            Optimized weights of the stocks in the port.
        """
        if len(self.stocks) > 0:
            self.weights = get_optimized_weights(self.weights, self.mean_returns, self.cov_matrix, target_return)
            print(self.weights)
        else:
            print("No stocks in portfolio!")
