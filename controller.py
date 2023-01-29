import view, import_data, export_data
from statistics import mean

def start():       
    while True:
        action = view.menu_action()
        if action == 1: # Добавление нового ученика
            student = import_data.new_student()  
            data[student] = {}   
            students_list.append(student)   
            if subjects_list:
                for subj in subjects_list:
                    data[student][subj] = []

        if action == 2: # Добавление нового предмета
            subj = import_data.new_subj()            
            subjects_list.append(subj)
            for student in students_list:
                data[student][subj] = []    

        if action == 3: # Добавление новой оценки
            student, subj, est = import_data.new_est()                         
            data[student][subj].append(est) 

        # Артур, в этом месте у меня вопрос: 
        # программа ругается, что для словарей метод append не подходит (строка 23), однако оценки добавляет
        # но при попытке создать словарь {предмет: оценка} путем subjects_data[subj].append(est) программа 
        # уже не работает и выдает ошибку, что для словаря метод append не работает.  
        # в итоге 7 пункт меню я не доделал
        # Заранее спасибо за пояснения.                
           
        if action == 4: # Показ списка учеников
            print(data)

        if action == 5: # Показ оценок ученика
            student = export_data.print_est_student()
            print(f"Средняя оценка {data[student]}")

        if action == 6: # Вывод средней оценки ученика по какому-либо предмету
            student, subj = export_data.midle_est_student()
            midle_est = mean(data[student][subj])
            print(midle_est)         
        
        if action == 0: # Выход из программы
            break 

data = {}
students_list = []
subjects_list = []

# subjects_data = {}
