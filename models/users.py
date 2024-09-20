from peewee import Model, AutoField, CharField, DateTimeField, IntegerField
from enum import IntEnum
from config.database import database


# Definindo um Enum para as categorias de usuários
class CategoriaUserEnum(IntEnum):
    USER = 1
    GUEST = 2
    ADMIN = 3


class UsuarioDB(Model):
    id_usuario = AutoField()
    nome_usuario = CharField()
    email_usuario = CharField()
    senha_usuario = CharField()
    usuario_foto = CharField(null=True)  # O campo pode ser NULL
    data_criacao_user = DateTimeField()

    # Usando IntegerField para armazenar a categoria do usuário como um número (1, 2, 3)
    categoria_user = IntegerField(choices=[(tag.value, tag.name) for tag in CategoriaUserEnum])

    total_time_user = DateTimeField()

    class Meta:
        database = database
        table_name = 'usuarios'