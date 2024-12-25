# task 1

class Teacher:
    
    all_teachers = []

    def __init__(self, name, education, experience):
        self.__name = name
        self.__education = education
        self.__experience = experience
        Teacher.all_teachers.append(self)

    @property
    def name(self):
        return self.__name

    @property
    def education(self):
        return self.__education

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, years):
        self.__experience = years

    def get_teacher_data(self):
        string = f'{self.__name}, образование: {self.__education}, опыт: {self.__experience} года.'
        print(string)
        return string

    def add_mark(self, student, mark):
        string = f'Учитель {self.__name} поставил {mark} ученику {student}.'
        print(string)
        return (string)

    def remove_mark(self, student, mark):
        string = f'Учитель {self.__name} удалил оценку {mark} у ученика {student}.'
        print(string)
        return (string)
    
    def give_consultation(self, group):
        string = f'Учитель {self.__name} провёл консультацию в {group}.'
        print(string)
        return string
    
    def fire_teacher(self):
        Teacher.all_teachers.remove(self)
    
    @classmethod
    def display_teachers(self):
        all_teachers_strings = []
        if Teacher.all_teachers:
            for teacher in Teacher.all_teachers:
                all_teachers_strings.append(teacher.get_teacher_data())
                print()
            return '\n'.join(all_teachers_strings)
        else:
            string = 'There are no teachers.'
            print(string)
            return string
        
        
class SubjectTeacher(Teacher):

    def __init__(self, name, education, experience, subject, job_title):
        Teacher.__init__(self, name, education, experience)
        self.__subject = subject
        self.__job_title = job_title

    @property
    def subject(self):
        return self.__subject

    @property
    def job_title(self):
        return self.__job_title

    @job_title.setter
    def job_title(self, title):
        self.__job_title = title

    def get_teacher_data(self):
        string = f'{self.name}, образование: {self.education}, опыт: {self.experience} года.\nПредмет: {self.subject}, должность: {self.__job_title}.'
        print(string)
        return string

    def add_mark(self, student, mark):
        string = f'Учитель {self.name} поставил {mark} ученику {student}.\nПредмет: {self.subject}'
        print(string)
        return (string)

    def remove_mark(self, student, mark):
        string = f'Учитель {self.name} удалил оценку {mark} у ученика {student}.\nПредмет: {self.subject}'
        print(string)
        return (string)
    
    def give_consultation(self, group):
        string = f'Учитель {self.name} провёл консультацию в {group}.\nПо предмету: {self.subject}, как {self.job_title}.'
        print(string)
        return string
        