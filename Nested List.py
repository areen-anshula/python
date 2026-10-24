if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input().strip()
        score = float(input())
        records.append([name, score])
        
sorted_record = sorted(records, key=lambda x:x[1])
unique_scores = sorted(set(record[1] for record in records))
second_lowest = unique_scores[1]
names = []
for record in  records:
    if record[1] == second_lowest:
        names.append(record[0])
sorted_names = sorted(names)        
print(*sorted_names, sep="\n")        