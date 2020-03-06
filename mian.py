import types
import importlib

def is_function(tup):
    name, item = tup
    return isinstance(item, types.FunctionType)

def import_modul_functions(modules, level='testcase'):
    for module_name in modules:
        imported = importlib.import_module(module_name)
        imported_functions_dict = dict(filter(is_function, vars(imported).items())


# def open_yeml():
#     with open('test.yml', 'r', encoding='utf-8') as ym:
#         yml_data = ym.read()

#         data  = yaml.full_load(yml_data)
#     print(data[0]['test']['function_binds']['gen_random_string'])
#     gen_random_string = data[0]['test']['function_binds']['gen_random_string']
#     func = eval(gen_random_string)
#     print(func(5))
# open_yeml()