from django.db import models


class BaseModel(models.Model):
    created_ad = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")
    updated_ad = models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqt")

    class Meta:
        abstract = True


class Author(BaseModel):
    title = models.CharField(max_length=150, verbose_name="Muallif ismi")
    image = models.ImageField(upload_to='authors/', verbose_name="Muallif rasmi")
    description = models.TextField(verbose_name="Muallif haqida qisqacha")
    content = models.TextField()

    facebook_url = models.CharField(max_length=300, verbose_name="Facebook manzili")
    twitter_url = models.CharField(max_length=300, verbose_name="Twitter manzili")
    instagram_url = models.CharField(max_length=300, verbose_name="Instagram manzili")
    pinterest_url = models.CharField(max_length=300, verbose_name="Pinterest manzili")

    is_top = models.BooleanField(default=False, verbose_name="Top Muallifligi")

    class Meta:
        verbose_name = "Muallif"
        verbose_name_plural = "Mualliflar"

    def __str__(self):
        return self.title


class Category(BaseModel):
    title = models.CharField(max_length=200, verbose_name="Maqolalar kategoriyasi")
    image = models.ImageField(upload_to='category/', verbose_name="Kategoriya rasmi")
    count_post = models.IntegerField(default=0, verbose_name="Boglangan maqolalar soni")

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

    def __str__(self):
        return self.title


class Tags(BaseModel):
    title = models.CharField(max_length=250, verbose_name="Kichik teglar")

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Taglar"

    def __str__(self):
        return self.title


class Post(BaseModel):
    title = models.CharField(max_length=250)
    image = models.ImageField('post/')
    short_content = models.CharField(max_length=300)
    content = models.TextField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tags, related_name='posts')

    published_date = models.DateTimeField(auto_now_add=True)

    read_min = models.CharField(max_length=200)

    is_featured = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Maqola"
        verbose_name_plural = "Maqolalar"

    def __str__(self):
        return self.title


class ContactUsRequest(BaseModel):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()

    class Meta:
        verbose_name = "Foydalanuvchi kontakti"
        verbose_name_plural = "Foydalanuvchi kontaktilari"


class ContactUs(BaseModel):
    content = models.TextField()

    facebook_url = models.CharField(max_length=300, verbose_name="Facebook manzili")
    twitter_url = models.CharField(max_length=300, verbose_name="Twitter manzili")
    instagram_url = models.CharField(max_length=300, verbose_name="Instagram manzili")
    pinterest_url = models.CharField(max_length=300, verbose_name="Pinterest manzili")


class FAQ(BaseModel):
    question = models.CharField(max_length=300)
    answer = models.TextField()

    class Meta:
        verbose_name_plural = "FAQlar"

    def __str__(self):
        return self.question
