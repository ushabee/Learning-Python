import requests
from requests import Response
def website(url:str)->str :
    if url.startswith(('http://','https://')):
     return url
    else:
       return (f'http://{url}')
def web_check(url:str, timeout: int=10)->None:
    url=website(url)

    print(f'\n.....website status diagnostics {url}.....')
    try:
        response: Response = requests.get(url, timeout=timeout)
        status_code: int = response.status_code
        content: str = response.text  # safe string
        encoding: str | None = response.encoding

        print(f'status_code: {status_code}')
        print(f'content (first 200 chars): {content.strip()[:200]}...')
        # print(f'content (first 200 chars): {content[:100]}...')  # prevent huge output
        print(f'encoding: {encoding}')
    except Exception as e:
       print(f'error occured: {e}')

    # status_code:int=response.status_code
    # #elapsed_time:float=response.elapsed
    # content:str=response.text
    # encoding:str|None= response.encoding
    # print(f'status_code:{status_code}')
    # #print(f'elapsed_time:{elapsed_time}s')
    # print(f'content:{content}')
    # print(f'encoding:{encoding}')

web_check('www.apple.com')

    

    
    

       
 