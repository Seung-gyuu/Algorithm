def solution(rank, attendance):
    # n명의 학생 중 참여가능한 학생 중 등수가 높은 3명을 선발

    #create a list of tuple
    students = [(i, rank[i], attendance[i]) for i in range(len(rank))]
    # sort list by rank
    sorted_students = sorted(students, key=lambda x: x[1])
    #calculate 10000 × a + 100 × b + c
    ranks = []
    for i , rank, a in sorted_students:
        if a:
            ranks.append(i)
            if len(ranks) == 3:
                return 10000 * ranks[0] + 100 * ranks[1] + ranks[2]


