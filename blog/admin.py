from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import User
from .models import Post
from .models import Comment
from blog.models import UserProfile

admin.site.register(Post)
admin.site.register(Comment)


class UserProfileInline(admin.TabularInline):
    model = UserProfile


class UserAdmin(DjangoUserAdmin):
    inlines = (UserProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
