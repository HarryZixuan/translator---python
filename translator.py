import urllib.request
import urllib.parse
import json

i = 10

while i>0:
    content = input("please enter the content you wanna translate\n")
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    data ={}
    data['i'] = content
    data['from'] ='AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '1527751477870'
    data['sign'] = '1588066ffb65f2fadef67ad072dff691'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom']= 'fanyi.web'
    data['action'] = 'FY_BY_REALTIME'
    data['typoResult'] = 'false'
    data = urllib.parse.urlencode(data).encode('utf-8')
    response = urllib.request.urlopen(url, data)
    html = response.read().decode('utf-8')
    result = json.loads(html)
    print((result['translateResult'][0][0]['tgt']))