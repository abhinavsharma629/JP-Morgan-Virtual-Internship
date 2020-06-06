################################################################################
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import urllib.request
import time
import json
import random

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500

def getDataPoint(quote):
	""" Produce all of the needed values to generate a datapoint """
	""" ------------- Update this function ------------- """
	stock = quote['stock']
	bid_price = float(quote['top_bid']['price'])
	ask_price = float(quote['top_ask']['price'])
	message="Correct Input Data"

	#If Input data is incorrect
	if(bid_price<=0 or ask_price<=0):
		return "Wrong Input Data", stock, bid_price, ask_price, 0

	price = (bid_price + ask_price)/2.0
	return message, stock, bid_price, ask_price, price



# # Find GCD For Ratio Purposes
# def findGCD(price_a, price_b):
# 	if(price_b==0):
# 		return price_a

# 	return findGCD(price_b, price_a%price_b)


def getRatio(price_a, price_b):
	""" Get ratio of price_a and price_b """
	""" ------------- Update this function ------------- """
	""" Also create some unit tests for this function in client_test.py """

	#If either side is 0 this means wrong data feed
	if(price_a==0 or price_b==0):
		return "{}".format(max(a,b))

	return "{}".format(round(price_a/price_b,4)) #rounding up the ratio to 4 decimal places for accuracy as well as readability

	#------------------- CODE TO SHOW RATIO IN A:B format ---------------------
	# # find position of decimal place
	# decimal_place_in_a=str(price_a).find('.')
	# decimal_place_in_b=str(price_b).find('.')

	# #update the prices with no decimal places
	# price_a=(int)(str(price_a)[:decimal_place_in_a]+str(price_a)[decimal_place_in_a+1:])
	# price_b=(int)(str(price_b)[:decimal_place_in_b]+str(price_b)[decimal_place_in_b+1:])

	# #Make price_a length equal to price_b
	# if(len(str(price_a))>len(str(price_b))):
	# 	price_b=(int)(str(price_b)+("0"*(len(str(price_a))-len(str(price_b)))))
	# else:
	# 	price_a=(int)(str(price_a)+("0"*(len(str(price_b))-len(str(price_a)))))

	# # Find GCD
	# gcd=findGCD(price_a,price_b)

	# price_a//=gcd
	# price_b//=gcd
	#-------------------------------------------------------------------------




# Main
if __name__ == "__main__":

	# Query the price once every N seconds.
	for _ in iter(range(N)):
		quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

		""" ----------- Update to get the ratio --------------- """
		prices={}
		for quote in quotes:
			message, stock, bid_price, ask_price, price = getDataPoint(quote)
			if(message=="Wrong Data Input"):
				print ("Quoted %s at (bid:%s, ask:%s) is an incorrect price")
			else:
				prices[stock]=price
				print ("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))

		if('ABC' in prices and 'DEF' in prices):
			print ("Ratio is %s" % getRatio(prices['ABC'],prices['DEF']),"approx.")
		else:
			print("Insufficient Data Available")

		print("\n-----------------------------------------------------------\n")
