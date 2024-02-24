from django.db import models
from django.utils.safestring import mark_safe

from modules.services.utils import unique_slugify
from tinymce.models import HTMLField
from realtors.models import Realtor


class Developer(models.Model):
    slug = models.SlugField(verbose_name='URL', max_length=255, blank=False, unique=True)
    title_en = models.CharField(max_length=255, blank=False, null=False, unique=True)
    title_ru = models.CharField(max_length=255, blank=False, null=False, unique=True)
    title_ar = models.CharField(max_length=255, blank=False, null=False, unique=True)
    logo = models.CharField(max_length=1000, blank=True, null=True)

    year_of_foundation = models.CharField(max_length=4, blank=True, null=True)

    buildings_finished = models.IntegerField(blank=True, null=True)
    complexes_finished = models.IntegerField(blank=True, null=True)
    buildings_in_progress = models.IntegerField(blank=True, null=True)
    complexes_in_progress = models.IntegerField(blank=True, null=True)
    main_office = models.CharField(max_length=1000, blank=True, null=True)
    number_of_employees = models.IntegerField(blank=True, null=True)
    stock_valuation = models.IntegerField(blank=True, null=True)

    text_en = HTMLField(blank=True)
    text_ru = HTMLField(blank=True)
    text_ar = HTMLField(blank=True)

    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Developer'
        verbose_name_plural = 'Developers'
        ordering = ['-id']
        db_table = "developers"

    def save(self, *args, **kwargs):
        """
        Сохранение полей модели при их отсутствии заполнения
        """
        if not self.slug:
            self.slug = unique_slugify(self, self.title_en)

        if not self.year_of_foundation:
            self.year_of_foundation = '2001'

        if not self.buildings_finished:
            self.buildings_finished = 81

        if not self.complexes_finished:
            self.complexes_finished = 18

        if not self.buildings_in_progress:
            self.buildings_in_progress = 10

        if not self.complexes_in_progress:
            self.complexes_in_progress = 4

        if not self.main_office:
            self.main_office = 'Dubai'

        if not self.number_of_employees:
            self.number_of_employees = 500

        if not self.stock_valuation:
            self.stock_valuation = 1400

        if not self.text_en:
            self.text_en = self.title_en + ' — is a Dubai development company operating in the luxury real estate market since 2002. Its portfolio includes premium residential complexes, office buildings and 5-star hotels in the United Arab Emirates, China, the Lebanese Republic, Jordan and the UK.<p>To date, 32,000 new properties have already been built, and another 34,000 are under construction.<p>The company has received more than 100 global awards in the field of real estate, architecture, interior design, services and services.'

        if not self.text_ru:
            self.text_ru = self.title_ru + ' — дубайская девелоперская компания, работающая на рынке элитной недвижимости с 2002 года. В ее портфеле жилые комплексы премиум-класса, офисные здания и 5-звездочные отели в Арабских Эмиратах, Китае, Ливанской республике, Иордании и Великобритании.<p>На сегодняшний день 32 000 новых объектов недвижимости уже построено, еще 34 000 — на стадии строительства.<p>Компания получила более 100 мировых наград в области недвижимости, архитектуры, дизайна интерьера, услуг и сервиса.'

        if not self.text_ar:
            self.text_ar = self.title_ar + ' — هي شركة تطوير في دبي تعمل في سوق العقارات الفاخرة منذ عام 2002. وتشمل محفظتها مجمعات سكنية متميزة ومباني مكتبية وفنادق 5 نجوم في الإمارات العربية المتحدة والصين وجمهورية لبنان والأردن والمملكة المتحدة.<p>وحتى الآن، تم بناء 32 ألف عقار جديد، وهناك 34 ألف عقار آخر قيد الإنشاء.<p>حصلت الشركة على أكثر من 100 جائزة عالمية في مجال العقارات والهندسة المعمارية والتصميم الداخلي والخدمات والخدمات.'

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """
        Ссылка на страницу застройщика
        """
        return '/en/developer/' + self.slug

    def image_logo(self):
        from django.utils.html import escape
        return mark_safe('<img src="%s" width="100" height="100"/>' % escape(self.logo))

    image_logo.short_description = 'Logo image'
    image_logo.allow_tags = True

    def __str__(self):
        return self.title_en
