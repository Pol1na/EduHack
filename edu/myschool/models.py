from django.db import models
from django.conf import settings


class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название предмета')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
        ordering = ['name']


class SchoolClass(models.Model):
    number = models.CharField(max_length=2, verbose_name='Номер класса')
    letter = models.CharField(max_length=1, verbose_name='Буква класса')
    school = models.ForeignKey('accounts.school', on_delete=models.CASCADE, verbose_name='Школа')

    def __str__(self):
        return f'{self.number}{self.letter}'

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'
        ordering = ['number']


class Teacher(models.Model):
    user = models.OneToOneField('accounts.customuser', on_delete=models.CASCADE, primary_key=True,
                                verbose_name='Пользователь')
    school_class = models.ForeignKey(SchoolClass, default=1, on_delete=models.CASCADE, verbose_name='Класс.рук')
    school = models.ForeignKey('accounts.school', on_delete=models.CASCADE, default=1 ,verbose_name='Школа')
    subject = models.ManyToManyField(Subject, verbose_name='Преподаваемые предметы', blank=True)
    work_exp = models.CharField(max_length=50, verbose_name='Стаж работы', blank=True)
    achievement = models.CharField(max_length=500, verbose_name='Достижения', blank=True)
    about = models.CharField(max_length=150, verbose_name='О учителе', blank=True)
    is_boss = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.name} {self.user.last_name}'

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'


class Student(models.Model):
    user = models.OneToOneField('accounts.customuser', on_delete=models.CASCADE, primary_key=True,
                                verbose_name='Пользователь')
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, default=1, verbose_name='Класс')
    date_add = models.DateField(verbose_name='Дата поступления', null=True, blank=True)
    date_end = models.DateField(verbose_name='Дата выпуска', blank=True, null=True)
    amount_hold_back = models.BinaryField(editable=True, verbose_name='Количество оставлений на второй год', null=True,
                                          blank=True)

    def __str__(self):
        return f'{self.user.name}{self.user.last_name}'

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Студент')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Предмет')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Учитель')
    date = models.DateField(auto_now_add=True, verbose_name='Дата оценки')
    mark = models.CharField(max_length=1, verbose_name='Оценка')
    description = models.CharField(max_length=150, null=True, verbose_name='Примечание')

    def __str__(self):
        return self.mark

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
        ordering = ['date']


class Parent(models.Model):
    user = models.OneToOneField('accounts.customuser', on_delete=models.CASCADE, primary_key=True,
                                verbose_name='Пользователь')
    student = models.ManyToManyField(Student, verbose_name='Ребёнок')

    def __str__(self):
        return f"{self.user.name} {self.user.last_name}"

    class Meta:
        verbose_name = 'Родитель'
        verbose_name_plural = 'Родители'


class Homework(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='По какому предмету д/з')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Кто задал?')
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, verbose_name='Кому задана?')
    name = models.CharField(max_length=150, verbose_name='Название д/з')
    description = models.CharField(max_length=300, null=True, verbose_name='Текст д/з')
    date_add = models.DateField(verbose_name='Дата выкладывания д/з', auto_now_add=True, blank=True)
    date_end = models.DateField(verbose_name='Дата завершения приема работ', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Домашнее задание'
        verbose_name_plural = 'Домашние задания'
        ordering = ['date_add']


class HomeworkForStudent(models.Model):
    homework = models.OneToOneField(Homework, on_delete=models.CASCADE, verbose_name='Домашнее задание')
    student = models.OneToOneField(Student, on_delete=models.CASCADE, verbose_name='Ученик')
    solution = models.CharField(max_length=200, verbose_name='Ссылка на файл с решением', blank=True, null=True)
    text_solution = models.CharField(max_length=500, verbose_name='Примечание')
    is_ready = models.BooleanField(default=False, verbose_name='Выполнено?')
    is_archived = models.BooleanField(default=False, verbose_name='Архивировано?')
    mark = models.IntegerField(verbose_name='Оценка', null=True, blank=True)

    def __str__(self):
        return self.homework.name

    class Meta:
        verbose_name = 'Домашнее задание для ученика'
        verbose_name_plural = 'Домашние задания для ученика'
        ordering = ['homework']


class SchoolCab(models.Model):
    name = models.CharField(max_length=10, verbose_name='Номер кабинета')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Кабинет'
        verbose_name_plural = 'Кабинеты'
        ordering = ['name']


class Schedule(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Урок')
    date = models.DateField(verbose_name='Дата', null=True, blank=True)
    number_lesson = models.CharField(max_length=3, verbose_name='Номер урока')
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, verbose_name='Класс')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Преподаватель')
    school_cab = models.ForeignKey(SchoolCab, on_delete=models.CASCADE, verbose_name='Кабинет')

    def __str__(self):
        return f"{self.subject.name} {self.date} {self.school_class}"

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'
        ordering = ['date']
