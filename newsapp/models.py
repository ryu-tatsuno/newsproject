from django.db import models

# Create your models here.
class NewsPost(models.Model):
    CATEGORY = (('seizi', '政治'),
                ('sports', 'スポーツ'),
                ('tenki', '天気'),
                ('nitizyo','日常'),
                )

    title = models.CharField(
        verbose_name='タイトル',
        max_length=200
    )

    content = models.TextField(
        verbose_name='本文'
    )

    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True
    )

    category = models.CharField(
        verbose_name='カテゴリ',
        max_length=50,
        choices=CATEGORY
    )

    def __str__(self):
        return self.title