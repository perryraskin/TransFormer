import csv
from datetime import datetime

def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def isChase(file):
    first = 'Type'

    with open(file, 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if first == row[0]:
                return True
    return False

def parseChaseData(file):
    with open(file, 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        refund = 0
        amount = 0
        t = 0
        r = 0
        for row in reader:
            date = row[1]
            if float(row[4]) < 0:
                amount = float(row[4]) + (abs(float(row[4]))*2)
                refund = 0
                t = t + 1
            else:
                refund = 0 - float(row[4])
                amount = 0
                r = r + 1
            desc = row[3]
            ctg = row[5]
            addTransaction(date, amount, desc, ctg, refund)
        print(t, "transactions and", r, "refunds have been added!")

def isCapitalOne(file):
    first = 'Transaction Date'

    with open(file, 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if first == row[0]:
                return True
    return False

def parseCapitalOneData(file):
    with open(file, 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        refund = 0
        amount = 0
        t = 0
        r = 0
        for row in reader:
            date = row[0]
            if isFloat(row[5]):
                amount = float(row[5])
                refund = 0
                t = t + 1
            else:
                refund = float(row[6])
                refund = refund - (2*refund)
                amount = 0
                r = r + 1
                if desc.find('CAPITAL ONE MOBILE PYMT'):
                    refund = 0
                    r = r - 1
            desc = row[3]
            ctg = row[4]
                
            addTransaction(date, amount, desc, ctg, refund)
        print(t, "transactions and", r, "refunds have been added!")

# def isDiscover()

def addTransaction(date, amount, desc, ctg, refund):
    with open('all_transactions_test.csv', 'a') as newFile:
        reader = csv.reader(newFile, delimiter=',')
        newFileWriter = csv.writer(newFile)
        if amount > 0:
            newFileWriter.writerow([date, str(amount), desc, ctg])
        else:
            newFileWriter.writerow([date, refund, desc, ctg])

def main():
    """ ASK USER FOR CSV TO IMPORT """
    count = 0
    print ("Enter CSV filename: ", end='')
    file = input()

    try:
        
      if isChase(file):
        parseChaseData(file)
      elif isCapitalOne(file):
        parseCapitalOneData(file)

    except Exception as e:
        raise e
        print ("An error has occured. Please try again.")

    return 0

if __name__ == "__main__":
    main()