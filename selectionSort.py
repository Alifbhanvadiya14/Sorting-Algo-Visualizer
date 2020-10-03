import time

def selectionSort(data, drawData, timeTick):
    for i in range(len(data)):
        
        min = i
        drawData(data, ['#03fc77' if x == min else 'red' for x in range(len(data))])
        time.sleep(timeTick)
        
        for j in range(i+1,len(data)):
            drawData(data, ['yellow' if x == j else 'red' for x in range(len(data))])
            time.sleep(timeTick)
            if data[j] < data[min]:
                drawData(data, ['blue' if x == j else 'red' for x in range(len(data))])
                time.sleep(timeTick)
                min = j
                

        drawData(data,['green' if x==i or x == min else 'red' for x in range(len(data))])
        time.sleep(timeTick)
        data[min],data[i] = data[i], data[min]
        

    
