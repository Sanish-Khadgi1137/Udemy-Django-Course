from django.shortcuts import render
from datetime import date


# Create your views here.

all_posts = [
{
    "slug": "codin",
    "image": "coding.jpg",
    "author": "Sanis",
    "date": date(2025, 1, 1),
    "title": "Coding cpmpetinio",
    "excerpt": """nothing like view you get when hiking in the mountain! And
            I was not even prepared for what happened whilst I was enjoing the
            view!""",
    "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit. Quo at fuga quia
          iusto similique doloribus esse dolorem quos harum perferendis ex
          architecto, ipsum ut omnis ab rerum quam ducimus nam."""

},
{
    "slug": "wood-hike",
    "image": "woods.jpg",
    "author": "Sanis",
    "date": date(2024, 1, 1),
    "title": "wood Hiking",
    "excerpt": """view you get when hiking in the mountain! And
            I was not even prepared for what happened whilst I was enjoing the
            view!""",
    "content": """LLorem ipsum dolor sit amet consectetur adipisicing elit. Quo at fuga quia
          iusto similique doloribus esse dolorem quos harum perferendis ex
          architecto, ipsum ut omnis ab rerum quam ducimus nam."""

},
{
    "slug": "hike-in-the-mountain",
    "image": "mountains.jpg",
    "author": "Sanis",
    "date": date(2021, 1, 1),
    "title": "Mountain Hiking",
    "excerpt": """There's nothing like view you get when hiking in the mountain! And
            I was not even prepared for what happened whilst I was enjoing the
            view!""",
    "content": """LLLorem ipsum dolor sit amet consectetur adipisicing elit. Quo at fuga quia
          iusto similique doloribus esse dolorem quos harum perferendis ex
          architecto, ipsum ut omnis ab rerum quam ducimus nam."""

},
{
        "slug": "hike-in-the-mountains2",
        "image": "mountains.jpg",
        "author": "Maximilian",
        "date": date(2027, 1, 1),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
          LLLLLLLorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "programming-is-fun2",
        "image": "coding.jpg",
        "author": "Maximilian",
        "date": date(2019, 1, 1),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          LLLLorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods2",
        "image": "woods.jpg",
        "author": "Maximilian",
        "date": date(2026, 1, 1),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          LLorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }

]

#supporting method(seperate stand alone funtion); we pass a single post; the "post0" do not have connection  with none but starting_page
def get_date(post0):
    """to filter out all but date from post dictionary"""
    return post0["date"]
               # date is key from above dictionary/dummy data/db

def starting_page(request):
                #sorting in old dictionary
    #sorted_posts = all_posts.sort(key=get_date)
    
                #sorting according to date oldest in front and give new list
    sorted_posts = sorted(all_posts, key=get_date)

                #list slicing to get last 3 items
    latest_post = sorted_posts[-3:]

    #passing dictionary to starting-page i.e index.html
    return render(request, "blog/index.html", {
        "posts1": latest_post
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts1": all_posts #"all_posts" is above dictionary
    } )

# slug perfom also like a dynamic "name=" keyword which leads to particular link; here lead to particular post
def post_detail(request, slug):
  #next() is a built-in funtion which finds next element that matches certain condition
    identified_post = next(post for post in all_posts if post['slug'] == slug)
                              #"post['slug']" = this slug from dictionary and "== slug" this slug was passed from urls.py    
    return render(request, "blog/post-detail.html", {
        "post3" : identified_post
    })
