from django.db import models
from users.models import User

# Create your models here.  
from django.db import models

class Entrepreneur(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=250, default="") #delete default
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='entrepreneurs/profile_pictures/', null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Pitch(models.Model):
    season_number = models.IntegerField(default=1)
    episode_number = models.IntegerField()
    pitch_number = models.IntegerField()
    brand_name = models.CharField(max_length=255, null=True, blank=True)
    product = models.CharField(max_length=255, null=True, blank=True)
    present_sharks = models.JSONField(null=True, blank=True)
    pitcher_ask_amount = models.FloatField(null=True, blank=True)
    pitcher_ask_equity = models.FloatField(null=True, blank=True)
    pitcher_ask_valuation = models.FloatField(null=True, blank=True)
    sector = models.CharField(max_length=255, null=True, blank=True)
    deal_or_not = models.BooleanField(null=True, blank=True)
    deal_valuation = models.FloatField(null=True, blank=True)
    entrepreneurs_founders = models.TextField(null=True, blank=True)
    deal = models.BooleanField(null=True, blank=True)
    deal_amount = models.IntegerField(default=0)
    deal_equity = models.FloatField(null=True, blank=True, default=0)
    total_sharks_invested = models.IntegerField(null=True, blank=True, default=0)
    sharks_invested = models.JSONField(null=True, blank=True, default=0)
    equity_per_shark = models.FloatField(null=True, blank=True, default=0)
    final_deal_debt = models.IntegerField(null=True, blank=True, default=0)
    final_deal_debt_interest = models.IntegerField(null=True, blank=True, default=0)
    social_media_links = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"Episode {self.episode_number} - Pitch {self.pitch_number}"



INDUSTRIES = (
    ('1','Technology'),
    ('2','Food'),
    ('3','Fashion'),
    ('4','Health'),
    ('5','Home'),
    ('6','Skincare'),
    ('7','Fitness'),
    ('8','Education'),
    ('9','Entertainment'),
    ('11','Transportation'),
    ('13','Pet Care'),
    ('14','Agriculture'),
    ('15','Sports'),
)

class Pitch_Request(models.Model):
    entrepreneur = models.ForeignKey(Entrepreneur, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    industry = models.CharField(max_length=2, choices=INDUSTRIES, default='1') # delete default
    cin = models.CharField(max_length=50, default="") # delete default
    video_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    all_time_revenue = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    last_year_revenue = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    
    def __str__(self):
        return self.title

class Shark(models.Model):
    name = models.CharField(max_length=150)
    bio = models.TextField()
    profession = models.CharField(max_length=100)
    award = models.TextField(null=True, blank=True)
    career = models.TextField(null=True, blank=True)
    twitter = models.URLField(max_length=250, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='sharks/profile_pictures/', null=True, blank=True)
    def __str__(self):
        return self.name



class Contact(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    surname = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    company_name = models.CharField(max_length=100)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"