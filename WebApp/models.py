from django.db import models



# Organization model: This data model describes an organization that operates a monitoring station network
class Organization(models.Model):
    organization_id = models.CharField(max_length=10, primary_key=True,
                                       help_text="Organization ID, usually the Accronym")
    organization_name = models.CharField(max_length=100, help_text="Organization Name (No Accronym)")
    organization_address = models.CharField(max_length=100, help_text="Organization physical address - Optional",
                                            blank=True)
    organization_city = models.CharField(max_length=100, help_text="Organization City - Optional", blank=True)
    organization_country = models.CharField(max_length=2, help_text="Organization Country ISO Code - Optional",
                                            blank=True)


# Station model: This data model describes a monitoring station operated by one of the organizations in the system
class Station(models.Model):
    station_id = models.CharField(max_length=10, primary_key=True, help_text="Station ID, unique identifier code")
    station_name = models.CharField(max_length=100, help_text="Station Name, a human readable name")
    station_lat = models.FloatField(help_text="Station Latitude in decimal degrees")
    station_lon = models.FloatField(help_text="Station Longitude in decimal degrees")
    station_elev = models.FloatField(help_text="Station Elevation in meters above sea level - Optional", blank=True,
                                     null=True)
    station_location = models.CharField(max_length=100, help_text="Station Location - Optional", blank=True)
    station_organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    station_year_established = models.IntegerField(help_text="Year the station was established - Optional", blank=True,
                                                   null=True)

    def __str__(self):
        return self.station_id + "-" + self.station_name


# Simplified Measurement model: This data model describes the individual measurements taken at a monitoring station
# The model includes just a small sample of variables (temperature and precipitation) taken on a daily frequency, for demonstration purposes,
# but it can be easily extended to include more variables and/or more frequent measurements
class Measurement(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    measurement_date = models.DateField(help_text="Measurement Date")
    measurement_temp = models.FloatField(help_text="Temperature in degrees Celsius")
    measurement_precip = models.FloatField(help_text="Precipitation in millimeters")

    def __str__(self):
        return self.station.station_id + "-" + self.station.station_name + "-" + str(self.measurement_date)
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



class Agency(models.Model):
    name = models.CharField(max_length=100)
    logo = models.FileField(upload_to='agency_logos/')  # Use FileField instead of ImageField

    def __str__(self):
        return self.name


class ImageFolder(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True)
    
    foldername = models.ForeignKey(ImageFolder, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.title


class Project(models.Model):
    name = models.CharField(max_length=1000)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, default=1)  # Set the default agency ID
    abstract = models.TextField()
    period = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    institution = models.CharField(max_length=100)
    query = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Title_People(models.Model):
    name = models.CharField(max_length=255)
    titleorder = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class People(models.Model):
    name = models.CharField(max_length=255)
    title = models.ForeignKey(Title_People, on_delete=models.CASCADE)  # Make sure Title is imported
    image = models.ImageField(upload_to='team_members/')
    bio = models.TextField() 
    cv = models.FileField(upload_to='cv_files/')

    def __str__(self):
        return self.name




