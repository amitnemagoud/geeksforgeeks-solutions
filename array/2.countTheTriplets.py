class Solution:
    def triplets(self,arr,n):
        arr.sort()
        count=0 
        for i in range(2,n):
            left=0 
            right=n-1
            while left < right:
                if arr[left] + arr[right] == arr[i]: 
                    count += 1
                    #print(arr[left], arr[right], "=", arr[i])
                    
                    
                    left+=1 
                    right -= 1
                elif arr[left] + arr[right] < arr[i]:
                    left += 1
                else:
                    right -= 1
        return [count]       



def main():
          
        A=list(map(int,input().split()))
        ob=Solution()
        ans=ob.triplets(A,len(A))
        
        for i in ans:
            print(i,end=" ")
            
        print()
        
    
        
if __name__ == "__main__":
    main()