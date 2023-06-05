import untangle

myresponse = open("statusReply.xml","r")
test = myresponse

respuesta = untangle.parse(test)
print(respuesta.services.service[0].name.cdata)
print(respuesta.services.service[0].status.cdata)
print(respuesta.services.service[1].name.cdata)
print(respuesta.services.service[1].status.cdata)