class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        # iterate through list of pairs
#         
        # the number must be in the index 1 N-1 times
        # the number cannot be in the index 0
        # if both conditions are met, return the judge's number. 
        # else return -1
        
        for pair in trust:
            trust_count = {}
            possible = []
            # print(trust_count)
            # print(possible)
            # print(f"person 1 and 2 {person[0], person[1]}")
            if pair[1] not in trust_count:
                trust_count[pair[1]] = 1
                # print(f"trust_count 1 {trust_count}")
                # print(f"possible 1 {possible}")
                # print(f"trust 1 {trust}")
                print(f"pair a and b {pair[0], pair[1]}")
            else:
                trust_count[pair[1]] += 1
                print(f"trust_count else 1 {trust_count}")
            # if trust_count[pair[1]]
            #     print(f"possible else 1 {possible}")
            #     print(f"trust else 1 {trust}")
            #     print(f"pair a and b {pair[0], person[1]}")
            for k, v in trust_count.items():
                if v == N-1:
                    possible.append(k)
                    print(f"trust_count 3 {trust_count}")
                    print(f"possible 3 {possible}")
                    print(f"trust 3 {trust}")
                    print(f"pair a and b {pair[0], pair[1]}")
                    for person in possible:
                        if person not in trust[pair[0]]:
                            return person
                        else:
                            return - 1    
        