class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # creating the hashmap
        hashmap = {} 
        #resultant array
        result = []
        #array with none values to the lenght of nums
        bucket = [None for i in range(len(nums)+1)] 

        
        #iterate through the nums array 
        for num in nums: 
            #if it is not present in hashmap
            if num in hashmap:
                #hashmap key to one 
                hashmap[num] +=1

            else:
                #set the initial freq to 1
                hashmap[num] = 1 

        #iterate through the key and value pair in hashmap       
        for key,val in hashmap.items(): 
            #if not  bucket value 
            if not bucket[val]:
                bucket[val]=[]
                #append the bucket array 
            bucket[val].append(key)

            #iterate through the bucket in reverse 
        for i in range(len(bucket)-1,-1,-1):
            #if bucket value is there 
            if bucket[i]:
                #add it to the result 
                result += bucket[i]
                #resuce the bucket length
                k-=len(bucket[i])
# if k is equal to 0 then break
            if k == 0: 
                break
        return result 

        