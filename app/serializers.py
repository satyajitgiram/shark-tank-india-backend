# myapp/serializers.py

from rest_framework import serializers
from .models import Entrepreneur, Pitch, Shark, Pitch_Request, Contact

class EntrepreneurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrepreneur
        fields = '__all__'

class PitchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pitch
        fields = '__all__'

class SharkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shark
        fields = '__all__'

class PitchRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pitch_Request
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

