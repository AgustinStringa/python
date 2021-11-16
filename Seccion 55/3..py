from urllib.request import Request, urlopen
import json
import pprint as pp


urlAPI = 'https://reqres.in/api/users/2'

request = Request(urlAPI, headers={
                  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0'})
# urllib.request.Request

httpclient = urlopen(request)
# HttpClient

bytess = httpclient.read()

json_respuesta = json.loads(bytess.decode('utf-8'))
# dict

pp.pprint(json_respuesta['data'])
