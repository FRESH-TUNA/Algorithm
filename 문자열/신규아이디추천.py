import re
def solution(new_id):
    # 1-2단계
    new_id = "".join(re.findall("[0-9a-zA-Z-_.]", new_id.lower()))
    # 3-4단계
    new_id = ".".join(re.split("[.]{2,}", new_id)).strip(".")
    # 5단계
    if not len(new_id): new_id = "a"
    # 6단계 
    new_id =  new_id[:15].rstrip(".")
    #7단계
    return new_id.ljust(3, new_id[-1]) if len(new_id) <= 2 else new_id
