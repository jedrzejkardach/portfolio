from django.db import models


class Blog(models.Model):

    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(upload_to="images/")

    def summary(self):
        str_body = str(self.body)
        if len(str_body.split()) < 10:
            return str_body
        else:
            return " ".join(str_body.split()[:10]) + "..."

    def pub_date_pretty(self):
        print(self.pub_date)
        return self.pub_date

    def __str__(self):
        return self.title
