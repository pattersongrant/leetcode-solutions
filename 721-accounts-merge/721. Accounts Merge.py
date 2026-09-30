class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        curRes = ["x"]
        prevRes = []
        while curRes != prevRes:
            emailToId = {} #string : int
            IdToEmail = defaultdict(set) #int : list
            prevRes = curRes
            for i in range(len(accounts)):
                acc = accounts[i]
                cur = i
                for j in range(1, len(acc)):
                    email = acc[j]
                    if email in emailToId:
                        cur = emailToId[email]
                        break
                for j in range(1, len(acc)):
                    emailToId[acc[j]] = cur
                    IdToEmail[cur].add(acc[j])

            res = []

            for i in IdToEmail:
                name = accounts[i][0]
                email_list = list(IdToEmail[i])
                email_list.sort()
                cur = [name]
                cur.extend(email_list)
                res.append(cur)
            accounts = res
            curRes = res
        return curRes
            
            