from django.db import models
from django.urls import reverse


# category model for classifying your products
class Category(models.Model):
    name = models.CharField(max_length=30, blank=False, unique=True, verbose_name="نام دسته")
    name_fa = models.CharField(max_length=30, blank=False, unique=True, verbose_name="فارسی نام دسته")
    slug = models.SlugField(max_length=30, unique=True, verbose_name="اسلاگ")
    description = models.TextField(max_length=256, blank=True, verbose_name="توضیحات")
    icon = models.ImageField(upload_to='photos/categories/', blank=True, verbose_name="آیکون") # optional field
    branch_of = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, verbose_name='زیرشاخه دسته بندی')

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def url(self):
        return reverse('filtered_by_category', args=[self.slug])  # or-> '/store/' + self.slug + '/'

    def __str__(self) -> str:
        # define a language field in whole app, then decide to return .name or .name_fa
        # return self.name
        return self.name_fa

