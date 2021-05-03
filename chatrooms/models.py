from django.db import models

class Messages1(models.Model):
    name = models.CharField('Имя', max_length=50)
    message = models.TextField("Сообщение")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сообщение1'
        verbose_name_plural = 'Сообщения1'


class Messages2(models.Model):
    name = models.CharField('Имя', max_length=50)
    message = models.TextField("Сообщение")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сообщение2'
        verbose_name_plural = 'Сообщения2'


class Messages3(models.Model):
    name = models.CharField('Имя', max_length=50)
    message = models.TextField("Сообщение")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сообщение3'
        verbose_name_plural = 'Сообщения3'


class Messages4(models.Model):
    name = models.CharField('Имя', max_length=50)
    message = models.TextField("Сообщение")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сообщение4'
        verbose_name_plural = 'Сообщения4'


class Messages5(models.Model):
    name = models.CharField('Имя', max_length=50)
    message = models.TextField("Сообщение")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сообщение5'
        verbose_name_plural = 'Сообщения5'