def solution(id_list, report, k):
    answer = []
   
    #report에서 중복되는 항목 제거
    report = list(set(report))
   
    #id_list를 key로 갖는 value 0인 딕셔너리 생성
    id_dict = {id : 0 for id in id_list}
    id_dict2 = {id : 0 for id in id_list}
   
    #split 해서 신고자와 신고 당한 사람 나누기
    splitted_report = [r.split() for r in report]

    #신고 당했을 경우 id_dict에 value 1씩 더해줌
    for report_idx in range(len(report)):
        id_dict[splitted_report[report_idx][1]] += 1

    #신고 당한 횟수 k번 이상인 경우 신고한 사람 id_dict2에 value 1씩 더해줌    
    for report_idx in range(len(report)):
        if id_dict[splitted_report[report_idx][1]] >= k:
            id_dict2[splitted_report[report_idx][0]] += 1

    #id_dict의 value값 answer에 추가        
    answer = list(id_dict2.values())

    return answer
