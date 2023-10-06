from django.db import models

# Create your models here.

class Paper(models.Model):
	def __str__(self):
		return str(self.year) + '_' + self.journal

	authors = models.CharField(max_length=500)
	year = models.IntegerField()
	title = models.TextField()
	abstract = models.TextField()
	journal = models.TextField()
	issue = models.IntegerField(null=True, blank=True)
	volume = models.IntegerField(null=True, blank=True)
	pages = models.CharField(max_length=500)
	DOI = models.CharField(max_length=500, null=True, blank=True)

	class Meta:
		ordering = ['-year']
	
	
