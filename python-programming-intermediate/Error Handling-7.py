## 2. Sets ##

print(legislators)
gender=[]
for l in legislators:
    gender.append(l[3])
    
gender=set(gender)
print(gender)

    

## 3. Exploring the Dataset ##

party = []
for item in legislators:
    party.append(item[6])

party = set(party)
print(party)

print(legislators)
    
    

## 4. Missing Values ##

gender=[]
for g in legislators:
    if g[3] =="":
        g[3]="M"
    gender.append(g[3])

gender=set(gender)
print(gender)
print(legislators)
        

## 5. Parsing Birth Years ##

birth_years=[]
for b in legislators:
    parts = b[2].split("-")
    birth_years.append(parts[0])
    
    
print(set(birth_years))

## 6. Try/except Blocks ##

try:
    float("hello")
except Exception:
    print("Error converting to float.")

## 7. Exception Instances ##

try:
    int('')
except Exception as exe:
    print(str(exe))
    print(type(exe))

## 8. The Pass Keyword ##

converted_years = []

for year in birth_years:
    try:
        year =int(year)
    except Exception:
        pass
    converted_years.append(year)
    
    
    

## 9. Convert Birth Years to Integers ##



for r in legislators:
    birth_year=r[2].split("-")[0]
    
    try:
        birth_year=int(birth_year)
    except Exception:
        birth_year=0
    r.append(birth_year)

## 10. Fill in Years Without a Value ##

last_value=1

for row in legislators:
    if row[7]==0:
        row[7]= last_value
    last_value=row[7]
