# Created byMartin.cz
# Copyright (c) Martin Strohalm. All rights reserved.

import ssl
import re
import time
import urllib.parse
import urllib.request
from . import config

# init last request time
_last_request_time = 0

# define page pattern
_PAGE_PATTERN = re.compile("page=([0-9]+)")

# handle SSL certificate
_SSL_CONTEXT = ssl._create_unverified_context()


def request(url, parameters={}, post=False):
    """
    Builds the final URL and opens handler.
    
    Args:
        url: str
            Request URL.
        
        parameters: dict
            Request parameters.
        
        post: bool
            If set to True, request will be sent as POST.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    # remove unset parameters
    parameters = {k: v for k, v in parameters.items() if v is not None}
    
    # set default API key
    parameters['key'] = assert_api_key(parameters.get('key', None))
    
    # parse page number
    if 'page' in parameters and isinstance(parameters['page'], str) and parameters['page'].startswith("http"):
        parameters['page'] = _PAGE_PATTERN.findall(parameters['page'])[0]
    
    # prepare options
    options = urllib.parse.urlencode(parameters, doseq=True)
    
    # assert time restrictions
    global _last_request_time
    while True:
        delay = _last_request_time + config.REQUEST_DELAY - time.time()
        if delay <= 0:
            _last_request_time = time.time()
            break
        else:
            time.sleep(delay)
    
    # send request
    if post:
        handle = urllib.request.urlopen(url, options.encode('utf8'), context=_SSL_CONTEXT)
    else:
        url = "%s?%s" % (url, options)
        handle = urllib.request.urlopen(url, context=_SSL_CONTEXT)
    
    return handle


def assert_api_key(api_key):
    """Checks given API key and use default."""
    
    # use module key
    if not api_key:
        api_key = config.API_KEY
    
    # check key
    if not api_key:
        raise ValueError("API key not specified. Run rebrick.init() to set your key for all functions.")
    
    return api_key


def assert_user_token(user_token):
    """Checks given user token and use default."""
    
    # use module token
    if not user_token:
        user_token = config.USER_TOKEN
    
    # check token
    if not user_token:
        raise ValueError("User token must be specified. Run rebrick.init() to set your token for all functions.")
    
    return user_token
