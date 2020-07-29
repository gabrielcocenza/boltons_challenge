import requests
import xmltodict
import base64
import json

def get_nfes_data():
	url = "https://sandbox-api.arquivei.com.br/v1/nfe/received"
	headers = {
        'x-api-id': 'f96ae22f7c5d74fa4d78e764563d52811570588e',
        'x-api-key': 'cc79ee9464257c9e1901703e04ac9f86b0f387c2',
        'Content-Type': 'application/json'
	}
	response = requests.request("GET", url, headers=headers)
	return response.json()['data']

def extract_total_value(xml_64):
	xml = decode_64(xml_64)
	if(xml.get('nfeProc')):
		return float(xml['nfeProc']['NFe']['infNFe']['total']['ICMSTot']['vNF'])
	else:
		return float(xml['NFe']['infNFe']['total']['ICMSTot']['vNF'])


def decode_64(xml_64):
	base64_bytes = xml_64.encode('ascii')
	message_bytes = base64.b64decode(base64_bytes)
	xml = message_bytes.decode('ascii')
	return xml_to_dict(xml)


def xml_to_dict(xml_decoded):
	return xmltodict.parse(xml_decoded)


