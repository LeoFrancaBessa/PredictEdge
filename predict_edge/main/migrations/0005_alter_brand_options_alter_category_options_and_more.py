# Generated by Django 5.0.2 on 2024-03-17 14:28

import colorfield.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0004_clothingimage_principal_alter_clothingimage_image"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="brand",
            options={
                "ordering": ["name"],
                "verbose_name": "Marca",
                "verbose_name_plural": "Marcas",
            },
        ),
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ["name"],
                "verbose_name": "Categoria",
                "verbose_name_plural": "Categorias",
            },
        ),
        migrations.AlterModelOptions(
            name="clothes_colors",
            options={
                "verbose_name": "Tamanho Roupa",
                "verbose_name_plural": "Tamanhos Roupa",
            },
        ),
        migrations.AlterModelOptions(
            name="clothes_sizes",
            options={
                "verbose_name": "Tamanho Roupa",
                "verbose_name_plural": "Tamanhos Roupa",
            },
        ),
        migrations.AlterModelOptions(
            name="clothing",
            options={
                "ordering": ["updated_at"],
                "verbose_name": "Roupa",
                "verbose_name_plural": "Roupas",
            },
        ),
        migrations.AlterModelOptions(
            name="clothingimage",
            options={
                "verbose_name": "Imagem Roupa",
                "verbose_name_plural": "Imagens Roupa",
            },
        ),
        migrations.AlterModelOptions(
            name="material",
            options={
                "ordering": ["name"],
                "verbose_name": "Material",
                "verbose_name_plural": "Materiais",
            },
        ),
        migrations.AlterModelOptions(
            name="subtype",
            options={
                "ordering": ["name"],
                "verbose_name": "SubTipo",
                "verbose_name_plural": "SubTipos",
            },
        ),
        migrations.AlterModelOptions(
            name="type",
            options={
                "ordering": ["name"],
                "verbose_name": "Tipo",
                "verbose_name_plural": "Tipos",
            },
        ),
        migrations.AlterField(
            model_name="brand",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="Descrição"),
        ),
        migrations.AlterField(
            model_name="brand",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Nome"),
        ),
        migrations.AlterField(
            model_name="category",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="Descrição"),
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Nome"),
        ),
        migrations.AlterField(
            model_name="clothes_colors",
            name="color",
            field=colorfield.fields.ColorField(
                choices=[
                    ("#FFFFFF", "branco"),
                    ("#000000", "preto"),
                    ("#808080", "cinza"),
                    ("#FF0000", "vermelho"),
                    ("#FFA500", "laranja"),
                    ("#FFFF00", "amarelo"),
                    ("#008000", "verde"),
                    ("#0000FF", "azul"),
                    ("#800080", "roxo"),
                    ("#FFC0CB", "rosa"),
                    ("#800000", "marrom"),
                    ("#00FFFF", "ciano"),
                    ("#A52A2A", "castanho"),
                    ("#FFD700", "dourado"),
                    ("#000080", "azul-marinho"),
                    ("#8B0000", "vermelho escuro"),
                    ("#800080", "roxo"),
                    ("#00FF00", "verde-limão"),
                    ("#FF00FF", "magenta"),
                    ("#FFFFF0", "bege"),
                    ("#40E0D0", "turquesa"),
                    ("#FF4500", "laranja escuro"),
                    ("#FF6347", "salmão"),
                    ("#FFE4B5", "mocassim"),
                    ("#BDB76B", "caqui"),
                    ("#008080", "teal"),
                    ("#FA8072", "salmon claro"),
                    ("#DC143C", "carmesim"),
                    ("#7FFFD4", "aquamarine"),
                    ("#F0E68C", "khaki claro"),
                    ("#B8860B", "ouro escuro"),
                    ("#00CED1", "azul-celeste"),
                    ("#6495ED", "azul ardósia"),
                    ("#CD5C5C", "marrom rosado"),
                    ("#556B2F", "verde oliva escuro"),
                    ("#4B0082", "índigo"),
                    ("#2F4F4F", "cinza ardósia escuro"),
                ],
                default="#FFFFFF",
                image_field=None,
                max_length=25,
                samples=None,
                verbose_name="Cor",
            ),
        ),
        migrations.AlterField(
            model_name="clothes_sizes",
            name="size",
            field=models.CharField(
                choices=[
                    ("PP", "PP"),
                    ("P", "P"),
                    ("M", "M"),
                    ("G", "G"),
                    ("GG", "GG"),
                ],
                max_length=4,
                verbose_name="Tamanho",
            ),
        ),
        migrations.AlterField(
            model_name="clothing",
            name="brand",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="main.brand",
                verbose_name="Marca",
            ),
        ),
        migrations.AlterField(
            model_name="clothing",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="main.category",
                verbose_name="Categoria",
            ),
        ),
        migrations.AlterField(
            model_name="clothing",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Criado Em"),
        ),
        migrations.AlterField(
            model_name="clothing",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="Descrição"),
        ),
        migrations.AlterField(
            model_name="clothing",
            name="gender",
            field=models.CharField(
                choices=[("M", "Masculino"), ("F", "Feminino")],
                max_length=1,
                verbose_name="Gênero",
            ),
        ),
        migrations.AlterField(
            model_name="clothing",
            name="material",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="main.material",
                verbose_name="Material",
            ),
        ),
        migrations.AlterField(
            model_name="clothing",
            name="name",
            field=models.CharField(max_length=200, verbose_name="Nome"),
        ),
        migrations.AlterField(
            model_name="clothing",
            name="price",
            field=models.DecimalField(
                decimal_places=2, max_digits=10, verbose_name="Preço"
            ),
        ),
        migrations.AlterField(
            model_name="clothing",
            name="subtype",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="main.subtype",
                verbose_name="SubTipo",
            ),
        ),
        migrations.AlterField(
            model_name="clothing",
            name="type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="main.type",
                verbose_name="Tipo",
            ),
        ),
        migrations.AlterField(
            model_name="clothing",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Atualizado Em"),
        ),
        migrations.AlterField(
            model_name="clothingimage",
            name="image",
            field=models.ImageField(upload_to="media/", verbose_name="Imagem"),
        ),
        migrations.AlterField(
            model_name="clothingimage",
            name="principal",
            field=models.BooleanField(default=False, verbose_name="Imagem Principal?"),
        ),
        migrations.AlterField(
            model_name="material",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="Descrição"),
        ),
        migrations.AlterField(
            model_name="material",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Nome"),
        ),
        migrations.AlterField(
            model_name="subtype",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="Descrição"),
        ),
        migrations.AlterField(
            model_name="subtype",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Nome"),
        ),
        migrations.AlterField(
            model_name="type",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="Descrição"),
        ),
        migrations.AlterField(
            model_name="type",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Nome"),
        ),
    ]
