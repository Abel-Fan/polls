from django.contrib import admin
from .models import Questions,Choices
from django.utils.html import format_html

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choices
    max_num = 3
    extra = 1

@admin.register(Questions)
class QuestionAdmin(admin.ModelAdmin):
    """
    创建 question 模型的后台
    """
    list_display = ('question_text','pub_date')
    search_fields = ('questions_text',)
    inlines = [ChoiceInline,]




@admin.register(Choices)
class ChoiceAdmin(admin.ModelAdmin):
    """
    创建 question 模型的后台
    """
    def list_votes(self,obj):
        return  format_html('<div style="color:blue;">%s</div>'%(str(obj.votes) + '个'))
    list_display = ('choice_text','list_votes','votes')
    search_fields = ('choice_text',)
    list_filter = ('question',)