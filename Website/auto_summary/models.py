from django.db import models


# Create your models here.
class UserInfo(models.Model):
    ip = models.CharField(max_length=40, default='', verbose_name=u'ip address', null=True)
    time = models.DateTimeField(verbose_name=u'update time', auto_now=True)

    class Meta:
        verbose_name = u'User Access Information'
        verbose_name_plural = verbose_name
        db_table = 'user_ip_info'


class ShortTextDB(models.Model):
    short_text = models.TextField(default='', verbose_name=u'short text', null=False)

    user_ip = models.ForeignKey('UserInfo', on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'User Short Text Input'
        verbose_name_plural = verbose_name
        db_table = 'user_short_input'


class LongTextDB(models.Model):
    long_text = models.TextField(default='', verbose_name=u'long text', null=False)

    user_ip = models.ForeignKey('UserInfo', on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'User Long Text Input'
        verbose_name_plural = verbose_name
        db_table = 'user_long_input'


class UserFeedBack(models.Model):
    user_name = models.CharField(default='', verbose_name=u'user name', max_length=50, null=False)
    user_email = models.EmailField(verbose_name=u'user email', null=False)
    user_message = models.TextField(verbose_name=u'user message', null=False)

    class Meta:
        verbose_name = u'User Feedback Info'
        verbose_name_plural = verbose_name
        db_table = 'user_feedback_info'
