# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from math import pi
from pyspark import SparkContext


class CheapestOperator():

    def __init__(self, number: str, sc: SparkContext):
        self.number = number
        self.sc = sc

    def setup_dataset(self, operators_url: dict):
        # create a dictionary to store the prices for each prefix and operator
        self.prefix_prices_op = {}

        # load the price lists as RDDs
        for operator, url in operators_url.items():
            operator_data_file = self.sc.textFile(url).map(lambda line: line.split() + [operator])
            if not self.prefix_prices_op:
                for prefix, price, operator in operator_data_file.collect():
                    self.prefix_prices_op[prefix] = (float(price), operator)
            else:
                self.update_prefix_prices(operator_data_file)

    # update prefix_prices_op with operator B (taking new prefixes and skiping duplicates, with the goal of keeping only the cheapest values)
    def update_prefix_prices(self, operator_data_file):
        for prefix, price, operator in operator_data_file.collect():
            if prefix in self.prefix_prices_op:
                if (self.prefix_prices_op[prefix][0] > float(price)):
                    min_price = float(price)
                    self.prefix_prices_op[prefix] = (min_price, operator)
            else:
                self.prefix_prices_op[prefix] = (float(price), operator)

    # define a function to find the cheapest operator for a given telephone number which has longest prefix
    def cheapest_operator(self):
        cheapest_price = float('inf')
        cheapest_operator = None
        longest_prefix = 0
        for prefix in self.prefix_prices_op.keys():
            if self.number.startswith(prefix):
                if len(prefix) >= longest_prefix:
                    longest_prefix = len(prefix)
                    cheapest_price = self.prefix_prices_op[prefix][0]  # Get price
                    cheapest_operator = self.prefix_prices_op[prefix][1]  # Get operator

        if cheapest_operator is not None:
            return cheapest_operator, cheapest_price
        else:
            return "No operator found for this number"