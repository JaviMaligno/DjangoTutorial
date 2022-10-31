from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import CommentForm

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post(request, pk):
    template = 'post.html'
    #post = Post.objects.get(id=pk)
    #https://docs.djangoproject.com/en/4.1/topics/http/shortcuts/
    post = get_object_or_404(Post, id=pk)
    comments = post.comments.filter(active=True)
    #return render(request, template, {'post': post})
    #we update the method to include comments
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})