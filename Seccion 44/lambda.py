# funcion_lambda = lambda a, b: a + b
# las funciones lambda son funciones anonimas, no tienen nombre y especifican que reciben y que retornan

mi_funcion_lambda = lambda *args, **kwargs: len(args) + len(kwargs)
print(mi_funcion_lambda(1, 2, 3, a=4, b=5))
print(mi_funcion_lambda(kwargs={"a": "b", "c": 4}, args=(1, 2, 3, 4)))
