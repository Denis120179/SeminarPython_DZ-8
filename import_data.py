def new_student():
    student = input("Введите фамилию и имя через пробел:  ")    
    print("Данные по новому ученику сохранены")  
    return student

def new_subj():
    subj = input("Введите предмет:  ")    
    print("Данные по новому предмету сохранены")
    return subj

def new_est():
    student = input("Введите фамилию и имя ученика:  ")
    subj = input("Введите предмет:  ")
    est = int(input("Введите оценку:  "))
    print("Данные по новой оценке сохранены")
    return student, subj, est
