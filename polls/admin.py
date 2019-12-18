from django.contrib import admin

# Register your models here.
from polls.models import Question, Choice


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),  # 위에 컬럼 이름을 바꾼다
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),  # 필드 작성 이름을 변경 한다
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
