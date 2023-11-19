from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authentification.application.serializers.post_serializer import PostSerializer
from authentification.application.use_cases.post_use_cases import PostUseCases
from authentification.infrastructure.viewsets.custom_pagination_viewset import CustomPaginationViewSet


class PostViewSet(viewsets.ModelViewSet):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.post_use_cases = PostUseCases()

    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPaginationViewSet
    serializer_class = PostSerializer

    def list(self, *args, **kwargs):
        posts = self.post_use_cases.get_posts()
        page = self.paginate_queryset(posts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

    def create(self, request, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            self.post_use_cases.create_post(serializer.validated_data)
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': serializer.errors})

    def destroy(self, request, *args, **kwargs):
        self.post_use_cases.delete_post(kwargs['pk'])
        return Response(status=status.HTTP_200_OK, data={'message': 'Post deleted successfully'})
