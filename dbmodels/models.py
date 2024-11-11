from tortoise.fields import CASCADE
from tortoise.models import Model
from tortoise import fields

# 学生表
class Student(Model):
    id = fields.IntField(pk=True, auto_increment=True)
    name = fields.CharField(max_length=50)
    age = fields.IntField()
    email = fields.CharField(max_length=50, unique=True)
    sno = fields.CharField(max_length=50, unique=True)
    password = fields.CharField(max_length=255)
    teacher = fields.ForeignKeyField("models.Teacher", related_name="students", on_delete=fields.NO_ACTION)
    clas = fields.ManyToManyField("models.Clas", related_name="students")
    course = fields.ManyToManyField("models.Course", related_name="students")

# 老师表
class Teacher(Model):
    id = fields.IntField(pk=True, auto_increment=True)
    name = fields.CharField(max_length=50)
    age = fields.IntField()
    email = fields.CharField(max_length=50, unique=True)
    tno = fields.CharField(max_length=50, unique=True)
    password = fields.CharField(max_length=255)
    clas = fields.ManyToManyField("models.Clas", related_name="teachers", CASCADE=False)
    course = fields.ManyToManyField("models.Course", related_name="teachers", CASCADE=False)

# 班级表
class Clas(Model):
    id = fields.IntField(pk=True, auto_increment=True)
    name = fields.CharField(max_length=50)
    course = fields.ManyToManyField("models.Course", related_name="classes", CASCADE=False)

# 课程表
class Course(Model):
    id = fields.IntField(pk=True, auto_increment=True)
    name = fields.CharField(max_length=50)
    add = fields.CharField(max_length=50, default='')
    major = fields.ForeignKeyField("models.Major", related_name="courses", CASCADE=False)


# 分数表
class Score(Model):
    id = fields.IntField(pk=True, auto_increment=True)
    score = fields.FloatField()
    course = fields.ManyToManyField("models.Course", related_name="scores", CASCADE=False)
    student = fields.ManyToManyField("models.Student", related_name="scores", CASCADE=False)


# 专业表
class Major(Model):
    id = fields.IntField(pk=True, auto_increment=True)
    name = fields.CharField(max_length=50)
