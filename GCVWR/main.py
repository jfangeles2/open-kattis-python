gcvwr, truckWeight, n = map(int, input().split(' '))

itemsWeight = sum(map(int, input().split(' ')))

print(int((gcvwr - truckWeight) * 0.9 - itemsWeight))
