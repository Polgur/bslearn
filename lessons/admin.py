from django.contrib import admin
from .models import Tag, Book, Lesson

# Register your models here.
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)

class LessonInline(admin.StackedInline):
    model = Lesson

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'year', 'link',)
    ordering = ('name',)
    inlines = [
        LessonInline,
    ]

admin.site.register(Tag,TagAdmin)
admin.site.register(Book,BookAdmin)