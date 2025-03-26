n = int(input())

course_dic = {}

for i in range(n):
    line = input().split()
    if line[-1] not in course_dic:
        course_dic[line[-1]] = {line[0] + " " + line[1]}
        continue
    
    course_dic[line[-1]].add(line[0] + " " + line[1])

courses = course_dic.keys()
courses = sorted(courses)

course_dic_sorted = {course: course_dic[course] for course in courses}

for key, val in course_dic_sorted.items():
    print(key, len(val))
    

