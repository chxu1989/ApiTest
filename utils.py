
import json
import os
import io
import exceptions
import logger


def get_os_environ(variable_name):
    print(os.environ)
    try:
        return os.environ[variable_name]
    except KeyError:
        raise exceptions.EnvNotFound(variable_name)
get_os_environ('python')

def dump_json_file(json_data, json_file_abs_path):
    """
     dump json data to file
    """
    class PythonObjectEncode(json.JSONEncoder):
        def default(self,obj):
            try:
                return super().default(self,obj)
            except TypeError:
                return str(obj)

    file_folder_path = os.path.dirname(json_file_abs_path)
    if not os.path.isdir(file_folder_path):
        os.mkdir(file_folder_path)
    try:
        with io.open(json_file_abs_path, 'w',encoding='utf-8') as outfile:
            json.dump(json_data, outfile, indent=4, separators=(',',':'),
             encoding='utf8', ensure_ascii=False, cls=PythonObjectEncode)
        msg = f'dump file:{json_file_abs_path}'
        logger.color_print(msg, 'BLUE')
    except TypeError as e:
        msg = f"Failed to dump json file: {json_file_abs_path}\nReason: {e}"
        logger.color_print(msg, "RED")


def prepare_dump_json_file_abs_path(project_mapping, tag_name):
    """ prepare dump json file absolute path.
    """
    pwd_dir_path = project_mapping.get("PWD") or os.getcwd()
    test_path = project_mapping.get("test_path")

    if not test_path:
        # running passed in testcase/testsuite data structure
        dump_file_name = "tests_mapping.{}.json".format(tag_name)
        dumped_json_file_abs_path = os.path.join(pwd_dir_path, "logs", dump_file_name)
        return dumped_json_file_abs_path

    # both test_path and pwd_dir_path are absolute path
    logs_dir_path = os.path.join(pwd_dir_path, "logs")
    test_path_relative_path = test_path[len(pwd_dir_path)+1:]

    if os.path.isdir(test_path):
        file_foder_path = os.path.join(logs_dir_path, test_path_relative_path)
        dump_file_name = "all.{}.json".format(tag_name)
    else:
        file_relative_folder_path, test_file = os.path.split(test_path_relative_path)
        file_foder_path = os.path.join(logs_dir_path, file_relative_folder_path)
        test_file_name, _file_suffix = os.path.splitext(test_file)
        dump_file_name = "{}.{}.json".format(test_file_name, tag_name)

    dumped_json_file_abs_path = os.path.join(file_foder_path, dump_file_name)
    return dumped_json_file_abs_path


def diff_reponse(resp_obj,expected_resp_json):

    resp_info = parse_reponse_object(resp_obj)    
    return diff_json(resp_info,expected_resp_json)



def parse_reponse_object(resp_obj):
    try:
        resp_body = resp_obj.json()

    except ValueError:
        resp_body = resp_obj.text

    return {
        'status_code': resp_obj.status_code,
        'headers': resp_obj.headers,
        'body': resp_body
    }

def diff_json(current_json, expected_json):
    json_diff = {}
    for key,expected_value in expected_json.items():
        value = current_json.get(key,None)
        if str(value) != expected_value:
            json_diff[key] ={
              'vlaue':value,
              'expecte':expected_value
            }
    return json_diff

def load_testcases(path):
    # for path in all_path(dirname):
    #   with open(path,'r',encoding='utf8') as fp:
    #       json_data = json.load(fp)
    # return json_data
    with open(path,'r',encoding='utf8') as fp:
        json_data = json.load(fp)
    return json_data


def all_path(dirname):
    result = []
    filter = '.json'
    for  maindir, subdir, file_name_list in os.walk(dirname):
        for file_name in file_name_list:
            apath = os.path.join(maindir, file_name)
            if os.path.splitext(apath)[1] in filter:
                result.append(apath)

    return result
