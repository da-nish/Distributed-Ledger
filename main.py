import json
import random

class MainClass:


	# def __init__(self):
	# 	pass
	# @staticmethod
	def getBlock(self, top):#from user
		rand = str(random.randrange(3, 100004))
		block = {rand:
					{"DATA_" : "test_data",
					"PREV_HASH" : top,
					"TIMESTAMP_" : "test_time",
					"HASH_" : rand
					}
				}
		return block
	
	def writeBlock(self):


		with open("dlt.json", "r") as f:
			obj = json.load(f)
		d = obj["dlt"]["ledger"]
		block = self.getBlock(obj["dlt"]["Top"])

		d.update(block)
		obj["dlt"]["Top"] =list(block.keys())[0]
		print(obj)
		with open("dlt.json", "w") as f:
		    json.dump(obj,f,indent=4)
		f.close()


	def readBlock():
		pass
	
	def processBlock():
		# input data
		# validate data
		# check existance
		# take permission
		# add and broadcast
		pass

	def validateLedger():
		pass
		
main = MainClass()
main.writeBlock()
