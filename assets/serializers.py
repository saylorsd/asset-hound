from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from assets.models import (Asset, Location, AssetType, Organization, AccessibilityFeature, ProvidedService,
                           TargetPopulation, DataSource)


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(
            value,
            context=self.context)
        return serializer.data


class AssetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetType
        fields = ['name', ]


class LocationSerializer(GeoFeatureModelSerializer):
    parent_location = RecursiveField()

    class Meta:
        model = Location
        geo_field = 'geom'
        fields = ['name', 'available_transportation', 'parent_location']


class OrganizationSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Organization
        fields = ['name', 'location', 'email', 'phone']


class AccessibilityFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessibilityFeature
        fields = ['name']


class ProvidedServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProvidedService
        fields = ['name']


class TargetPopulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TargetPopulation
        fields = ['name']


class DataSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSource
        fields = ['name', 'url']


class AssetSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer()
    location = LocationSerializer()
    accessibility_features = AccessibilityFeatureSerializer(many=True)
    services = ProvidedServiceSerializer(many=True)
    hard_to_count_population = TargetPopulationSerializer(many=True)
    data_source = DataSourceSerializer()
    asset_types = AssetTypeSerializer(many=True)

    class Meta:
        model = Asset
        fields = [
            "name",
            'asset_types',
            "organization",
            "localizability",
            "location",
            "url",
            "email",
            "phone",
            "hours_of_operation",
            "holiday_hours_of_operation",
            "child_friendly",
            "capacity",
            "accessibility_features",
            "internet_access",
            "wifi_network",
            "computers_available",
            "services",
            "open_to_public",
            "hard_to_count_population",
            "sensitive",
            "date_entered",
            "last_updated",
            "data_source",
        ]

