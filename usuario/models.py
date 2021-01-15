from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique = True)
    senha = models.CharField(max_length = 254, db_column = 'senha')

    def __str__(self):
        return self.nome

# class Usuario(BaseUserManager):
#     def criar_usuario(self, email, username, password=None):
#         if not email:
#             raise ValueError('Usuário não tem um endereço de email')
#         if not username:
#             raise ValueError('Usuário não tem um nome')

#         user = self.model(
#             email = self.normalize_email(email)
#             username = username,
#         )
#         user.set_password(password)
#         user.save()
#         return user

