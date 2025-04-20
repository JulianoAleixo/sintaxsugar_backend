from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .serializers import PostSerializer


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "id"


class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "id"


class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "id"

    def delete(self, request, *args, **kwargs):
        post = self.get_object()
        if not post.is_active:
            return super().delete(request, *args, **kwargs)
        return Response({"detail": "Cannot delete an active post."}, status=status.HTTP_400_BAD_REQUEST)


class UpdatePostActiveStatusView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, id):
        try:
            post = Post.objects.get(id=id)
        except Post.DoesNotExist:
            return Response({"detail": "Post not found."}, status=status.HTTP_404_NOT_FOUND)

        if request.user != post.author and not request.user.is_staff:
            return Response({"detail": "Not authorized."}, status=status.HTTP_403_FORBIDDEN)

        is_active = request.data.get("is_active")
        if is_active is None:
            return Response({"detail": 'Missing "is_active" field.'}, status=status.HTTP_400_BAD_REQUEST)

        post.is_active = is_active
        post.save()
        status_str = "activated" if is_active == "True" else "deactivated"
        return Response({"detail": f"Post {status_str} successfully."}, status=status.HTTP_200_OK)
