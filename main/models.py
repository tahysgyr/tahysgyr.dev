from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
	title = models.CharField('Заголовок', max_length=80)

	def __str__(self) -> str:
		return self.title

class Blog(models.Model):
	id_blog = models.IntegerField("Номер новости", null=True)
	title = models.CharField("Заголовок", max_length=120, null=True)
	image = models.ImageField("Изображение", upload_to='users/%Y/%m/%d', blank=True, null=True)
	description = models.CharField("Описание", max_length=350, null=True)
	date = models.DateField("Дата публикации", null=True)
	user = models.CharField("Опубликовал", max_length=21, null=True)
	tag = models.ForeignKey('Tag', on_delete=models.PROTECT, null=True)

	@property
	def image_url(self):
		if self.image and hasattr(self.image, 'url'):
			return self.image.url

	def __str__(self):
		return f'{self.title} {self.image} {self.description} {self.date} {self.user}'
	
	class Meta():
		verbose_name = 'Весть'
		verbose_name_plural = 'Вести'