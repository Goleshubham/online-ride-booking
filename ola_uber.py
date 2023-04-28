#Assignment for ola and uber.abc
# Source = Swargate
# Destination = Kothrud
# Distance between source and Destination = 15 kms.
#car type = Mini car,sedan 
#per km = 20 rs * 15
#3 route = Swargate to Pune
# Swargate to Hadapsar
# Kothrud to Viman Nagar. 
#Dynamically.
#Using Dictionary

'''
print('*********Distance and price of routes between Pune*********')
'''
'''
a = str(input('Enter your current Location = ')),
b = str(input('Enter your Desired Location = ')),
'''
'''
c = dict(
    currentlocation = ['Swargate'],
    Desiredlocation = ['\t\tKothrud'],
    TotalDistance   = ['\t\t2.7 kms']
)
print(len(c))
print('Current Location\t\tDesired Location\tTotal Distance\t\tTotal Cost')
for a in range(len(c['Desiredlocation'])):
    for k,v in c.items():
        print(f'{v[a]}\t',end = '')

TotalCost = 20 
TotalDistance = 2.7
Perkm = (TotalCost*TotalDistance)
print(Perkm)

    '''
'''
try:
    print('*****Get Distance*****')
    routes = {'swargate-kothrud':20,'kothrud-swargate':20,
         'swargate-hadapsar':15,'hadapsar-swargate':15,'swargate-vimannagar':25,'vimannagar-swargate':20}

    print('******Available Here******')
    list_routes = routes.keys()
    print(list_routes) 

    for r in list_routes:
     print(r)
    
    source = input("Enter source =  ")
    source_lower = source.lower()
    destination = input("Enter Destination =  ")
    destination_lower = destination.lower()
    

    route_to_find = source_lower + '-' + destination_lower
    route_to_find = route_to_find
    if route_to_find in routes.keys():
     route_to_find = route_to_find
     print(
     f'Distance Between {source} and {destination} = {routes[route_to_find]}kms')
     
    else:
     print(
        f"Entered Route {source} to {destination} is not available routes.please try another route "
        )  
    #print(
     #f'Distance Between {source} and {destination} = {routes[route_to_find]}kms')

except BaseException as ex:
    print(f"Error occured as = {ex}")
    print("Something went Wrong.Please Contact support team +9881821696")

'''
'''
t1 = (11,22,33)
t2 = (44,55,66)
t3 = t1 > t2
print(t3)
'''
'''
#Swapping of two numbers.
a = input('Enter your First Number =  ')
b = input('Enter your Second Number = ')
a,b = b,a
print('a = ',a)
print('b = ',b)
'''