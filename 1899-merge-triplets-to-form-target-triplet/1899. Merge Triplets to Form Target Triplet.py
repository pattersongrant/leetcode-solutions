class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        t_a, t_b, t_c = target
        possible_a = []
        possible_b = []
        possible_c = []
        for a, b, c in triplets:
            if a == t_a and b <= t_b and c <= t_c:
                possible_a = [a,b,c]
            if a <= t_a and b == t_b and c <= t_c:
                possible_b = [a,b,c]
            if a <= t_a and b <= t_b and c == t_c:
                possible_c = [a,b,c]
        if not (possible_a and possible_b and possible_c):
            return False
        test = [max(possible_a[0], possible_b[0], possible_c[0]),
                max(possible_a[1], possible_b[1], possible_c[1]),
                max(possible_a[2], possible_b[2], possible_c[2])]
        return test == target
            
            

           

            

            
        