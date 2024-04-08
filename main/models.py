from django.db import models


class Section(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Розділ'
        verbose_name_plural = 'Розділи'

    def __str__(self):
        return self.title


class Subsection(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='subsections')
    type_subsection = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    slogan = models.TextField(max_length=355, blank=True, null=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='media/portfolio_images/', null=True, blank=True)
    alt_text = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'Підрозділ'
        verbose_name_plural = 'Підрозділи'

    def __str__(self):
        return self.title


class Content(models.Model):
    TAG_CHOICES = [
        ('p', 'Paragraph'),
        ('li', 'List Item'),
    ]
    subsection = models.ForeignKey(Subsection, on_delete=models.CASCADE)
    content = models.TextField()
    tag = models.CharField(max_length=2, choices=TAG_CHOICES)

    class Meta:
        verbose_name = 'Вміст'
        verbose_name_plural = 'Вміст'

    def __str__(self):
        return f'{self.tag} - {self.content[:20]}'
