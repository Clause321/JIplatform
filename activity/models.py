from django.db import models
from DjangoUeditor.models import UEditorField

# from south.modelsinspector import add_ignored_fields,add_introspection_rules
# add_introspection_rules([], [r"^DjangoUeditor\.models\.UEditorField"])

class Activity(models.Model):
    title = models.CharField(max_length=30)
    content = UEditorField(u'content', toolbars="full",
                         imagePath="image/", filePath="file/", width=800,
                         upload_settings={"imageMaxSize":1204000},
                         settings={},command=None,
                         blank=True)
    summary = models.CharField(max_length=50)
    pic = models.ImageField(upload_to = 'news_img/')
    write_date = models.DateTimeField()
    due_date = models.DateTimeField()
    private = models.BooleanField(default = False)
    type = models.CharField(max_length = 20)
    group = models.CharField(max_length = 20)

    def __unicode__(self):
        return self.title

class act_allow_group(models.Model):
    act_id = models.IntegerField()
    group_id = models.IntegerField()

    def __unicode__(self):
        return self.act_id



