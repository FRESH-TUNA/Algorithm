# https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phoneBook):
    phonebook_set = {phone for phone in phoneBook}
    for phone in phoneBook:
        for i in range(1, len(phone)):
            if phone[0:i] in phonebook_set: return False
    return True
