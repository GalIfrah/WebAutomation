import json
import random


class ProjectUtils:

    @staticmethod
    def loadJson():

        with open('FM.json', 'r') as f:
            obj = json.load(f)

        return obj

    @staticmethod
    def writeToJson(data):

        with open('FM.json', 'w') as outfile:
            json.dump(data, outfile)

    @staticmethod
    def createRandomMail():

        randEmail = ''.join(random.choice('0123456789ABCDEF') for i in range(16)) + '@mycheck.co.il'

        return randEmail
