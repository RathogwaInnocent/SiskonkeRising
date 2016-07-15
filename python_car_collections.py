import sys
myFavouriteCars = {1:'BMW_M4', 2:'VW_GTI_7',3: 'FORD_MUSTENG_GT'}

print(myFavouriteCars)
for car in myFavouriteCars:
    print  (car,myFavouriteCars[car])

# OR

for i, v in enumerate(['BMW_M4','VW_GTI_7','FORD_MUSTENG_GT']):
    print i, v

# OR

myCarCollection = ['BMW_M4','VW_GTI_7','FORD_MUSTENG_GT']
for f in sorted(set(myCarCollection)):
    print f


