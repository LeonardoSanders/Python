def gradingStudents(grades):
    numbers = grades
    cont_num = 0
    
    for n in numbers:
        if n >= 38:
            for i in range(1, 6):
                if (n + i) % 5 == 0:
                    if (n + i) - n < 3:
                        numbers[cont_num] = n + i
        cont_num += 1
        
    return numbers


result = gradingStudents([73, 67, 40, 33])
print(result)