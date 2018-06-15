from django.contrib import admin
from meetup.models import Category, Meetup, Group
from django.contrib.auth.models import User


def make_staff(modeladmin, something, queryset):
    queryset.update(is_staff=True)
    modeladmin.description = "Make selected user staff user"


class UserAdmin(admin.ModelAdmin):

    list_display = ('username', 'email', 'is_staff')
    actions = [make_staff]


class MeetupAdmin(admin.ModelAdmin):

    list_display = ('meetup_group', 'meetup_place', 'meetup_date_time')
    list_filter = ['meetup_date_time']
    search_fields = ['meetup_group']


class GroupAdmin(admin.ModelAdmin):

    list_display = ('name', 'group_description', 'group_category')
    search_fields = ['name']


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Category)
