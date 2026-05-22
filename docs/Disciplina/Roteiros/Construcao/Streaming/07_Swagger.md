# 06 - Swagger

## Introdução ao Swagger

Para adicionar documentação OpenAPI/Swagger ao seu projeto Django com Django REST Framework, você pode usar a biblioteca **drf-spectacular**. Esta biblioteca gera o schema da API e permite visualizar a documentação com Swagger UI e ReDoc.

### Passos para Configurar o Swagger com `drf-spectacular`

1. **Instalar o `drf-spectacular`**

   Execute o seguinte comando para instalar a biblioteca `drf-spectacular`:

   ```bash
   pip install drf-spectacular
   ```

2. **Configurar o `drf-spectacular` no Projeto**

   No arquivo `settings.py`, adicione o app e configure o DRF para usar o schema do `drf-spectacular`:

   ```python
   INSTALLED_APPS = [
      # ...
      'drf_spectacular',
   ]

   REST_FRAMEWORK = {
      'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
   }

   SPECTACULAR_SETTINGS = {
      'TITLE': 'API de Conteúdos',
      'DESCRIPTION': 'Documentação da API para o app de streaming de áudio e vídeo',
      'VERSION': '1.0.0',
   }
   ```

3. **Configurar as URLs da documentação**

   Abra o arquivo `urls.py` do seu projeto Django (geralmente o `urls.py` no diretório principal do projeto) e adicione as seguintes configurações para incluir a documentação Swagger.

   ```python
   #streaming_platform/urls.py
   from django.contrib import admin
   from django.urls import path, include
   from drf_spectacular.views import (
      SpectacularAPIView,
      SpectacularSwaggerView,
      SpectacularRedocView,
   )

   urlpatterns = [
       # Suas outras URLs
       path('admin/', admin.site.urls),
       path('api/', include('app.urls')),  # Inclua as URLs do seu app

      # Schema OpenAPI
      path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

      # UIs de documentação
      path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
      path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
   ]
   ```

4. **Acessar a Documentação Swagger e ReDoc**

   Com a configuração acima, você terá acesso a dois tipos de documentação:

   * **Swagger UI**: Interface de documentação interativa. Acesse em:

     ```plaintext
    http://localhost:8000/api/docs/
     ```

   * **ReDoc**: Alternativa ao Swagger com uma interface de documentação mais moderna. Acesse em:

     ```plaintext
    http://localhost:8000/api/redoc/
     ```

5. **Testar a Documentação**

   Ao acessar `http://localhost:8000/api/docs/`, você verá a documentação de sua API com base nas views definidas e nos parâmetros dos serializadores. A partir do Swagger UI, você também pode testar diretamente os endpoints da sua API, enviando requisições com diferentes parâmetros.

### Configuração Opcional

Para personalizar ainda mais a documentação, ajuste o bloco `SPECTACULAR_SETTINGS` no `settings.py` com informações adicionais como versão, servidores, tags e metadados da API.

---

Esses passos devem ser suficientes para configurar e visualizar a documentação da API com `drf-spectacular` em seu projeto Django, facilitando o uso e a manutenção da sua API.
