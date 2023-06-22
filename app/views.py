# myapp/views.py

from rest_framework import generics
from .models import Entrepreneur, Pitch, Shark, Pitch_Request, Contact
from .serializers import EntrepreneurSerializer, PitchSerializer, SharkSerializer, PitchRequestSerializer, ContactSerializer

class EntrepreneurListCreateView(generics.ListCreateAPIView):
    queryset = Entrepreneur.objects.all()
    serializer_class = EntrepreneurSerializer

class EntrepreneurRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entrepreneur.objects.all()
    serializer_class = EntrepreneurSerializer

class PitchListCreateView(generics.ListCreateAPIView):
    queryset = Pitch.objects.all()
    serializer_class = PitchSerializer

class PitchRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pitch.objects.all()
    serializer_class = PitchSerializer

class SharkListCreateView(generics.ListCreateAPIView):
    queryset = Shark.objects.all()
    serializer_class = SharkSerializer

class SharkRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shark.objects.all()
    serializer_class = SharkSerializer

class PitchRequestListCreateView(generics.ListCreateAPIView):
    queryset = Pitch_Request.objects.all()
    serializer_class = PitchRequestSerializer

class PitchRequestRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pitch_Request.objects.all()
    serializer_class = PitchRequestSerializer


class ContactListCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer




# runs only to create the Sharks in the Database
from app.models import Shark
import os
import json

def add_sharks_from_json():
    path ="/home/zec/personal/Tasks/by-tushar/shark-tank-india/shark_tank_backend/sharks_s1.json"
    with open(path, 'r') as file:
        json_data = json.load(file)

    for data in json_data:
        shark = Shark()
        shark.name = data['shark']
        shark.bio = data['bio']
        shark.profession = data['profession']
        shark.award = data['awards']
        shark.twitter = data['twitter']
        shark.career = data['career']
        shark.save()
        print("Shark Added", data['shark'])

# add_sharks_from_json()


import json
from django.core.exceptions import ObjectDoesNotExist

# Path to the JSON file
json_file_path = "/home/zec/personal/Tasks/by-tushar/shark-tank-india/shark_tank_backend/combined_data.json"

def add_data_to_database():
    counter = 1
    with open(json_file_path, 'r') as file:
        json_data = json.load(file)
        
        for data in json_data:
            try:
                pitch = Pitch.objects.get(id=data['id'])
                # If the pitch already exists, update the fields
                pitch.season_number = data['episode_number']
                pitch.episode_number = data['episode_number']
                pitch.pitch_number = data['pitch_number']
                pitch.brand_name = data['brand_name']
                pitch.product = data['product/idea']
                pitch.present_sharks = data['sharks_present']
                pitch.pitcher_ask_amount = data['pitcher_ask_amount']
                pitch.pitcher_ask_equity = data['pitcher_ask_equity']
                pitch.pitcher_ask_valuation = data['pitcher_ask_valuation']
                pitch.sector = data['sector']
                pitch.deal_or_not = bool(data['deal_or_not'])
                pitch.deal_valuation = data['deal_valuation']
                pitch.entrepreneurs_founders = data['entrepreneurs/founders']
                pitch.deal = bool(data['deal_or_not'])
                pitch.deal_amount = data['deal_amount']
                pitch.deal_equity = data['deal_equity']
                pitch.total_sharks_invested = data['total_sharks_invested']
                pitch.sharks_invested = data['sharks_deal']
                pitch.equity_per_shark = data['equity_per_shark']
                pitch.final_deal_debt = data['final_deal_debt']
                pitch.final_deal_debt_interest = data['final_deal_dept_interest']
                pitch.social_media_links = data['company_social_media']
                pitch.save()
                
            except ObjectDoesNotExist:
                # If the pitch doesn't exist, create a new one
                pitch = Pitch(
                    id=data['id'],
                    season_number=data['episode_number'],
                    episode_number=data['episode_number'],
                    pitch_number=data['pitch_number'],
                    brand_name=data['brand_name'],
                    product=data['product/idea'],
                    present_sharks=data['sharks_present'],
                    pitcher_ask_amount=data['pitcher_ask_amount'],
                    pitcher_ask_equity=data['pitcher_ask_equity'],
                    pitcher_ask_valuation=data['pitcher_ask_valuation'],
                    sector=data['sector'],
                    deal_or_not=bool(data['deal_or_not']),
                    deal_valuation=data['deal_valuation'],
                    entrepreneurs_founders=data['entrepreneurs/founders'],
                    deal=bool(data['deal_or_not']),
                    deal_amount=data['deal_amount'],
                    total_sharks_invested=data['total_sharks_invested'],
                    sharks_invested=data['sharks_deal'],
                    equity_per_shark=data['equity_per_shark'],
                    final_deal_debt=data['final_deal_debt'],
                    final_deal_debt_interest=data['final_deal_dept_interest'],
                    social_media_links=data['company_social_media']
                )
                pitch.save()
                print("Data Saved - ", counter )
                counter +=1

# Call the function to add the data to the database
# add_data_to_database()
