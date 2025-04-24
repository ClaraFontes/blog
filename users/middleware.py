
def CustomFunctionMiddleware(get_response):
    # Inicialização
    print('hello!')

    def middleware(request):
        # código a ser executado ANTES da view ser chamada - request
        print('executado antes da view')
        response = get_response(request) # passa a request para o próximo middleware (ou view)
        print('executado depois da view')
        # código a ser executado DEPOIS da view ser chamada - response
        return response
    
    return middleware