import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):

    def test_getDataPoint_calculatePrice(self):

  		# this test ist contains some impossible stock values also to test it on wrong data , as stocks value can't be in negative or 0
        quotes = [
          {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
          {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'},
          {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
          {'top_ask': {'price': -1, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'},
          {'top_ask': {'price': 0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
          {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'},
          {'top_ask': {'price': 0.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
          {'top_ask': {'price': 1.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 1.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'},
          {'top_ask': {'price': 122.0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 122.0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
          {'top_ask': {'price': 122.0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 122.0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """

        #invalid stock prices as they can't be 0 or negative

        for quote in quotes:
            top_ask_price=quote['top_ask']['price']
            top_bid_price=quote['top_bid']['price']

            price=(top_ask_price+top_bid_price)/2
            message="Correct Input Data"

            if(top_ask_price<=0 or top_bid_price<=0):
                    price=0
                    message="Wrong Input Data"

            self.assertEqual(getDataPoint(quote), (message, quote['stock'], top_bid_price, top_ask_price, price))


    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        """ ------------ Add more unit tests ------------ """
        quotes = [
			{'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
			{'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'},
			{'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
			{'top_ask': {'price': -1, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'},
			{'top_ask': {'price': 0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
			{'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'},
			{'top_ask': {'price': 0.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
			{'top_ask': {'price': 1.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 1.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'},
			{'top_ask': {'price': 122.0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 122.0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
			{'top_ask': {'price': 122.0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 122.0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
		]

        """ ------------ Add the assertion below ------------ """
        prices = {}
        for quote in quotes:
            message, stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price

        if('ABC' in prices and 'DEF' in prices):
            self.assertEqual(getRatio(prices['ABC'], prices['DEF']), ("{}".format(round(prices['ABC']/prices['DEF'],4))))


if __name__ == '__main__':
    unittest.main()
