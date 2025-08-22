from rest_framework.permissions import BasePermission


class IsRelatedPerson(BasePermission):
    """Class for determining perms for entity's related persons.
    Only related persons can change information about entities and their contact details."""

    def has_object_permission(self, request, view, obj):
        return obj.related_person == request.user
