from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)


class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Group(models.Model):
    name = models.CharField(max_length=200)
    group_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    group_description = models.TextField()

    def __str__(self):
        return self.name

#
# class Membership(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)


class Meetup(models.Model):
    meetup_group = models.ForeignKey(Group, on_delete=models.CASCADE)
    meetup_date_time = models.DateTimeField('date of meetup')
    meetup_place = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   null=True, blank=True)

    class Meta:
        ordering = ['-meetup_date_time']
