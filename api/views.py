from rest_framework import status
from rest_framework.response import Response
from .models import Aluno
from rest_framework import generics
from .serializer import AlunoSerializer


class AlunosSet(generics.CreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.get("items") if 'items' in request.data else request.data
        many = isinstance(data, list)
        lista = []
        for x in data:
            x['media'] = round((x['nota'] + x['nota2'])/2,2)
            if x['media'] >= 6:
                lista.append(x)

        serializer = self.get_serializer(data=lista, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)