if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    answer = student_marks.get(query_name, [])
    final_answer = sum(answer) / 3
    final_final_answer = f"{final_answer:.2f}"   
    print(final_final_answer)   