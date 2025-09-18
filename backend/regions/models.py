from django.db import models

class Regions(models.Model):
    """
    지역 정보
    [code] 지역 코드(KR)
    [level] 지역 레벨
    [ko] 한국어 이름
    [en] 영문 이름
    [ja] 일본어 이름
    [parent_id] 상위 지역 ID
    """
    class LevelChoices(models.IntegerChoices):
        COUNTRY = 0, 'Nation'
        STATE = 1, 'Province'
        CITY = 2, 'City'

    code = models.CharField(max_length=50, null=False, blank=False, help_text='지역 코드(KR)')
    level = models.SmallIntegerField(null=False, choices=LevelChoices.choices)
    ko = models.CharField(max_length=255, null=False, blank=False, help_text='한국어 이름')
    en = models.CharField(max_length=255, null=False, blank=False, help_text='영문 이름')
    ja = models.CharField(max_length=255, null=False, blank=False, help_text='일본어 이름')
    parent_id = models.PositiveBigIntegerField(null=True, blank=True, help_text='상위 지역 ID')

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Region list'

    def __str__(self):
        return self.code
