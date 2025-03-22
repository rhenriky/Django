# API CRUD em Django com Django REST Framework

Este projeto é uma API RESTful construída com Django e Django REST Framework (DRF) para operações CRUD.

## Requisitos

Certifique-se de ter instalado:

- Python 3.8+
- Django 4+
- Django REST Framework

## Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/django-crud-api.git
   cd django-crud-api
   ```
2. Crie e ative um ambiente virtual:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```
3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
4. Execute as migrações do banco de dados:
   ```sh
   python manage.py migrate
   ```

## Estrutura do Projeto

```
api/
├── manage.py
├── api/
│   ├── models.py  # Modelos de dados
│   ├── serializers.py  # Serializadores DRF
│   ├── views.py  # Views da API
│   ├── urls.py  # Rotas da API
│   ├── tests.py  # Testes automatizados
├── db.sqlite3  # Banco de dados SQLite
├── requirements.txt  # Dependências do projeto
```

## Criando a API CRUD

1. Criar um modelo no `models.py`:
   ```python
   from django.db import models

   class Item(models.Model):
       name = models.CharField(max_length=255)
       description = models.TextField()
       created_at = models.DateTimeField(auto_now_add=True)
   ```
2. Criar um serializador em `serializers.py`:
   ```python
   from rest_framework import serializers
   from .models import Item

   class ItemSerializer(serializers.ModelSerializer):
       class Meta:
           model = Item
           fields = '__all__'
   ```
3. Criar as views em `views.py`:
   ```python
   from rest_framework import viewsets
   from .models import Item
   from .serializers import ItemSerializer

   class ItemViewSet(viewsets.ModelViewSet):
       queryset = Item.objects.all()
       serializer_class = ItemSerializer
   ```
4. Configurar as rotas em `urls.py`:
   ```python
   from django.urls import path, include
   from rest_framework.routers import DefaultRouter
   from .views import ItemViewSet

   router = DefaultRouter()
   router.register(r'items', ItemViewSet)

   urlpatterns = [
       path('', include(router.urls)),
   ]
   ```

## Executando a API

1. Inicie o servidor de desenvolvimento:
   ```sh
   python manage.py runserver
   ```
2. Acesse a API no navegador ou via Postman: `http://127.0.0.1:8000/items/`

## Testando a API

Você pode testar os endpoints usando `curl` ou Postman:

### Criar um item:

```sh
curl -X POST http://127.0.0.1:8000/items/ -H "Content-Type: application/json" -d '{"name": "Exemplo", "description": "Descrição do item"}'
```

### Listar itens:

```sh
curl -X GET http://127.0.0.1:8000/items/
```

### Atualizar um item:

```sh
curl -X PUT http://127.0.0.1:8000/items/1/ -H "Content-Type: application/json" -d '{"name": "Atualizado", "description": "Nova descrição"}'
```

### Deletar um item:

```sh
curl -X DELETE http://127.0.0.1:8000/items/1/
```

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b minha-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Envie para o repositório (`git push origin minha-feature`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT.sds
