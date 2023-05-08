class Student:
    def __init__(self, email, name, surname):
        self.all_grade = {
            "project": -1,
            "l_1": -1,
            "l_2": -1,
            "l_3": -1,
            "h_1": -1,
            "h_2": -1,
            "h_3": -1,
            "h_4": -1,
            "h_5": -1,
            "h_6": -1,
            "h_7": -1,
            "h_8": -1,
            "h_9": -1,
            "h_10": -1,
            "grade": -1,
        }
        self.email = email
        self.name = name
        self.surname = surname
        self.status = None

    def __str__(self):
        return "Email: " + self.email + "\nName: " + self.name + "\nSurname: " + self.surname + "\nAll grades: " + str(
            self.all_grade) + "\nStatus: " + str(self.status)

    def add_grade(self, grade_type, grade):
        self.all_grade[grade_type] = grade

    def calculate_grade(self):
        project_grade = self.all_grade['project']
        list_grades = [self.all_grade['l_1'], self.all_grade['l_2'], self.all_grade['l_3']]
        homework_grades = [self.all_grade['h_1'], self.all_grade['h_2'], self.all_grade['h_3'], self.all_grade['h_4'],
                           self.all_grade['h_5'], self.all_grade['h_6'], self.all_grade['h_7'], self.all_grade['h_8'],
                           self.all_grade['h_9'], self.all_grade['h_10']]

        # Check if all grades are available
        if project_grade == -1 or -1 in list_grades or -1 in homework_grades:
            print("Cannot calculate grade, missing some grades")
            return

        # Calculate grade
        grade = project_grade + sum(list_grades) * 20

        # Update list grades based on homework average
        homework_avg = sum(homework_grades) / len(homework_grades)
        if homework_avg >= 80:
            grade += 60
            if self.all_grade['l_1'] == min(list_grades):
                list_grades[list_grades.index(min(list_grades))] = 20
            elif self.all_grade['l_2'] == min(list_grades):
                list_grades[list_grades.index(min(list_grades))] = 20
            elif self.all_grade['l_3'] == min(list_grades):
                list_grades[list_grades.index(min(list_grades))] = 20
        elif homework_avg >= 70:
            grade += 40
            if self.all_grade['l_1'] == min(list_grades):
                list_grades[list_grades.index(min(list_grades))] = 20
                if self.all_grade['l_2'] == min(list_grades):
                    list_grades[list_grades.index(min(list_grades))] = 20
            elif self.all_grade['l_3'] == min(list_grades):
                list_grades[list_grades.index(min(list_grades))] = 20
                if self.all_grade['l_2'] == min(list_grades):
                    list_grades[list_grades.index(min(list_grades))] = 20
            elif self.all_grade['l_2'] == min(list_grades):
                list_grades[list_grades.index(min(list_grades))] = 20
                if self.all_grade['l_1'] == min(list_grades):
                    list_grades[list_grades.index(min(list_grades))] = 20

                    # Update dictionary with new grades
                    self.all_grade['l_1'] = list_grades[0]
                    self.all_grade['l_2'] = list_grades[1]
                    self.all_grade['l_3'] = list_grades[2]
                    self.all_grade['grade'] = grade

                    # Update status
                    if grade >= 90:
                        self.status = "A"
                    elif grade >= 80:
                        self.status = "B"
                    elif grade >= 70:
                        self.status = "C"
                    elif grade >= 60:
                        self.status = "D"
                    else:
                        self.status = "F"

                    return grade


