from django.db import models

# Create your models here.

class Questions(models.Model):
    # id可以省略
    class Meta:  # 元类
        db_table = "questions"
        verbose_name="问题"
        verbose_name_plural="问题"

    question_text = models.CharField(max_length=200,verbose_name="问题")
    pub_date = models.DateTimeField(verbose_name="问题")

    def __str__(self):
        return self.question_text

class Choices(models.Model):
    class Meta:  # 元类
        db_table = "choices"
        verbose_name = "选项"
        verbose_name_plural = "选项"
    question = models.ForeignKey(Questions,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200,verbose_name="选项")
    votes = models.IntegerField(default=0,verbose_name="数量")

    def __str__(self):
        return  self.choice_text

