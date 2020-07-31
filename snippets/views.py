from django.contrib.auth.models import User
from rest_framework import permissions, renderers, viewsets, generics, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Snippet
from .permissions import IsOwnerOrReadOnly
from .serializers import SnippetSerializer, UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ExplorationViewSet(generics.RetrieveAPIView):
    
    def get(self, request, *args, **kwargs):
        print(dir(request))
        print('*** Request ***')
        print('Method: {}'.format(request.method))
        print('Content Type: {}'.format(request.content_type))
        print('Stream: {}'.format(request.stream))
        print('Data: {}'.format(request.data))
        print('Query Params: {}'.format(request.query_params))
        print('User: {}'.format(request.user))
        print('Auth: {}'.format(request.auth))
        print('Authenticators: {}'.format(request.authenticators))
        # print('Meta: {}'.format(request.META))
        print('Session: {}'.format(request.session))

        return Response(status=status.HTTP_200_OK)
