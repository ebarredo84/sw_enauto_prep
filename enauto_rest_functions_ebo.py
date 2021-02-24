
#---------MODEL-----------
import requests
import json
import base64

from ncclient import manager,xml_
import xmltodict
import xml.dom.minidom
import os
import sys

#------USER INTERFACE (VIEW)----------
import tkinter as tk

#------REST FUNCTIONS-----------------
def POST_EBO(url,services,headers,data):
    requests.packages.urllib3.disable_warnings()                    #deshabilitar SSL certificate warnings
    url+=services           #concateno url completo
    resp=requests.post(url,headers=headers,data=data,verify=False)  #post con los datos anteriores
    return resp
def GET_EBO(url,services,headers):
    requests.packages.urllib3.disable_warnings()                    #deshabilitar SSL certificate warnings
    url+=services                                                   #concateno url completo
    resp = requests.get(url, headers=headers, verify=False)         #get con los datos anteriores
    return resp
def PATCH_EBO(url,services,headers,data):
    requests.packages.urllib3.disable_warnings()                    #deshabilitar SSL certificate warnings
    url+=services                                                   #concateno url completo
    resp=requests.patch(url,headers=headers,data=data,verify=False)  #post con los datos anteriores
    print("Request status: ", resp.status_code)                     #imprime el estado del post 200 OK
    return resp
def PUT_EBO(url,services,headers,data):
    requests.packages.urllib3.disable_warnings()                    #deshabilitar SSL certificate warnings
    url+=services                                                   #concateno url completo
    resp=requests.put(url,headers=headers,data=data,verify=False)  #post con los datos anteriores
    print("Request status: ", resp.status_code)                     #imprime el estado del post 200 OK
    return resp
def DELETE_EBO(url,services,headers):
    requests.packages.urllib3.disable_warnings()                    #deshabilitar SSL certificate warnings
    url+=services                                                   #concateno url completo
    resp = requests.delete(url, headers=headers, verify=False)         #get con los datos anteriores
    print("Request status: ", resp.status_code)                     #imprime el estado del post 200 OK
    return resp

#------NETCONF FUNCTIONS
def GET_SCHEMA_NETCONF(host,netconf_port,username,password,identifier):
    with manager.connect(host=host,port=netconf_port,username=username,password=password,hostkey_verify=False) as m:
        netconf_reply=m.get_schema(identifier=identifier)
    return netconf_reply

def GET_NETCONF(host,netconf_port,username,password,source,netconf_filter):
    with manager.connect(host=host,port=netconf_port,username=username,password=password,hostkey_verify=False) as m:
        netconf_reply=m.get_config(source,filter=netconf_filter)
    return netconf_reply

def EDIT_NETCONF(host,netconf_port,username,password,target,netconf_data):
    with manager.connect(host=host,port=netconf_port,username=username,password=password,hostkey_verify=False) as m:
        netconf_reply=m.edit_config(netconf_data,target=target)
    return netconf_reply