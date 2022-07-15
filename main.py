import ovh
from requests import get
from dotenv import load_dotenv
import os

load_dotenv()

client = ovh.Client(

    endpoint = os.environ["ENDPOINT"],
    application_key = os.environ["APPLICATION_KEY"],    # Application Key
    application_secret = os.environ["APPLICATION_SECRET"],  # Application Secret
    consumer_key = os.environ["CONSUMER_KEY"],       # Consumer Key
)

domainZone = client.get('/domain/zone/' + os.environ['WEBSITE'] + '/export')

domainRecord = client.get('/domain/zone/' + os.environ['WEBSITE'] + '/record',
                          # Filter the value of fieldType property(like)(type: zone.NamedResolutionFieldTypeEnum)
                          fieldType='A',
                          # Filter the value of subDomain property(like)(type: string)
                          subDomain=None,
                          )
ip2 = get('http://myexternalip.com/raw').text
ip = get('https://api.ipify.org').text

if domainZone.find(ip) == -1:
    print(ip2)
    print(ip)
    # result = client.put('/domain/zone/taojouet.com/record/5226221090',
    #     target=ip, # Resource record target (type: string)
    # )
    # print(result);


# result = client.get('/domain/zone/{zoneName}/export')
