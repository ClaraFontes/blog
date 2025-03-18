def categories(request):
    categories = [
    'Programação',
    'Comida',
    'Viagem'
    ]
    return {'categories': categories}