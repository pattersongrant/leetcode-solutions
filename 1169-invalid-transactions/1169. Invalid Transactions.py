class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:

        for i in range(len(transactions)):
            transactions[i] = transactions[i].split(",")

        for t in transactions:
            
            time = t[1]
            t[1] = t[0]
            t[0] = time
        
        transactions.sort()

        people = defaultdict(list) #name : [[rest of data]]
        res = []
        

        for t in transactions:
            people[t[1]].append([t[0], t[2], t[3]])
        
        for name in people:
            seen = set()
            for i in range(len(people[name])):
                j = i

                while j >= 0:
                    if (people[name][i][2] != people[name][j][2] and 
                        abs(int(people[name][i][0]) - int(people[name][j][0])) <= 60):
                        if i not in seen:
                            res.append([name, people[name][i][0], people[name][i][1], people[name][i][2]])
                            seen.add(i)
                        if j not in seen:
                            res.append([name, people[name][j][0], people[name][j][1], people[name][j][2]])
                            seen.add(j)
                                                
                    elif int(people[name][j][1]) > 1000:
                        if j not in seen:
                            res.append([name, people[name][j][0], people[name][j][1], people[name][j][2]])
                            seen.add(j)
                    j -= 1
        

        for i in range(len(res)):
            res[i] = (",").join(res[i])
        return res

                


        

        