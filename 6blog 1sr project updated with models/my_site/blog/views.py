from django.shortcuts import render, get_object_or_404

from .models import Post





def starting_page(request):
    latest_post = Post.objects.all().order_by("-date")[:3]#"-date" for decending-order(latest frist); [:3] for first 3 from latest order
    return render(request, "blog/index.html", {
        "posts1": latest_post  })


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts1": all_posts
    } )


def post_detail(request, slug):

    # identified_post = Post.objects.get(slug=slug)  ##slug of db = slug passed i.e. def post-detail(request, slug)
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {
        "post3" : identified_post,
        "post_tags": identified_post.caption.all()
    })
