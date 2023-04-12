from django.db import models

class Post(models.Model):
    title = models.CharField('Заголовок', max_length= 150)
    text = models.TextField('Текст')
    author = models.CharField('Автор', max_length=70)
    date = models.DateField('дата публикации')
    image = models.ImageField('', upload_to = 'image/%Y')

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

class Comments(models.Model):
    email = models.EmailField()
    name = models.CharField('Имя: ', max_length= 100)
    comm_text = models.TextField('Текст комментария:', max_length= 1500)
    post = models.ForeignKey(Post, verbose_name='публикация', on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'