#Write a code to search a user input integer in a list(unsorted) in python
#If element is present, return its count, else return 0
#Complete the function
def find_element(n:int, l:list)->int:
    #Write your code here
def find_count(n:int)->int:
    #Write your code here
if __name__=='__main__':
    l = list(map(int, input().split()))
    n = int(input())
    print(find_count(find_element(n, l)))
