from rest_framework import serializers
from .models import UserProfile
from projects.serializers import StackSerializer, DomainSerializer
from projects.models import Stack, Domain

class UserProfileSerializer(serializers.ModelSerializer):
    stacks = StackSerializer(many=True, required=False)
    domains = DomainSerializer(many=True, required=False)

    class Meta:
        model = UserProfile
        fields = '__all__'

    def create(self, validated_data):
        stacks_data = validated_data.pop('stacks')
        domains_data = validated_data.pop('domains')
        user_profile = UserProfile.objects.create(**validated_data)

        for stack_data in stacks_data:
            stack, created = Stack.objects.get_or_create(**stack_data)
            user_profile.stack.add(stack)

        for domain_data in domains_data:
            domain, created = Domain.objects.get_or_create(**domain_data)
            user_profile.domains.add(domain)

        return user_profile

    def update(self, instance, validated_data):
        stacks_data = validated_data.pop('stacks', [])
        domains_data = validated_data.pop('domains', [])

        instance.stacks.clear()
        for stack_data in stacks_data:
            stack, created = Stack.objects.get_or_create(**stack_data)
            instance.stacks.add(stack)

        instance.domains.clear()
        for domain_data in domains_data:
            domain, created = Domain.objects.get_or_create(**domain_data)
            instance.domains.add(domain)

        instance.save()
        return instance
