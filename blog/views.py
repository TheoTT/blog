from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post,Tag,Category
import markdown
from comments.forms import CommentForm

#def index(request):
#	post_list=Post.objects.all().order_by('-create_time')
#	
#	return render(request,'blog/index.html',context={'post_list':post_list})
#	return render(request, 'blog/index.html', context={
#                      'title': '我的博客首页', 
#                      'welcome': '欢迎访问我的博客首页'
#                  })

#主页的视图函数
def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', context={'post_list': post_list})

#文章详情页的视图函数
def detail(request,pk):
	post = get_object_or_404(Post,pk=pk)
	#使用markdown修饰显示的文章内容
	post.body = markdown.markdown(post.body,extention=['markdown.extensions.extra','markdown.extensions.codehilite''markdown.extensions.toc',])
	
	form = CommentForm()
	 # 获取这篇 post 下的全部评论
	comment_list = post.comment_set.all()

	# 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
	context = {'post': post,'form': form,'comment_list': comment_list
               }


	return render(request,'blog/detail.html',context=context)

#侧边栏归档页面视图函数
def archives(request,year,month):
	post_list=Post.objects.filter(create_time__year=year,create_time__month=month).order_by('-create_time')
	return render(request,'blog/index.html',context={'post_list':post_list})

#侧边栏分类页面视图函数
def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request, 'blog/index.html', context={'post_list': post_list})


