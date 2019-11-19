from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import authentication, permissions,generics
from django.contrib.auth.models import User
from mainapp.serializers import *
from mainapp.models import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from .permissions import IsOwnerOrReadOnly

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class WalletListView(generics.ListCreateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

class WalletDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

class LendingBookList(APIView):

    def get(self, request, format=None):
        lendings = LendingBook.objects.filter(user=1) ##change this
        serializer = LendingBookSerializer(lendings,many=True)
        return Response(serializer.data)

    def post(self,request, format=None):
        serializer = LendingBookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LendingBookDetail(APIView):

    def get_object(self, pk):
        try:
            return LendingBook.objects.get(pk=pk)
        except LendingBook.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        lending = self.get_object(pk)
        serializer = LendingBookSerializer(lending)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        lending = self.get_object(pk)
        serializer = LendingBookSerializer(lending, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        lending = self.get_object(pk)
        lending.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ContactBookList(generics.ListCreateAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    def get(self, request, format=None):
        contacts = ContactBook.objects.filter(user=self.request.user)  ##change to request.user and added authentication
        serializer = ContactBookSerializer(contacts, many=True)
        return Response(serializer.data)

    def post(self,request, format=None):
        serializer = ContactBookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ContactBookDetail(APIView):

        permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]

        def get_object(self, pk):
            try:
                return ContactBook.objects.get(pk=pk)
            except ContactBook.DoesNotExist:
                raise Http404

        def get(self, request, pk, format=None):
            contact = self.get_object(pk)
            serializer = ContactBookSerializer(contact)
            return Response(serializer.data)

        def put(self, request, pk, format=None):
            contact = self.get_object(pk)
            serializer = ContactBookSerializer(contact, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, pk, format=None):
            contact = self.get_object(pk)
            contact.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)             # <-- And here

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
