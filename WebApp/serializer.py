from rest_framework import serializers

from .models import Paper

class PaperSerializer(serializers.ModelSerializer):
	class Meta:
		model = Paper
		fields = [
			'id',
			'authors',
			'year',
			'title',
			'abstract',
			'journal',
			'issue',
			'volume',
			'pages',
			'DOI'
		]
