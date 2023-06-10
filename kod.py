
def stroc(s: str):
    
    for sym in s:
        counter = 0
        for sub_sum in s:
            if sym == sub_sum:
                counter += 1
        
        print(sym, counter)
        
stroc("hello")