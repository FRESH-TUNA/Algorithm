def solution(record):
    answer = []
    names = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}

    for _record in record:
        _record = _record.split()
        if _record[0] in ['Enter', 'Change']:
            names[_record[1]] = _record[2]

    for _record in record:
        if _record.split()[0] != 'Change':
            answer.append(names[_record.split()[1]] + printer[_record.split()[0]])

    return answer
