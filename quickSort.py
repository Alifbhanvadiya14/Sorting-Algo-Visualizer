import time

def partition(data, left, right, drawData, timeTick):

    i = left
    pi = data[right]

    drawData(data, getColorArray(len(data), left, right, i, i))
    time.sleep(timeTick)

    for j in range(left,right):
        if data[j] < pi:
            drawData(data, getColorArray(len(data), left, right, i, j, True))
            time.sleep(timeTick)

            data[i], data[j] = data[j],data[i]
            i = i+1
            
        drawData(data, getColorArray(len(data), left, right, i, j))
        time.sleep(timeTick)

    # swap pivot with border value
    drawData(data, getColorArray(len(data), left, right, i, right, True))
    time.sleep(timeTick)
    data[i],data[right] = data[right],data[i]

    return i

def quick_sort(data, left, right, drawData, timeTick):
    if left < right:
        pivot = partition(data, left, right, drawData, timeTick)

        quick_sort(data, left, pivot-1, drawData, timeTick)
    
        quick_sort(data, pivot+1, right, drawData, timeTick)

def getColorArray(dataLen, left, right, border, currIdx, isSwap = False):

    colorArray = []
    for i in range(dataLen):

        # base coloring
        if i>= left and i<= right:
            colorArray.append('gray')
        
        else:
            colorArray.append('white')

        if i == right:
            colorArray[i] = 'blue'
        elif i == border:
            colorArray[i] = 'red'
        elif i == currIdx:
            colorArray[i] = 'yellow'
        
        if isSwap:
            if i == border or  i== currIdx:
                colorArray[i] = 'green'
    return colorArray