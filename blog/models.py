from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Post(models.Model):
	#文章标题
	title = models.CharField(max_length=70)
	#文章正文
	body =models.TextField()

	#文章创建时间，最后修改时间
	create_time = models.DateTimeField()
	modified_time = models.DateTimeField()

	#文章摘要
	excerpt = models.CharField(max_length=200,blank=True)

	#分类、标签，外键.文章与分类为多对一（ForeignKey），文章与标签为多对多（ManyToManyField）且可为空
	category = models.ForeignKey(Category,on_delete=models.CASCADE)
	tags = models.ManyToManyField(Tag,blank=True)
	
	#作者
	author = models.ForeignKey(User)
	
	def __str__(self):
		return self.title
	#定义get_absolute_url方法,文章的url
	def get_absolute_url(self):
		return reverse('blog:detail',kwargs={'pk': self.pk})
	
	class Meta:
		ordering = ['-create_time']
