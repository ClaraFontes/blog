
# def CustomFunctionMiddleware(get_response):
#     # Inicialização
#     print('hello!')

#     def middleware(request):
#         # código a ser executado ANTES da view ser chamada - request
#         print('executado antes da view')
#         response = get_response(request) # passa a request para o próximo middleware (ou view)
#         print('executado depois da view')
#         # código a ser executado DEPOIS da view ser chamada - response
#         return response
    
#     return middleware

class CustomClassMiddleware:
    def __init__(self,get_response): # construtor
        self.get_response = get_response

    # Inicialização
    print('hello!')

    def __call__(self,request):
        # código a ser executado ANTES da view ser chamada - request
        print('executado antes da view')
        print(request.path)

        if(request.path == '/users/get/'):
            print("view get foi chamada")

        response = self.get_response(request) # passa a request para o próximo middleware (ou view)
        print('executado depois da view')
        # código a ser executado DEPOIS da view ser chamada - response
        return response
