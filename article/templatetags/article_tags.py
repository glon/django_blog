from django import template
from article.models import ArticlePost

register = template.Library()

@register.simple_tag
def total_articles():
    return ArticlePost.objects.count()

@register.simple_tag
def author_total_articles(user):
    return user.article.count()

@register.inclusion_tag('article/latest_articles.html')
def latest_articles(n=5):
    newest_articles = ArticlePost.objects.order_by("-created")[:n]
    return {"latest_articles":newest_articles}


