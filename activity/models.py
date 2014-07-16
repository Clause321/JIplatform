from django.db import models
from DjangoUeditor.models import UEditorField

# from south.modelsinspector import add_ignored_fields,add_introspection_rules
# add_introspection_rules([], [r"^DjangoUeditor\.models\.UEditorField"])

class Activity(models.Model):
    title = models.CharField(max_length=30)
    # content = UEditorField(u'content',height=100,width=500,default='test',imagePath="images/",imageManagerPath="imglib",toolbars='full',options={"elementPathEnabled":True},filePath='files/',blank=True)
    # content = UEditorField(u'content',height=100,width=500,default='test',)
    # content = models.TextField()
    content = UEditorField(u'content', toolbars="full",
                         imagePath="image/", filePath="file/", width=800,
                         upload_settings={"imageMaxSize":1204000},
                         settings={},command=None,
                         blank=True)
    summary = models.CharField(max_length=50)
    pic = models.ImageField(upload_to = 'activity/static/news_img/')
    write_date = models.DateTimeField()
    due_date = models.DateTimeField()
    group = models.CharField(max_length = 15)
    itemID = models.CharField(max_length = 8, default = 00000000)

    def __unicode__(self):
        return self.title