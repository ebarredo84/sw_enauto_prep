#--------MODEL----------------
from enauto_rest_functions_ebo import *

#------USER INTERFACE (VIEW)----------
import tkinter as tk
from enauto_gui_functions_ebo import *

#------CONTROLLER--------------------
import json
import base64

#---------REST INTERFACE FUNCTIONS---------------
def GET_FUNCTION_EBO(ans1,services,headers,text_box):
    #SELECCIONO EL SANDBOX
    url=SANDBOX_INFO(ans1)
    response=GET_EBO(url=url,services=services,headers=headers)
    PRINT_STATUS_CODE(response,text_box)
    return response

def POST_FUNCTION_EBO(ans1,services,headers,text_box,data):
    #SELECCIONO EL SANDBOX
    url=SANDBOX_INFO(ans1)

    response=POST_EBO(url=url,services=services,headers=headers,data=data)
    PRINT_STATUS_CODE(response,text_box)
    return response

def PATCH_FUNCTION_EBO(ans1,services,headers,text_box,data):
    #SELECCIONO EL SANDBOX
    url=SANDBOX_INFO(ans1)

    response=PATCH_EBO(url=url,services=services,headers=headers,data=data)
    PRINT_STATUS_CODE(response,text_box)
    return response

def PUT_FUNCTION_EBO(ans1,services,headers,text_box,data):
    #SELECCIONO EL SANDBOX
    url=SANDBOX_INFO(ans1)

    response=PUT_EBO(url=url,services=services,headers=headers,data=data)
    PRINT_STATUS_CODE(response,text_box)
    return response

def DELETE_FUNCTION_EBO(ans1,services,headers,text_box):
    #SELECCIONO EL SANDBOX
    url=SANDBOX_INFO(ans1)
        
    response=DELETE_EBO(url=url,services=services,headers=headers)
    PRINT_STATUS_CODE(response,text_box)
    return response

#---------NETCONF INTERFACE FUNCTIONS---------------------------
def GET_SCHEMA_IOS_NETCONF(ans1,identifier):
    #SELECCIONO EL IOS, POR EL MOMENTO SOLO HAY UNO
    if ans1[1]=="1":
        host="ios-xe-mgmt.cisco.com"
        username="developer"
        password="C1sco12345"
        port=10000   #netconf port
    
    netconf_reply=GET_SCHEMA_NETCONF(host=host,netconf_port=port,username=username,password=password,identifier=identifier)
    #print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
    return xmltodict.parse(netconf_reply.xml)

def GET_IOS_NETCONF(ans1,source,netconf_filter):
    #SELECCIONO EL IOS, POR EL MOMENTO SOLO HAY UNO
    if ans1[1]=="1":
        host="ios-xe-mgmt.cisco.com"
        username="developer"
        password="C1sco12345"
        port=10000   #netconf port
    
    netconf_reply=GET_NETCONF(host=host,netconf_port=port,username=username,password=password,source=source,netconf_filter=netconf_filter)
    #print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
    return xmltodict.parse(netconf_reply.xml)

def EDIT_IOS_NETCONF(ans1,target,netconf_data):
    #SELECCIONO EL IOS, POR EL MOMENTO SOLO HAY UNO
    if ans1[1]=="1":
        host="ios-xe-mgmt.cisco.com"
        username="developer"
        password="C1sco12345"
        port=10000   #netconf port
 
    netconf_reply=EDIT_NETCONF(host=host,netconf_port=port,username=username,password=password,target=target,netconf_data=netconf_data)
    #print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
    return xmltodict.parse(netconf_reply.xml)

#---------SANDBOX INFORMATION FOR DNAC, SDWAN Y MERAKI-------------------
def SANDBOX_INFO(ans1):
    #SELECCIONO ENTRE LOS DOS IOS XE
    if ans1[:2]=="11":
        host="ios-xe-mgmt.cisco.com"
        port=9443   #restconf port
        url="https://"+host+":"+str(port)+"/restconf/data/"
    #elif ans1[:2]=="12":
    #SELECCIONO ENTRE LOS DOS DNAC
    elif ans1[:2]=="21":url="https://sandboxdnac.cisco.com/dna/intent/api/"
    elif ans1[:2]=="22":url="https://sandboxdnac2.cisco.com/dna/intent/api/"
    #SELECCIONO ENTRE LOS DOS SDWAN
    elif ans1[:2]=="31":url="https://sandbox-sdwan-1.cisco.com:443/"
    elif ans1[:2]=="32":url="https://sandboxsdwan.cisco.com:8443/"
    #SELECCIONO ENTRE LOS DOS MERAKI
    elif ans1[:2]=="41":url="https://api.meraki.com/api/v1/"
    elif ans1[:2]=="42":url="https://api.meraki.com/api/v0/"
    return url

#----------SANDBOX AUTHENTICATION FOR IOS XE, DNAC, SDWAN Y MERAKI------------------------
def SANDBOX_AUTHENTICATION(ans1,text_box):
    #SELECCIONO ENTRE LOS DOS IOS XE
    if ans1[:2]=="11":
        user="developer"
        password="C1sco12345"
    #elif ans1[:2]=="12": #PARA UN SEGUNDO SANDBOX DE IOS XE
    #SELECCIONO ENTRE LOS DOS DNAC
    elif ans1[:2]=="21":
        url="https://sandboxdnac2.cisco.com:443/dna/intent/api/"
        user="dnacdev"
        password="D3v93T@wK!"
    elif ans1[:2]=="22":
        url="https://sandboxdnac.cisco.com:443/dna/intent/api/"
        user="devnetuser"
        password="Cisco123!"
    #SELECCIONO ENTRE LOS DOS SD WAN
    elif ans1[:2]=="31":
        url="https://sandbox-sdwan-1.cisco.com:443/"
        j_username="devnetuser"
        j_password="RG!_Yw919_83"
    elif ans1[:2]=="32":
        url="https://sandboxsdwan.cisco.com:8443/"
        j_username="devnetuser"
        j_password="C1sco12345"
    #SELECCIONO ENTRE LOS DOS MERAKI
    elif ans1[:2]=="41":
        api_key="15da0c6ffff295f16267f88f98694cf29a86ed87"
    elif ans1[:2]=="42":
        api_key="6bec40cf957de430a6f1f2baa056b99a4fac9ea0"


    #SI ES IOS XE
    if ans1[0]=="1":
        authorization=base64.b64encode(str(user+":"+password).encode('UTF-8'))
        headers={"Content-type": "application/yang-data+json",
            "Accept": "application/yang-data+json",
            "Authorization": "Basic "+authorization.decode('utf-8')}
        PRINT_HEADERS(headers,text_box)
        return headers 
    #SI ES DNA CENTER
    elif ans1[0]=="2":
        url=url.replace("intent","system")
        authorization=base64.b64encode(str(user+":"+password).encode('UTF-8'))
        headers={"Content-type": "application/json",
                "Authorization": "Basic "+authorization.decode('utf-8')}    #variable diccionario para el encabezado
        data=""
        services="v1/auth/token"
    #SI ES SDWAN
    elif ans1[0]=="3":
        headers={"Content-Type": "application/x-www-form-urlencoded"}            
        data = "j_username="+j_username+"&j_password="+j_password        #variable para el cuerpo (usuario y clave)
        services="j_security_check"
    #SI ES MERAKI
    elif ans1[0]=="4":
        headers = {"content-type": "application/json",
                    "Accept": "application/json",
                    "X-Cisco-Meraki-API-Key": api_key}
        PRINT_HEADERS(headers,text_box)
        return headers
    
    #PIDO EL TOKEN
    response=POST_EBO(url=url,services=services,headers=headers,data=data)
    #IMPRIMO EN EL TEXT BOX
    PRINT_STATUS_CODE(response,text_box)
    #EXTRAIGO TOKEN Y CONFORMO NUEVO HEADER
    #SI ES DNA CENTER
    if ans1[0]=="2":
        token=response.json()["Token"]
        headers={"content-type": "application/json",
                    "x-auth-token": token}
    #SI ES SDWAN
    elif ans1[0]=="3":
        j_session_id=dict(response.cookies)['JSESSIONID']
        headers={"Cookie": "JSESSIONID="+j_session_id}
    
    return headers

 

