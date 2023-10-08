from rest_framework import serializers
from .models import Project, Stack, Domain, ProjectLink

class StackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stack
        fields = '__all__'

class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = '__all__'

class ProjectLinkSerializer(serializers.ModelSerializer):

    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all(), write_only=True, required=False)

    class Meta:
        model = ProjectLink
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    stacks = StackSerializer(many=True, required=False)
    domains = DomainSerializer(many=True, required=False)
    links = ProjectLinkSerializer(many=True, required=False)

    class Meta:
        model = Project
        fields = '__all__'

    def create(self, validated_data):
        stacks_data = validated_data.pop('stacks', [])
        domains_data = validated_data.pop('domains', [])
        links_data = validated_data.pop('links', [])
        
        project = Project.objects.create(**validated_data)

        for stack_data in stacks_data:
            stack, created = Stack.objects.get_or_create(**stack_data)
            project.stacks.add(stack)
        
        for domain_data in domains_data:
            domain, created = Domain.objects.get_or_create(**domain_data)
            project.domains.add(domain)
        
        for link_data in links_data:
            ProjectLink.objects.create(project=project, **link_data)

        return project

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.summary = validated_data.get('summary', instance.summary)
        instance.level = validated_data.get('level', instance.level)
        instance.github_uri = validated_data.get('github_uri', instance.github_uri)

        if 'stacks' in validated_data:
            instance.stacks.clear()

            stacks_data = validated_data.pop('stacks')
            for stack_data in stacks_data:
                stack, created = Stack.objects.get_or_create(**stack_data)
                instance.stacks.add(stack)

        if 'domains' in validated_data:
            instance.domains.clear()

            domains_data = validated_data.pop('domains')
            for domain_data in domains_data:
                domain, created = Domain.objects.get_or_create(**domain_data)
                instance.domains.add(domain)

        if 'links' in validated_data:
            links_data = validated_data.pop('links')

            links_to_retain = []

            for link_data in links_data:
                link_instance, created = ProjectLink.objects.update_or_create(
                    project=instance, title=link_data['title'], defaults={'url': link_data['url']}
                )
                links_to_retain.append(link_instance.id)

            instance.links.exclude(id__in=links_to_retain).delete()

        instance.save()
        return instance
