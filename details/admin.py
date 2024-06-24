from django.contrib import admin

from .models import LibraryMember,User,BooksDetails,image
class UserDetails(admin.ModelAdmin):
    list_display=['username','password','is_admin']

class LibraryMemberList(admin.ModelAdmin):
    list_display=['Name','Book_title','Date']
class BooksDetailss(admin.ModelAdmin):
    list_display = ['id','image','Title', 'author',  'Quantity',]  
class imagelist(admin.ModelAdmin):
    list_display=['Name','Date','photo']

admin.site.register(LibraryMember,LibraryMemberList)
admin.site.register(User,UserDetails)
admin.site.register(BooksDetails,BooksDetailss)
admin.site.register(image,imagelist)
