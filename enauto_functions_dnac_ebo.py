#------USER INTERFACE (VIEW)----------
import tkinter as tk
from enauto_gui_functions_ebo import *

#------CONTROLLER--------------------
import json
import base64
from enauto_functions_interface_ebo import *

#---------AUNTHENTICATION------------
def DNAC_AUTHENTICATION(ans1,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC
    headers=SANDBOX_AUTHENTICATION(ans1,text_box)

    return headers
#---------SITE-------------------
def DNAC_SITE(ans1,headers,text_box):
    response=GET_FUNCTION_EBO(ans1=ans1,services="v1/site",headers=headers,text_box=text_box)
    PRINT_TABLE_IN_TEXT(text_box,response.json()['response'],
                        size1="30",name1="Name",data1='name',
                        size2="40",name2="Site Id",data2='id',
                        size3="30",name3="Site Name Hierarchy",data3='siteNameHierarchy')

def DNAC_SITE_HEALTH(ans1,headers,text_box):
    timestamp="1612209600000"    
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="v1/site-health?timestamp="+timestamp,headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_RESPONSE_JSON(response,text_box)


#---------TOPOLOGY------------------- 
def DNAC_TOPOLOGY_PHYSICAL(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="v1/topology/physical-topology",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    #PRINT_RESPONSE_JSON(response,text_box)
    PRINT_TABLE_IN_TEXT(text_box,response.json()['response']['nodes'],
                        size1="20",name1="Host-Name",data1='label',
                        size2="55",name2="Device Model",data2='deviceSeries',
                        size3="20",name3="Ip Address",data3='ip',
                        size4="40",name4="Devices ID",data4='id')

    PRINT_TABLE_IN_TEXT(text_box,response.json()['response']['links'],
                        size1="40",name1="Devices ID 1",data1='source',
                        size2="30",name2="Port Name 1",data2='startPortName',
                        size3="40",name3="Devices ID 2",data3='target',
                        size4="30",name4="Port Name 2",data4='endPortName')

def DNAC_TOPOLOGY_SITE(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="v1/topology/site-topology",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    #PRINT_RESPONSE_JSON(response,text_box)
    PRINT_TABLE_IN_TEXT(text_box,response.json()['response']['sites'],
                        size1="30",name1="Name",data1='name',
                        size2="40",name2="Site Id",data2='id',
                        size3="40",name3="Parent Id",data3='parentId',
                        size4="40",name4="Group Hierarchy",data4='groupNameHierarchy')

def DNAC_TOPOLOGY_VLAN(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="v1/vlan",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_RESPONSE_JSON(response,text_box)

#---------DEVICES------------------- 
def DNAC_DEVICES_NETWORK(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="v1/network-device",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_TABLE_IN_TEXT(text_box,response.json()['response'],
                        size1="30",name1="Host-Name",data1='hostname',
                        size2="60",name2="Id",data2='id',
                        size3="20",name3="Ip Address",data3='managementIpAddress')

def DNAC_DEVICES_INTERFACES(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="v1/interface",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_RESPONSE_JSON(response,text_box)
    PRINT_TABLE_IN_TEXT(text_box,response.json()['response'],
                        size1="20",name1="Pid",data1='pid',
                        size2="40",name2="Device Model",data2='series',
                        size3="30",name3="Port Name",data3='portName',
                        size4="20",name4="Mac Address",data4='macAddress',
                        size5="10",name5="Status",data5='status',
                        size6="15",name6="admin Status",data6='adminStatus')
    

#---------CLIENT -------------------    
def DNAC_CLIENT_HEALTH(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    timestamp="1612209600000"
    response=GET_FUNCTION_EBO(ans1=ans1,services="v1/client-health?timestamp="+timestamp,headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_RESPONSE_JSON(response,text_box)

def DNAC_CLIENT_ENRICHMENT_DETAILS(ans1,headers,text_box):
    entity_type="mac_address"
    entity_value=input("Por favor introducir una mac address, por ejemplo ")
    headers['entity_type']=entity_type
    headers['entity_value']=entity_value
    response=GET_FUNCTION_EBO(ans1=ans1,
                services="v1/client-enrichment-details",
                headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_RESPONSE_JSON(response,text_box)
    del headers['entity_type']
    del headers['entity_value']

def DNAC_ISSUES_ENRICHMENT_DETAILS(ans1,headers,text_box):
    entity_type="mac_address"
    entity_value=input("Por favor introducir una mac address, por ejemplo ")
    headers['entity_type']=entity_type
    headers['entity_value']=entity_value
    response=GET_FUNCTION_EBO(ans1=ans1,
                services="v1/issue-enrichment-details",
                headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_RESPONSE_JSON(response,text_box)
    del headers['entity_type']
    del headers['entity_value']

#---------TEMPLAES------------------- 
def DNAC_TEMPLATES_PROJECT_LIST(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="v1/template-programmer/project",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    #PRINT_RESPONSE_JSON(response,text_box)
    PRINT_TABLE_IN_TEXT(text_box,response.json(),
                        size1="40",name1="Project Name",data1='name',
                        size2="50",name2="Project Id",data2='id',
                        size3="10",name3="Deletable",data3='isDeletable')

def DNAC_TEMPLATES_TEMPLATE_LIST(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="v1/template-programmer/template",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    #PRINT_RESPONSE_JSON(response,text_box)
    PRINT_TABLE_IN_TEXT(text_box,response.json(),
                        size1="40",name1="Project Name",data1='projectName',
                        size2="50",name2="Template Name",data2='name',
                        size3="50",name3="Template Id",data3='templateId')

def DNAC_TEMPLATES_TEMPLATE_DETAILS(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    template_id=input("Por favor introducir un templateId")
    response=GET_FUNCTION_EBO(ans1=ans1,services="v1/template-programmer/template/"+template_id,headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
#    PRINT_RESPONSE_JSON(response,text_box)
    text_box.config(state="normal")                 #habilito la escritura
    text_box.insert(tk.END,response.json()['templateContent']+"\n")
    text_box.config(state="disabled")               #solo lectura

def DNAC_TEMPLATES_TEMPLATE_CREATE(ans1,headers,text_box):
    #COMFORMO EL BODY PARA EL TEMPLATE
    project_id=input("Por favor introducir un Project Id")
    body_template = {
            "templateId": "1c9bf864-44ae-4263-b12a-2de8f2165c44",
            "targetInfo": [
                {
                    "id": "10.10.20.81",
                    "type": "MANAGED_DEVICE_IP",
                    }
            ]
        }

    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=POST_FUNCTION_EBO(ans1=ans1,services="v1/template-programmer/project/"+project_id+"/template",headers=headers,text_box=text_box,data=body_template)
    #IMPRIMO EN EL TEXT BOX
    PRINT_RESPONSE_JSON(response,text_box)    

def DNAC_TEMPLATES_TEMPLATE_DEPLOY(ans1,headers,text_box):
    #COMFORMO EL BODY PARA EL TEMPLATE
    body_template = {
            "forcePushTemplate": "true",
            "targetInfo": [
                {
                    "id": "10.10.20.81",
                    "type": "MANAGED_DEVICE_IP"
                    }
            ],
            "templateId": "1c9bf864-44ae-4263-b12a-2de8f2165c44"
        }

    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=POST_FUNCTION_EBO(ans1=ans1,services="v1/template-programmer/template/deploy",headers=headers,text_box=text_box,data=json.dumps(body_template))
    #IMPRIMO EN EL TEXT BOX
    PRINT_RESPONSE_JSON(response,text_box)

def DNAC_TEMPLATES_TEMPLATE_DEPLOY_STATUS(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="v1/template-programmer/template/deploy/status/deploymentId",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_RESPONSE_JSON(response,text_box)

#---------COMMAND RUNNER------------------- 
def DNAC_COMMAND_RUNNER_LEGIT_READS(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="v1/network-device-poller/cli/legit-reads",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_RESPONSE_JSON(response,text_box)

def DNAC_COMMAND_RUNNER_READ_REQUEST(ans1,headers,text_box):
   #COMFORMO EL BODY
    #body_template = {"name":"my commands",
    #            "commands":["show ver | inc Software, Version", "show clock"],
    #            "deviceUuids":"2f0b7d3b-c9e1-491e-a584-f272b5403719"
    #            }
    body_template = {
        "commands": ["show run"],
        "deviceUuids": ["3c634ae3-dccc-4255-add5-515e7502d4b9"]
    }

    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=POST_FUNCTION_EBO(ans1=ans1,services="v1/network-device-poller/cli/read-request",headers=headers,text_box=text_box,data=json.dumps(body_template))
    #IMPRIMO EN EL TEXT BOX
    PRINT_RESPONSE_JSON(response,text_box)

#---------NETWORK DISCOVERY------------------- 
def DNAC_NETWORK_DISCOVERY_COUNT(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="v1/discovery/count",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_RESPONSE_JSON(response,text_box)

def DNAC_NETWORK_DISCOVERY_LIST(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    count=input("Por favor introducir un número entre 1 y el conteo de la opción 1\n")
    response=GET_FUNCTION_EBO(ans1=ans1,services="v1/discovery/1/"+str(count),headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    #PRINT_RESPONSE_JSON(response,text_box)
    PRINT_TABLE_IN_TEXT(text_box,response.json()['response'],
                        size1="30",name1="Name",data1='name',
                        size2="20",name2="Discovery Type",data2='discoveryType',
                        size3="20",name3="Discovery Id",data3='id')

def DNAC_NETWORK_DISCOVERY_SUMMARY(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    discovery_id=input("Por favor introducir un Discovery Id de la opción 2\n")
    response=GET_FUNCTION_EBO(ans1=ans1,services="v1/discovery/"+discovery_id+"/summary",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_RESPONSE_JSON(response,text_box)

#---------PATH TRACE-------------------
def DNAC_PATH_TRACE_INIT(ans1,headers,text_box):
    #dest_ip=input("Por favor introducir una dirección IP destino\n")
    #source_ip=input("Por favor introducir una dirección IP origen\n")
    #COMFORMO EL BODY
    body_template = {"sourceIP":"10.10.20.82",
                    "destIP":"10.10.20.80"}

    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=POST_FUNCTION_EBO(ans1=ans1,services="v1/flow-analysis",headers=headers,text_box=text_box,data=json.dumps(body_template))
    #IMPRIMO EN EL TEXT BOX
    PRINT_RESPONSE_JSON(response,text_box)

def DNAC_PATH_TRACE_GET_FLOW_ANALYSIS(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="v1/flow-analysis",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    #PRINT_RESPONSE_JSON(response,text_box)
    PRINT_TABLE_IN_TEXT(text_box,response.json()['response'],
                        size1="20",name1="Souce IP",data1='sourceIP',
                        size2="20",name2="Destination IP",data2='destIP',
                        size3="40",name3="Flow Analysis ID",data3='id',
                        size4="20",name4="Flow Analysis Status",data4='status')

def DNAC_PATH_TRACE_GET_FLOW_ANALYSIS_ID(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    flow_analysis_id=input("Por favor introducir un flow analysis de la opción 2\n")
    response=GET_FUNCTION_EBO(ans1=ans1,services="v1/flow-analysis/"+flow_analysis_id,headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_RESPONSE_JSON(response,text_box)

def DNAC_PATH_TRACE_DELETE_FLOW_ANALYSIS_ID(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    flow_analysis_id=input("Por favor introducir un flow analysis de la opción 2\n")
    response=DELETE_FUNCTION_EBO(ans1=ans1,services="v1/flow-analysis/"+flow_analysis_id,headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_RESPONSE_JSON(response,text_box)

#---------TASK-------------------
def DNAC_TASK_LIST(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="v1/task",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_TABLE_IN_TEXT(text_box,response.json()['response'],
                        size1="30",name1="Service Type",data1='serviceType',
                        size2="30",name2="Instance Tenant Id",data2='instanceTenantId',
                        size3="40",name3="Task ID",data3='id')

def DNAC_TASK_ID(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    task_id=input("Por favor introducir un taskId de la opción 1\n")
    response=GET_FUNCTION_EBO(ans1=ans1,services="v1/task/"+task_id,headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_RESPONSE_JSON(response,text_box)

#---------FILE-------------------
def DNAC_FILE_NAMESPACE_LIST(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="v1/file/namespace",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_RESPONSE_JSON(response,text_box)

def DNAC_FILE_NAMESPACE_ID(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    namespace=input("Por favor introducir un namespace de la opción 1\n")
    response=GET_FUNCTION_EBO(ans1=ans1,services="v1/file/namespace/"+namespace,headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_TABLE_IN_TEXT(text_box,response.json()['response'],
                        size1="20",name1="Name Space",data1='nameSpace',
                        size2="40",name2="File Id",data2='id',
                        size3="40",name3="Download Path",data3='downloadPath')

def DNAC_FILE_ID(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    file_id=input("Por favor introducir un fileId de la opción 2\n")
    response=GET_FUNCTION_EBO(ans1=ans1,services="v1/file/"+file_id,headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_RESPONSE_JSON(response,text_box)

#---------EVENT-------------------
def DNAC_EVENT_GET(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="v1/events?tags=ASSURANCE",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    #PRINT_RESPONSE_JSON(response,text_box)
    PRINT_TABLE_IN_TEXT(text_box,response.json(),
                        size1="30",name1="Event Id",data1='eventId',
                        size2="90",name2="Description",data2='description',
                        size3="10",name3="Category",data3='category',
                        size4="10",name4="Severity",data4='severity')

def DNAC_EVENT_SUBSCRIPTION(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="v1/event/subscription",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_RESPONSE_JSON(response,text_box)

def DNAC_EVENT_NOTIFICATIONS(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="v1/event/event-series",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_RESPONSE_JSON(response,text_box)

def DNAC_EVENT_POST_SUSCRIPTION(ans1,headers,text_box):
   #COMFORMO EL BODY
    url_notification=input("Por favor introducir la URL de notificatión\n")
    body_template = {
                "name": "test_event_ebo",
                "description": "",
                "subscriptionEndpoints":
                [
                    {
                    "subscriptionDetails":{
                        "connectorType": "REST",
                        "name": "fred",
                        "description": "created by API",
                        "url": url_notification,
                        "method": "POST",
                        "trustCert": False,
                        }
                    }
                ],
                "filter": {
                    "eventIds": "NETWORK-TEST-EBO-101",
                    "others": []
                    },
                "isPrivate": False,
                }

    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=POST_FUNCTION_EBO(ans1=ans1,services="v1/event/subscription",headers=headers,text_box=text_box,data=body_template)
    #IMPRIMO EN EL TEXT BOX
    PRINT_RESPONSE_JSON(response,text_box)