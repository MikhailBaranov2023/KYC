from rest_framework import generics
from rest_framework.parsers import MultiPartParser

from document.models import Document
from document.serializers import DocumentSerializer, DocumentVerifiedSerializer
from document.permissions import IsStaffPermission
from rest_framework.permissions import IsAuthenticated
from document.services.services import send_mail_to_admin, send_mail_verification, send_mail_not_verified


class DocumentUpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView,
                                   generics.RetrieveAPIView):
    """
    class for Update, Delete, Retrieve document
    """
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    permission_classes = (IsStaffPermission,)


class DocumentCreateAPIView(generics.CreateAPIView):
    """
    Add document for verification
    """
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser,)

    def perform_create(self, serializer):
        new_document = serializer.save()
        new_document.user = self.request.user
        new_document.save()
        send_mail_to_admin(new_document.document, new_document.id, new_document.user)


class DocumentVerifiedAPIView(generics.UpdateAPIView):
    serializer_class = DocumentVerifiedSerializer
    queryset = Document.objects.all()
    permission_classes = (IsAuthenticated, IsStaffPermission,)

    def perform_update(self, serializer):
        document = serializer.save()
        if document.verification_status is True:
            send_mail_verification(document.user)
        elif document.verification_status is False:
            send_mail_not_verified(document.user)
