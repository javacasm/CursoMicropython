import time

def performanceTest():
    endTime = time.ticks_ms() + 10000
    count = 0
    while time.ticks_ms() < endTime:
        count += 1
    print("Count: ", count)
performanceTest()