from optparse import Values

from django.core.validators import MinValueValidator
from django.db import models
from headhunter_app.validators import MinLengthValidator, WordLengthValidator
from django.db.models.deletion import get_candidate_relations_to_delete
from django.contrib.auth import get_user_model

# Create your models here.
class DeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class IsDeletedMixin(models.Model):
    is_deleted = models.BooleanField(default=False)

    objects = DeleteManager()

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        delete_candidates = get_candidate_relations_to_delete(self.__class__._meta)
        if delete_candidates:
            for rel in delete_candidates:
                if rel.on_delete.__name__ == 'CASCADE' and rel.one_to_many and not rel.hidden:
                    for item in getattr(self, rel.related_name).all():
                        item.delete()
                        
        self.save(update_fields=['is_deleted', ])

    class Meta:
        abstract = True


class TodoTask(IsDeletedMixin):
    title = models.CharField(max_length=25, null=False, blank=False, verbose_name='Название задачи', validators=[MinLengthValidator(3)])
    # description = models.TextField(max_length=500, null=True, blank=True, verbose_name='Описание задачи', validators=[WordLengthValidator(50)])
    # types = models.ManyToManyField(to='todoapp.TaskType', related_name='types', verbose_name='Тип', blank=True)
    # status = models.ForeignKey(to='todoapp.TaskStatus', on_delete=models.RESTRICT, related_name='statuses', verbose_name='Статус')
    # project =  models.ForeignKey(
    #     to='todoapp.TodoProject', 
    #     on_delete=models.CASCADE, 
    #     related_name='project', 
    #     verbose_name='Проект', 
    #     default=1)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return "№{} {}".format(self.pk, self.title) 


class Resume(IsDeletedMixin):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Название задачи',
                          validators=[MinLengthValidator(3)])
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name='Описание задачи', validators=[WordLengthValidator(50)])
    infos = models.ManyToManyField(to='headhunter_app.Info', related_name='infos', verbose_name='Дополнительная информация', blank=True)
    telegram = models.CharField(max_length=50, null=True, blank=True, verbose_name='Телеграм',
                             validators=[MinLengthValidator(3)])
    email =models.EmailField(max_length=50, null=False, blank=False, verbose_name='Email')
    phone_number =models.IntegerField(max_length=12, null=False, blank=False, verbose_name='Телефон')
    facebook = models.CharField(max_length=50, null=True, blank=True, verbose_name='Facebook',
                             validators=[MinLengthValidator(3)])
    linkedin = models.CharField(max_length=50, null=True, blank=True, verbose_name='Linkedin',
                             validators=[MinLengthValidator(3)])
    # status = models.ForeignKey(to='headhunter_app.TaskStatus', on_delete=models.RESTRICT, related_name='statuses', verbose_name='Статус')
    # project =  models.ForeignKey(
    #     to='todoapp.TodoProject',
    #     on_delete=models.CASCADE,
    #     related_name='project',
    #     verbose_name='Проект',
    #     default=1)
    # created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    # updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')


class Info(IsDeletedMixin):
    title = models.CharField(max_length=25, null=False, blank=False, verbose_name='Название поля', validators=[MinLengthValidator(3)])
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name='Описание поля', validators=[WordLengthValidator(50)])
    
    def __str__(self):
        return f"{self.title}"


class Category(IsDeletedMixin):
    title = models.CharField(max_length=20, null=False, blank=False, verbose_name='Категория')

    def __str__(self):
        return f"{self.title}"


class TodoProject(IsDeletedMixin):
    title = models.CharField(max_length=25, null=False, blank=False, verbose_name='Название проекта', validators=[MinLengthValidator(3)])
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name='Описание проекта', validators=[WordLengthValidator(50)])
    # users = models.ManyToManyField(get_user_model(), related_name='projects', verbose_name='Участник проекта', blank=True)
    begin_at = models.DateField(null=False, blank=False, verbose_name='Время начала')
    end_at = models.DateField(null=True, blank=True, verbose_name='Время окончания')

    def __str__(self):
        return "№{} {}".format(self.pk, self.title) 

    class Meta:
        permissions = [
            ('can_edit_users', 'Можно менять участников проекта')
        ]


class Vacancy(IsDeletedMixin):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Название вакансии')
    salary = models.IntegerField(
        null=False, blank=False,
        validators=[MinValueValidator(0)], verbose_name='Заработная плата'
    )
    description = models.TextField(
        max_length=500, null=True, blank=True,
        verbose_name='Детальное описание', validators=[WordLengthValidator(50)]
    )
    experience = models.ForeignKey(
        to='headhunter_app.Experience', on_delete=models.CASCADE,
        related_name='experience', verbose_name='Опыт работы'
    )
    category = models.ForeignKey(
        to='headhunter_app.Category', on_delete=models.CASCADE,
        related_name='category', verbose_name='Категория'
    )


class Experience(models.Model):
    title = models.CharField(max_length=20, null=False, blank=False, verbose_name='Опыт работы')

    def __str__(self):
        return f"{self.title}"


