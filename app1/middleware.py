def mymiddleware(get_response):
    print('in my middleware')
    def inner_middleware(request):
        print('before calling view')
        response = get_response(request)
        print('after calling view')

        return response
    return inner_middleware


class MyMiddleware:
    def __init__(self, get_response):
        print('In class middleware')
        self.get_response = get_response

    def __call__(self, request):
        print('before class')
        response = self.get_response(request)
        print('after class')
        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        # This code is executed just before the view is called
        print("in process view")
        pass

    def process_exception(self, request, exception):
        # This code is executed if an exception is raised
        print('in process exception')
        pass

    def process_template_response(self, request, response):
        # This code is executed if the response contains a render() method
        print('in process template response')
        return response

