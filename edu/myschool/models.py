from django.db import models


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
    school = models.ForeignKey('accounts.school', on_delete=models.CASCADE, verbose_name='Буква класса')

    def __str__(self):
        return f'{self.number}{self.letter}'

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'
        ordering = ['name']


class Teacher(models.Model):
    user = models.OneToOneField('accounts.customuser', on_delete=models.CASCADE, primary_key=True,
                                verbose_name='Пользователь')
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, verbose_name='Класс.рук')
    subject = models.ManyToManyField(Subject, verbose_name='Преподаваемые предметы', blank=True)
    work_exp = models.CharField(max_length=50, verbose_name='Стаж работы')
    achievement = models.CharField(max_length=500, verbose_name='Достижения')
    about = models.CharField(max_length=150, verbose_name='О учителе')
    is_boss = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField('accounts.customuser', on_delete=models.CASCADE, primary_key=True,
                                verbose_name='Пользователь')
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, verbose_name='Класс')
    date_add = models.DateField(verbose_name='Дата поступления')
    date_end = models.DateField(verbose_name='Дата выпуска')
    amount_hold_back = models.BinaryField(editable=True, verbose_name='Количество оставлений на второй год')


class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Студент')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Предмет')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Учитель')
    date = models.DateField(auto_now_add=True, verbose_name='Дата оценки')
    mark = models.CharField(max_length=1, verbose_name='Оценка')
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
