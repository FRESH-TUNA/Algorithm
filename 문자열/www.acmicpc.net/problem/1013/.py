import re

def solution():
    REGEX = re.compile('((100+1+)|(01))+$')
    N = int(input())
    NO, YES = "NO", "YES"
    
    def check(data):
        return re.match(REGEX, data) != None

    def call():
        for _ in range(N):
            print([NO, YES][check(input())])
    call()

solution()
