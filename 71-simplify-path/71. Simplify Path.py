class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []

        start = 0
        for i in range(1, len(path)):
            #double or triple slash turns into one slash
            if start == i-1 and path[i] == "/":
                start = i
            
            elif path[i] == "/": #non-consecutive slash
                end = i
                inside = path[start+1:end]
                if inside == "..":
                    if stack:
                        stack.pop()
                elif inside != ".":
                    stack.append(inside)
                start = end
        if path[len(path)-1] != "/":
            end = len(path)
            inside = path[start+1:end]
            if inside == "..":
                if stack:
                    stack.pop()

            elif inside != ".":
                stack.append(inside)
            start = end

        return "/" + "/".join(stack)

        