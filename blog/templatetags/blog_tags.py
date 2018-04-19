from django import template
from ..models import Post,Category

register=template.Library()
#自定义模板标签，显示最近的文章列表，侧边栏
@register.simple_tag
def get_recent_posts(num=5):
	return Post.objects.all().order_by('-create_time')[:num]


@register.simple_tag
def archives():
	return Post.objects.dates('create_time','month',order='DESC')



@register.simple_tag
def get_categories():
	return Category.objects.all()


