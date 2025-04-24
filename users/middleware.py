from django.http import HttpResponse
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
        print('executado antes da view') # código executado ANTES da view ser chamada - request

        if(request.path == '/users/get/'):
            print("view get foi chamada")

        # response = HttpResponse("RESPONSE DA CLASSE MIDDLEWARE")
        response = self.get_response(request) # passa a request para o próximo middleware (ou view)

        print('executado depois da view') # código executado DEPOIS da view ser chamada - response
        return response
    
    # def process_view(self,request,view_func,view_args,view_kwargs):
    #     print('process view antes da chamada da view')
    #     print("NOME DA VIEW:",view_func.__name__)

    #     return None

    def process_exception(self,request,exception):
        print('process exception foi chamado!')
        print(exception)
        # return HttpResponse("RESPONSE DO PROCESS_EXCEPTION") 
        return None