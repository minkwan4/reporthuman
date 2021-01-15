#
# from django.contrib import admin
# from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin
#
# User = get_user_model()
#
#
from django.contrib.auth.admin import UserAdmin


# class MyUserAdmin(UserAdmin):
#     model = User
#     # 유저 목록
#     list_display = ['username', 'id']
#
#     # 유저 정보 관리 페이지 정보 입력창 추가
#     fieldsets = [
#         (None, {'fields': ['username']}),
#
#     ]
#
#
# admin.site.unregister(User)
# admin.site.register(User, MyUserAdmin)