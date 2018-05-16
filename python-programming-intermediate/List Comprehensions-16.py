## 2. Enumerate ##

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]

for index,value in enumerate(ships):
    print(value)
    print(cars[index])

## 3. Adding Columns ##

things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]

for index,value in enumerate(things):
    value.append(trees[index])

## 4. List Comprehensions ##

apple_prices = [100, 101, 102, 105]

apple_prices_doubled = [ price * 2 for price in apple_prices]
apple_prices_lowered = [ price-100 for price in apple_prices]

## 5. Counting Female Names ##

name_counts={}

print(legislators)

for r in legislators:
    if r[3]=="F" and r[7] > 1940:
        name = r[1]
        if name in name_counts:
            name_counts[name]=name_counts[name]+1
        else:
            name_counts[name]=1
       

## 7. Comparing with None ##

values = [None, 10, 20, 30, None, 50]
checks = []
checks = [x is not None and x>30 for x in values]
        

## 8. Highest Female Name Count ##

max_value=None
for k in name_counts:
    count=name_counts[k]
    if max_value is None or count>max_value:
        max_value=count
print(max_value)

## 9. The Items Method ##

plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}

for k,v in plant_types.items():
    print(k)
    print(v)
    

## 10. Finding the Most Common Female Names ##

top_female_names = []

for k in name_counts:
    if name_counts[k]==2:
        top_female_names.append(k)
        

## 11. Finding the Most Common Male Names ##

top_male_names = []
male_name_counts = {}
for row in legislators:
    if row[3] == "M" and row[7] > 1940:
        name = row[1]
        if name in male_name_counts:
            male_name_counts[name] = male_name_counts[name] + 1
        else:
            male_name_counts[name] = 1
            
highest_male_count = None
for name,count in male_name_counts.items():
    if highest_male_count is None or count > highest_male_count:
        highest_male_count = count

for name,count in male_name_counts.items():
    if count == highest_male_count:
        top_male_names.append(name)