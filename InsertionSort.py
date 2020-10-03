import time

# review this once
'''def insertionSort(data, drawData, timeTick):
    key = 0
    j = 0

    for i in range(1, len(data)):
        key = data[i]
        j = i-1
        #drawData(data, ['blue' if x == j  else 'red' for x in range(len(data))])
        #time.sleep(timeTick)
        while j >= 0 and data[j] > key:
            #drawData(data, ['green' if x == j  else 'red' for x in range(len(data))])
            #time.sleep(timeTick)
            data[j+1] = data[j]
            drawData(data, ['green' if data[x] == key  else 'red' for x in range(len(data))])
            time.sleep(timeTick)
            data[j] = key
            j -= 1
            drawData(data, ['green' if j == x or x == j+1 else 'red' for x in range(len(data))])
            time.sleep(timeTick)
    
'''
def insertionSort(data, drawData, timeTick):

    for i in range(len(data)):
        
        j = i
        
        while j > 0 and data[j-1] > data[j]:
            #drawData(data, ['green' if x == j  else 'red' for x in range(len(data))])
            #time.sleep(timeTick)
            data[j-1], data[j] = data[j], data[j-1]
            j -= 1
            
            drawData(data, ['#03fc77' if j == x or x == j+1 else 'red' for x in range(len(data))])
            time.sleep(timeTick)

