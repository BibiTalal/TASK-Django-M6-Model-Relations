from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=30)


class Lecture(models.Model):
    name = models.CharField(max_length=30)
    # many-to-one: lecture is many to check run : pytest -k many_to_one
    _course=models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lectures")

    def __str__(self):
        return self.name


class Slide(models.Model):
    name = models.CharField(max_length=30)
    link = models.URLField()
    # one-to-one to check run: pytest -k one_to_one
    lecture=models.OneToOneField(Lecture, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.name


class Assignment(models.Model):
    name = models.CharField(max_length=30)
    link = models.URLField()
    lecture=models.OneToOneField(Lecture,on_delete=models.CASCADE,primary_key=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=30)
    # many-to-many to check run: pytest -k many_to_many
    courses=models.ManyToManyField(Course, related_name="tags")

    def __str__(self):
        return self.name
