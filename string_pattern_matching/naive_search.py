from typing import List 

'''Naive pattern matching'''
#NOTE: the idea is that we are always sliding the pattern over the text and manual checking over each character 
#NOTE: Complexity: O(MN)
def naive_search(pat: str, text: str)-> List[int]: 
    m = len(pat)
    n = len(text)
    res = [] 

    for i in range(n - m + 1): 

        match = True 

        for j in range(m): 

            if text[i+j] != pat[j]: 
                match = False
                break 

        if match: 
            res.append(i)

    return res

if __name__ == '__main__': 
    print(naive_search("abc", "abcabc"))
