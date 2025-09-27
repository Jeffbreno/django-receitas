from django.core.management.base import BaseCommand
from recipes.models import Recipe, Category
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Carrega dados de exemplo para testar o sistema.'

    def handle(self, *args, **options):
        # Exemplo de dados
        # Cria categoria padrão se não existir
        category, _ = Category.objects.get_or_create(name='Categoria Teste')

        # Cria usuário admin de teste se não existir
        user, created = User.objects.get_or_create(username='admin')
        if created:
            user.set_password('admin123')
            user.is_superuser = True
            user.is_staff = True
            user.save()

        sample_recipes = [
            {
                'title': 'Bolo de Cenoura',
                'description': 'Um delicioso bolo de cenoura com cobertura de chocolate.',
                'slug': 'bolo-de-cenoura',
                'preparation_time': 60,
                'preparation_time_unit': 'Minutos',
                'servings': 8,
                'servings_unit': 'Fatias',
                'preparation_steps': 'Misture tudo e asse por 40 minutos.',
                'cover': 'recipes/covers/bolo-de-cenoura.jpg',
            },
            {
                'title': 'Lasanha de Frango',
                'description': 'Lasanha cremosa de frango com queijo.',
                'slug': 'lasanha-de-frango',
                'preparation_time': 90,
                'preparation_time_unit': 'Minutos',
                'servings': 6,
                'servings_unit': 'Porções',
                'preparation_steps': 'Monte as camadas e leve ao forno.',
                'category_id': 1,
                'cover': 'recipes/covers/lasanha-de-frango.jpg',
            },
            {
                'title': 'Feijoada Completa',
                'description': 'Tradicional feijoada brasileira com carnes e acompanhamentos.',
                'slug': 'feijoada-completa',
                'preparation_time': 180,
                'preparation_time_unit': 'Minutos',
                'servings': 10,
                'servings_unit': 'Pessoas',
                'preparation_steps': 'Cozinhe as carnes e o feijão juntos.',
                'category_id': 1,
                'cover': 'recipes/covers/feijoada-completa.jpg',
            },
            {
                'title': 'Moqueca Baiana',
                'description': 'Moqueca de peixe com leite de coco e azeite de dendê.',
                'slug': 'moqueca-baiana',
                'preparation_time': 60,
                'preparation_time_unit': 'Minutos',
                'servings': 4,
                'servings_unit': 'Porções',
                'preparation_steps': 'Cozinhe o peixe com os temperos e finalize com leite de coco.',
                'category_id': 1,
                'cover': 'recipes/covers/moqueca-baiana.jpg',
            },
            {
                'title': 'Pudim de Leite Condensado',
                'description': 'Sobremesa clássica, cremosa e caramelizada.',
                'slug': 'pudim-de-leite-condensado',
                'preparation_time': 90,
                'preparation_time_unit': 'Minutos',
                'servings': 12,
                'servings_unit': 'Fatias',
                'preparation_steps': 'Bata os ingredientes e asse em banho-maria.',
                'category_id': 1,
                'cover': 'recipes/covers/pudim-de-leite-condensado.jpg',
            },
            {
                'title': 'Strogonoff de Carne',
                'description': 'Strogonoff cremoso de carne com champignon.',
                'slug': 'strogonoff-de-carne',
                'preparation_time': 40,
                'preparation_time_unit': 'Minutos',
                'servings': 5,
                'servings_unit': 'Porções',
                'preparation_steps': 'Refogue a carne, adicione creme de leite e champignon.',
                'category_id': 1,
                'cover': 'recipes/covers/strogonoff-de-carne.jpg',
            },
            {
                'title': 'Quiche de Alho-Poró',
                'description': 'Quiche leve e saborosa de alho-poró.',
                'slug': 'quiche-de-alho-poro',
                'preparation_time': 50,
                'preparation_time_unit': 'Minutos',
                'servings': 8,
                'servings_unit': 'Fatias',
                'preparation_steps': 'Prepare a massa e recheie com alho-poró refogado.',
                'category_id': 1,
                'cover': 'recipes/covers/quiche-de-alho-poro.jpg',
            },
            {
                'title': 'Torta de Frango',
                'description': 'Torta salgada de frango desfiado com massa leve.',
                'slug': 'torta-de-frango',
                'preparation_time': 70,
                'preparation_time_unit': 'Minutos',
                'servings': 10,
                'servings_unit': 'Fatias',
                'preparation_steps': 'Misture o recheio e asse com a massa.',
                'category_id': 1,
                'cover': 'recipes/covers/torta-de-frango.jpg',
            },
            {
                'title': 'Brigadeiro Gourmet',
                'description': 'Docinho brasileiro feito com chocolate de qualidade.',
                'slug': 'brigadeiro-gourmet',
                'preparation_time': 30,
                'preparation_time_unit': 'Minutos',
                'servings': 20,
                'servings_unit': 'Unidades',
                'preparation_steps': 'Cozinhe até desgrudar da panela e enrole.',
                'category_id': 1,
                'cover': 'recipes/covers/brigadeiro-gourmet.jpg',
            },
            {
                'title': 'Salada Caesar',
                'description': 'Salada clássica com molho especial e croutons.',
                'slug': 'salada-caesar',
                'preparation_time': 20,
                'preparation_time_unit': 'Minutos',
                'servings': 4,
                'servings_unit': 'Porções',
                'preparation_steps': 'Misture os ingredientes e sirva gelada.',
                'category_id': 1,
                'cover': 'recipes/covers/salada-caesar.jpg',
            },
            {
                'title': 'Escondidinho de Carne Seca',
                'description': 'Purê de mandioca com recheio de carne seca desfiada.',
                'slug': 'escondidinho-de-carne-seca',
                'preparation_time': 80,
                'preparation_time_unit': 'Minutos',
                'servings': 8,
                'servings_unit': 'Porções',
                'preparation_steps': 'Monte camadas de purê e carne seca e leve ao forno.',
                'category_id': 1,
                'cover': 'recipes/covers/escondidinho-de-carne-seca.jpg',
            },
        ]

        for data in sample_recipes:
            recipe, created = Recipe.objects.get_or_create(
                slug=data['slug'],
                defaults={
                    **data,
                    'category': category,
                    'author': user,
                    'is_published': True,
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Receita '{recipe.title}' criada."))
            else:
                self.stdout.write(self.style.WARNING(f"Receita '{recipe.title}' já existe."))

        self.stdout.write(self.style.SUCCESS('Dados de exemplo carregados com sucesso!'))
