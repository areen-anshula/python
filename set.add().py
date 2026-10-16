n = int(input())
s = set()
for i in range(n):
    country_name = input()
    s.add(country_name)
    
distinct_countries_count = len(s) 
print(distinct_countries_count)   