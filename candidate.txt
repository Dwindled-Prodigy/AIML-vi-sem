import csv

with open("training.csv") as f:
    csv_file = csv.reader(f)
    data = list(csv_file)
    specific = data[1][:-1]
    general = [['?' for i in range(len(specific))] for j in range(len(specific))]

    for i in data[1:]:
        if i[-1] == "Yes":
            for j in range(len(specific)):
                if(i[j] != specific[j]):
                    specific[j] = "?"
                    general[j][j] = '?'
                
        elif i[-1] == 'No':
            for j in range(len(specific)):
                if i[j] != specific[j]:
                    general[j][j] = specific[j]
                else:
                    general[j][j] = "?"
    
        print(f"Step {data.index(i)} of candidate elimination: ")
        print(specific)
        print(general)

    gh = []
    for i in general:
        for j in i:
            if j != '?':
                gh.append(i)
                break
    
    print("Final specific hypothesis:", specific)
    print("Final general hypothesis:", gh)