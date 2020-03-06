
import json
import requests
import utils

    
def run_single_testcase(testcase):
    req_kwargs = testcase['request']

    try:
        url = req_kwargs.pop('url')
        method = req_kwargs.pop('method')
    except KeyError:
          raise Exception('Params Error')

    resp_obj = requests.request(url=url,method= method,**req_kwargs)
    diff_content = utils.diff_reponse(resp_obj,req_kwargs['response'])
    success = False if diff_content else True
    return success, diff_content

          