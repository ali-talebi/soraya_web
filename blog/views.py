from django.shortcuts import render , redirect
from .models import Post  , PostComment
from django.views import View
from .forms import PostCommentForm
from django.contrib import messages

class TotalBlogsView(View) :

    template_name = 'blog/blog-grid.html'

    def setup(self, request , *args , **kwargs ) :
        self.total_data = Post.objects.all()
        return super().setup(request , *args , **kwargs )

    def get(self , request ) :
        return render(request , self.template_name , {'total_blogs' : self.total_data} )





class DetailBlogView(View) :

    form_comment = PostCommentForm
    template_name = 'blog/blog-detail.html'


    def setup(self , request , *args , **kwargs ) :
        self.data = Post.objects.get(id = kwargs['id'])
        self.total_comments =  PostComment.objects.filter( post_selected = self.data )
        self.another_posts  =  Post.objects.all()
        return super().setup(request , *args , **kwargs )


    def get(self , request , id ) :
        return render(request , self.template_name , {'data':self.data , 'another_posts' : self.another_posts  , 'form' : self.form_comment , 'total_comment' : self.total_comments } )


    def post(self , request , id ) :
        form = self.form_comment(request.POST )
        if form.is_valid() :
            new_comment = form.save()
            messages.success(request , 'با موفقیت نظر شما ثبت شد . بعد از  بررسی منتشر میشود' , 'success' )
            return redirect('blog:detail_blog' , id  )
        return render(request , self.template_name , {'data':self.data , 'another_posts' : self.another_posts  , 'form' : self.form_comment , 'total_comment' : self.total_comments } )



