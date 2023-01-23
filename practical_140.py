# 140. Word Break II   

s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
results = []

def helper(i, path):

            if s[i:] in wordDict:

                results.append(" ".join(path + [s[i:]]))
                
            for j in range(i, len(s)):

                if s[i:j] in wordDict:

                    path.append(s[i:j])
                    helper(j, path)
                    path.pop()
        
helper(0, [])
print(results)   