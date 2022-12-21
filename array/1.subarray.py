class Solution:
    def subArraySum(self,arr,n,s):
        for i in range(n):
            curr_sum = arr[0]
            start = 0

            while curr_sum > s and start < i-1:
                curr_sum-=arr[start]
                start+=1        
               
           
            if curr_sum == s:
                return [start, i-1]
            
            if i<n:
                curr_sum+=arr[i]
                
        return [-1]             
                


import math
def main():
    T=int(input())
    while(T>0):
        NS=input().strip().split()
        N=int(NS[0])
        S=int(NS[1])
        
        A=list(map(int,input().split()))
        ob=Solution()
        ans=ob.subArraySum(A,N,S)
        
        for i in ans:
            print(i,end=" ")
            
        print()
        
        T-=1
        
if __name__ == "__main__":
    main()