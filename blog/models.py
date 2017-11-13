from django.db import models
from django.utils import timezone
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Post(models.Model):
    ENGLISH='EN'
    GERMAN='DE'
    LANGUAGES = (
        (ENGLISH, "English"),
        (GERMAN, "Deutsch")
    )
    author = models.ForeignKey('auth.User')
    language = models.CharField(choices=LANGUAGES, default="EN", max_length=20)
    title = models.CharField(max_length=200)
    text = MarkdownxField()
    #text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    @property
    def formatted_markdown(self):
        return markdownify(self.text)

    def __unicode__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


class Image(models.Model):
    image = models.ImageField(upload_to='img/%Y/%m/%d')


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


