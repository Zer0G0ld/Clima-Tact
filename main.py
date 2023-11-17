import requests
import json

iTOKEN = "ad5d4371b478be61a04059701d79fc1e"
iTIPODECONSULTA = 1

# http://apiadvisor.climatempo.com.br/api/v1/locale/city?name=São Paulo&state=SP&token=your-app-token
if iTIPODECONSULTA == 1:
    iCITY = input("Informe o nome da cidade: ")
    iURL = "http://apiadvisor.climatempo.com.br/api/v1/locale/city?name=" + str(iCITY) + "&token=" + str(iTOKEN)
    iRESPONSE = requests.request("GET", iURL)
    iRESTORNO_REQ = json.loads(iRESPONSE.text)
    for iCHAVE in iRESTORNO_REQ:
        iID = iCHAVE["id"]
        iNAME = iCHAVE["name"]
        iSTATE = iCHAVE["state"]
        iCOUNTRY = iCHAVE["country"]
        print("id: {} iNAME {} iSTATE {} iCOUNTRY {}".format(iID, iNAME, iSTATE, iCOUNTRY))