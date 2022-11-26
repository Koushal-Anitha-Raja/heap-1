def minMeetingRoom(intervals):
     #Sort first index in the intervals
    start = sorted([i[0] for i in intervals])
    #Sort second index in the intervals 
    end = sorted([i[1] for i in intervals]) 
    #res variable to 0
    res = 0 
    #count variable to 0
    count = 0  
    
    s, e = 0, 0 
    #until s is less than interval length
    while s < len(intervals):   
        #if start value is less than end
        if start[s] < end[e]:   
            s += 1
            count += 1
        else: 
            #else doincrement e and decremnt count
            e += 1
            count -= 1
         #Compare the maximum between res and count and store it in res   
        res = max(res, count)   
    return res 

print(minMeetingRoom([(0,30),(5,10),(15,20)]))