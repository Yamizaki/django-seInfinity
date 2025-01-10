from django.db import models

CHOICES = [
        ('recurso', 'Recurso'),
        ('duplicacion', 'Duplicación'),
    ]

class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    section = models.CharField(
        max_length=20,  # Tamaño máximo del campo
        choices=CHOICES,  # Opciones definidas
        default='recurso',  # Valor predeterminado
    )

    def __str__(self):
        return self.title
    
class Pdf(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pdf_file = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    section = models.CharField(
        max_length=20,  # Tamaño máximo del campo
        choices=CHOICES,  # Opciones definidas
        default='recurso',  # Valor predeterminado
    )

    def __str__(self):
        return self.title

class Audio(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    audio_file = models.FileField(upload_to='audios/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    section = models.CharField(
        max_length=20,  # Tamaño máximo del campo
        choices=CHOICES,  # Opciones definidas
        default='recurso',  # Valor predeterminado
    )

    def __str__(self):
        return self.title

class Resource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    resource_file = models.FileField(upload_to='resources/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    section = models.CharField(
        max_length=20,  # Tamaño máximo del campo
        choices=CHOICES,  # Opciones definidas
        default='recurso',  # Valor predeterminado
    )

    def __str__(self):
        return self.title

class History(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    history_file = models.FileField(upload_to='histories/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    section = models.CharField(
        max_length=20,  # Tamaño máximo del campo
        choices=CHOICES,  # Opciones definidas
        default='recurso',  # Valor predeterminado
    )

    def __str__(self):
        return self.title
    
class Ppt(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    ppt_file = models.FileField(upload_to='ppts/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    section = models.CharField(
        max_length=20,  # Tamaño máximo del campo
        choices=CHOICES,  # Opciones definidas
        default='recurso',  # Valor predeterminado
    )

    def __str__(self):
        return self.title