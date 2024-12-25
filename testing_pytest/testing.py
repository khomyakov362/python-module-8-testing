import pytest
from main import Teacher, SubjectTeacher

@pytest.fixture
def teacher_name():
    return 'Владимир'

@pytest.fixture
def teacher_education():
    return 'МГУ'

@pytest.fixture
def teacher_experience():
    return 6

@pytest.fixture
def student():
    return 'Вова'

@pytest.fixture
def mark():
    return 5

@pytest.fixture
def group():
    return '7A'

@pytest.fixture
def subject_teacher_subject():
    return 'Химия'

@pytest.fixture
def subject_teacher_job_title():
    return 'завуч'

@pytest.fixture
def teacher(teacher_name, teacher_education, teacher_experience):
    return Teacher(teacher_name, teacher_education, teacher_experience)

@pytest.fixture
def subject_teacher(teacher_name, teacher_education, teacher_experience, subject_teacher_subject, subject_teacher_job_title):
    return SubjectTeacher(teacher_name, teacher_education, teacher_experience, subject_teacher_subject, subject_teacher_job_title)

def test_teacher_getters(teacher, teacher_name, teacher_education, teacher_experience):
    assert teacher.name == teacher_name
    assert teacher.education == teacher_education
    assert teacher.experience == teacher_experience

def test_techer_experience_setter(teacher):
    teacher.experience = 9
    assert teacher.experience == 9
    teacher.experience = 6

def test_get_teacher_data(teacher, teacher_name, teacher_education, teacher_experience):
    assert teacher.get_teacher_data() == f'{teacher_name}, образование: {teacher_education}, опыт: {teacher_experience} года.'

def test_add_mark(teacher, student, mark):
    assert teacher.add_mark(student, mark) == f'Учитель {teacher.name} поставил {mark} ученику {student}.'

def test_remove_mark(teacher, student, mark):
    assert teacher.remove_mark(student, mark) == f'Учитель {teacher.name} удалил оценку {mark} у ученика {student}.'

def test_give_consultation(teacher, group):
    assert teacher.give_consultation(group) == f'Учитель {teacher.name} провёл консультацию в {group}.'

def test_fire_teacher(teacher):
    length = len(Teacher.all_teachers)
    teacher.fire_teacher()
    assert length == len(Teacher.all_teachers) + 1

def test_display_teachers(teacher_name, teacher_education, teacher_experience):
    all_teachers_string = (f'{teacher_name}, образование: {teacher_education}, опыт: {teacher_experience} года.\n' * len(Teacher.all_teachers))[0:-1]
    assert Teacher.display_teachers() == all_teachers_string
    Teacher.all_teachers = []
    assert Teacher.display_teachers() == 'There are no teachers.'

def test_subject_teacher_getters(subject_teacher, subject_teacher_subject, subject_teacher_job_title):
    assert subject_teacher.subject == subject_teacher_subject
    assert subject_teacher.job_title == subject_teacher_job_title

def test_subject_teacher_job_title_setter(subject_teacher):
    subject_teacher.job_title = 'teacher'
    assert subject_teacher.job_title == 'teacher'

def test_subject_teacher_add_mark(subject_teacher, student, mark):
    assert subject_teacher.add_mark(student, mark) == f'Учитель {subject_teacher.name} поставил {mark} ученику {student}.\nПредмет: {subject_teacher.subject}'

def test_subject_teacher_remove_mark(subject_teacher, student, mark):
    assert subject_teacher.remove_mark(student, mark) == f'Учитель {subject_teacher.name} удалил оценку {mark} у ученика {student}.\nПредмет: {subject_teacher.subject}'

def test_subject_teacher_give_consultation(subject_teacher, group):
    assert subject_teacher.give_consultation(group) == f'Учитель {subject_teacher.name} провёл консультацию в {group}.\nПо предмету: {subject_teacher.subject}, как {subject_teacher.job_title}.'

def test_get_subject_teacher_data(subject_teacher, teacher_name, teacher_education, teacher_experience, subject_teacher_subject, subject_teacher_job_title):
    assert subject_teacher.get_teacher_data() == f'{teacher_name}, образование: {teacher_education}, опыт: {teacher_experience} года.\nПредмет: {subject_teacher_subject}, должность: {subject_teacher_job_title}.'
