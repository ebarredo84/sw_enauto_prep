#------USER INTERFACE (VIEW)----------
import tkinter as tk
from enauto_gui_functions_ebo import *

#------CONTROLLER--------------------
import json
import base64
from enauto_functions_interface_ebo import *

#---------AUTHENTICATION------------
def SDWAN_AUTHENTICATION(ans1,text_box):
    headers=SANDBOX_AUTHENTICATION(ans1,text_box)
    return headers

#---------CERTIFICATION-------------------
def SDWAN_CERTIFICATION_DEVICE_DETAILS(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/certificate/device/details",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_TABLE_IN_TEXT(text_box,response.json()['data'],
                        size1="20",name1="Name",data1='name',
                        size2="20",name2="Type",data2='type',
                        size3="20",name3="Subtype",data3='subtype',
                        size4="20",name4="Attibutes",data4='attributes')

def SDWAN_CERTIFICATION_VSMART_LIST(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/certificate/vsmart/list",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_TABLE_IN_TEXT(text_box,response.json()['data'],
                        size1="20",name1="Device Type",data1='deviceType',
                        size2="40",name2="Serial Numbers",data2='serialNumber',
                        size3="50",name3="UUID",data3='uuid',
                        size4="20",name4="IP Address",data4='local-system-ip')

def SDWAN_CERTIFICATION_VEDGE_LIST(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/certificate/vedge/list",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_TABLE_IN_TEXT(text_box,response.json()['data'],
                        size1="15",name1="Device Type",data1='deviceType',
                        size2="35",name2="Serial Numbers",data2='serialNumber',
                        size3="45",name3="UUID",data3='uuid',
                        size4="40",name4="Chasis Number",data4='chasisNumber')

def SDWAN_CERTIFICATION_CSR_DETAILS(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/certificate/csr/details",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_CONTENT_JSON(response,text_box)

#---------DEVICE INVENTORY-------------------
def SDWAN_DEVICE_INVENTORY_VEDGES(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/system/device/vedges",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_TABLE_IN_TEXT(text_box,response.json()['data'],
                        size1="20",name1="Device Type",data1='deviceType',
                        size2="50",name2="UUID",data2='uuid',
                        size3="20",name3="Operation Mode",data3='configOperationMode')

def SDWAN_DEVICE_INVENTORY_CONTROLLERS(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/system/device/controllers",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_TABLE_IN_TEXT(text_box,response.json()['data'],
                        size1="15",name1="Device Type",data1='deviceType',
                        size2="45",name2="Device Name",data2='ncsDeviceName',
                        size3="40",name3="UUID",data3='uuid',
                        size4="15",name4="Operation Mode",data4='configOperationMode',
                        size5="15",name5="IP Address",data5='deviceIP')

def SDWAN_DEVICE_INVENTORY_VEDGES_STATUS(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/system/device/controllers/vedge/status",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_TABLE_IN_TEXT(text_box,response.json()['data'],
                        size1="20",name1="Total Controllers",data1='totalControllers',
                        size2="50",name2="Offline Controllers",data2='ControllersOutOfSync')

def SDWAN_DEVICE_INVENTORY_MNG_SYS_IP(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/system/device/management/systemip",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_TABLE_IN_TEXT(text_box,response.json()['data'],
                        size1="20",name1="Device Type",data1='deviceType',
                        size2="50",name2="Chasis Number",data2='chasisNumber',
                        size3="50",name3="Manage IP Address",data3='managementSystemIP',
                        size4="20",name4="ID Number",data4='_id')

#---------ADMINISTRATION API-------------------
def SDWAN_ADMINISTRATION_AUDITLOG(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/auditlog",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_TABLE_IN_TEXT(text_box,response.json()['data'],
                        size1="50",name1="Log ID",data1='logid',
                        size2="20",name2="Log User",data2='loguser',
                        size3="20",name3="Entry Time",data3='entry_time',
                        size4="20",name4="Log User IP",data4='logusersrcip')

def SDWAN_ADMINISTRATION_USER(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/admin/user",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_CONTENT_JSON(response,text_box)

def SDWAN_ADMINISTRATION_USER_GROUP(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/admin/usergroup/keyvalue",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_CONTENT_JSON(response,text_box)

#---------CONFIGURATION API-------------------
def SDWAN_CONFIGURATION_DEVICE_FEATURELIST(ans1,headers,text_box):
    deviceId=input("Por favor introducir un deviceId, ejemplo: 10.10.1.1\n")
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/device/featurelist?deviceId="+deviceId,headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_CONTENT_JSON(response,text_box)

def SDWAN_CONFIGURATION_DEVICE_TEMPLATE(ans1,headers,text_box):
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/template/device",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_TABLE_IN_TEXT(text_box,response.json()['data'],
                        size1="40",name1="Template ID",data1='templateId',
                        size2="30",name2="Template Name",data2='templateName',
                        size3="20",name3="Device Type",data3='deviceType',
                        size4="20",name4="Devices Attached",data4='devicesAttached')

def SDWAN_CONFIGURATION_GET_FEATURE_TEMPLATE(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/template/feature?summary=false",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_TABLE_IN_TEXT(text_box,response.json()['data'],
                        size1="40",name1="Template ID",data1='templateId',
                        size2="55",name2="Template Name",data2='templateName',
                        size3="30",name3="Template Type",data3='templateType',
                        size4="10",name4="Dev. Att.",data4='devicesAttached',
                        size5="10",name5="Mas. Att.",data5='attachedMastersCount')

#def SDWAN_CONFIGURATION_PUT_FEATURE_TEMPLATE(ans1,headers,text_box):
#    4)  PUT FEATURE TEMPLATE	                    (PUT /template/feature/{templateId})


#def SDWAN_CONFIGURATION_DEL_FEATURE_TEMPLATE(ans1,headers,text_box):
#    5)  DEL FEATURE TEMPLATE                        (DEL /template/feature/{templateId})

def SDWAN_CONFIGURATION_DEVICE_RUNCONFIG_TEMPLATE(ans1,headers,text_box):
    deviceUUID=input("Por favor introducir un device UUID, ejemplo: 81ac6722-a226-4411-9d5d-45c0ca7d567b\n")
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/template/config/running/"+deviceUUID,headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_CONTENT_JSON(response,text_box)
    #print(response.content[0])

def SDWAN_CONFIGURATION_GET_CLI_CONTROLLER_DEV_CONFIG_TEMP(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/template/config/device/mode/cli?type=controller",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_TABLE_IN_TEXT(text_box,response.json()['data'],
                        size1="20",name1="Device IP",data1='deviceIP',
                        size2="40",name2="UUID",data2='uuid',
                        size3="20",name3="Host Name",data3='host-name')

def SDWAN_CONFIGURATION_GET_CLI_VMANAGE_DEV_CONFIG_TEMP(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/template/config/device/mode/cli?type=vmanage",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_TABLE_IN_TEXT(text_box,response.json()['data'],
                        size1="20",name1="Device IP",data1='deviceIP',
                        size2="40",name2="UUID",data2='uuid',
                        size3="20",name3="Host Name",data3='host-name')

#def SDWAN_CONFIGURATION_POS_CLI_DEV_CONFIG_TEMP(ans1,headers,text_box):
#    9)  POST CLI DEVICE CONFIG TEMPLATE             (POS /template/config/device/mode/cli)                      *****    


#def SDWAN_CONFIGURATION_GET_ATTACHED_DEV_TEMP(ans1,headers,text_box):
#    A)  GET ATTACHED DEVICE TEMPLATE                (GET /template/device/config/attached/{masterTemplateId})   *****

#def SDWAN_CONFIGURATION_POS_ATTACHED_DEV_TEMP(ans1,headers,text_box):
#    B)  POST ATTACHED DEVICE TEMPLATE               (POS /template/device/config/attachfeature                  *****

#---------MONITORING API-------------------
def SDWAN_MONITORING_ALARMS(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/alarms",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_CONTENT_JSON(response,text_box)
 
def SDWAN_MONITORING_ALARMS_STATS(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/alarms/stats",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_CONTENT_JSON(response,text_box)
    #PRINT_TABLE_IN_TEXT(text_box,response.json()['Link Update Correlator']['Threads'],
    #                    size1="20",name1="Current State",data1='Current State',
    #                    size2="20",name2="Total Events Counter",data2='Total Events Counter',
    #                    size3="20",name3="Total DB Counter",data3='Total DB Counter')

def SDWAN_MONITORING_DEVICE(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/device",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_TABLE_IN_TEXT(text_box,response.json()['data'],
                        size1="10",name1="Name",data1='host-name',
                        size2="15",name2="IP Address",data2='system-ip',
                        size3="15",name3="IP vManages",data3='connectedVManages',
                        size4="15",name4="Device Type",data4='device-type',
                        size5="40",name5="UUID",data5='uuid',
                        size6="30",name6="Device Model",data6='device-model')

def SDWAN_MONITORING_DEVICE_STATUS(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/device/status",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_TABLE_IN_TEXT(text_box,response.json()['data'],
                        size1="20",name1="Type",data1='type',
                        size2="20",name2="Numbers",data2='count')

def SDWAN_MONITORING_DEVICE_COUNTERS(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/device/counters",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_CONTENT_JSON(response,text_box)

def SDWAN_MONITORING_DATA_DEV_STATS(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/data/device/statistics",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_CONTENT_JSON(response,text_box)

def SDWAN_MONITORING_EVENT_LISTENERS(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/event/listeners",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_CONTENT_JSON(response,text_box)

def SDWAN_MONITORING_EVENT_TYPE(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/event/types/keyvalue",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_CONTENT_JSON(response,text_box)

#---------REAL TIME MONITORING API-------------------
def SDWAN_RT_MONITORING_ARP(ans1,headers,text_box):
    deviceId=input("Por favor introducir una dirección IP, ejemplo: 10.10.1.1\n")
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/device/arp?deviceId="+deviceId,headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_TABLE_IN_TEXT(text_box,response.json()['data'],
                        size1="20",name1="Host Name",data1='vdevice-host-name',
                        size2="20",name2="Host IP Address",data2='vdevice-name',
                        size3="10",name3="Interface",data3='if-name',
                        size4="20",name4="IP Address",data4='ip',
                        size5="20",name5="MAC Address",data5='mac')

def SDWAN_RT_MONITORING_CONTROL_SUMMARY(ans1,headers,text_box):
    deviceId=input("Por favor introducir una dirección IP, ejemplo: 10.10.1.1\n")
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/device/control/summary?deviceId="+deviceId,headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_CONTENT_JSON(response,text_box)

def SDWAN_RT_MONITORING_CONTROL_WAN_IF(ans1,headers,text_box):
    deviceId=input("Por favor introducir una dirección IP, ejemplo: 10.10.1.1\n")
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/device/control/waninterface?deviceId="+deviceId,headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_CONTENT_JSON(response,text_box)

def SDWAN_RT_MONITORING_DHCP_IF(ans1,headers,text_box):
    deviceId=input("Por favor introducir una dirección IP, ejemplo: 10.10.1.1\n")
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/device/dhcp/interface?deviceId="+deviceId,headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_CONTENT_JSON(response,text_box)

def SDWAN_RT_MONITORING_DHCP_SERVER(ans1,headers,text_box):
    deviceId=input("Por favor introducir una dirección IP, ejemplo: 10.10.1.1\n")
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/device/dhcp/server?deviceId="+deviceId,headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_CONTENT_JSON(response,text_box)

def SDWAN_RT_MONITORING_DHCPV6_IF(ans1,headers,text_box):
    deviceId=input("Por favor introducir una dirección IP, ejemplo: 10.10.1.1\n")
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/device/dhcpv6/interface?deviceId="+deviceId,headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_CONTENT_JSON(response,text_box)

def SDWAN_RT_MONITORING_IF(ans1,headers,text_box):
    deviceId=input("Por favor introducir una dirección IP, ejemplo: 10.10.1.1\n")
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/device/interface?deviceId="+deviceId,headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_TABLE_IN_TEXT(text_box,response.json()['data'],
                        size1="20",name1="Host Name",data1='vdevice-host-name',
                        size2="20",name2="Host IP Address",data2='vdevice-name',
                        size3="10",name3="Interface",data3='ifname',
                        size4="20",name4="AF Type",data4='af-type',
                        size5="20",name5="Admin Status",data5='if-admin-status',
                        size6="20",name6="Op Status",data6='if-oper-status')

def SDWAN_RT_MONITORING_ROUTE_TABLE(ans1,headers,text_box):
    deviceId=input("Por favor introducir una dirección IP, ejemplo: 10.10.1.1\n")
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/device/ip/routetable?deviceId="+deviceId,headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX

    PRINT_TABLE_IN_TEXT(text_box,response.json()['data'],
                        size1="20",name1="Host Name",data1='vdevice-host-name',
                        size2="20",name2="Host IP Address",data2='vdevice-name',
                        size3="10",name3="Protocol",data3='protocol',
                        size4="20",name4="Prefix",data4='prefix',
                        size5="20",name5="Next Hop IP",data5='nexthop-addr',
                        size6="20",name6="Next Hop Interface",data6='nexthop-ifname')

#---------TSHOOT MONITORING API-------------------
def SDWAN_TSHOOT_ACTIVE_COUNT_STATUS_DEV(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/device/action/status/tasks/activeCount",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_CONTENT_JSON(response,text_box)

def SDWAN_TSHOOT_CLEAN_STATUS_DEV(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/device/action/status/clean",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_CONTENT_JSON(response,text_box)

def SDWAN_TSHOOT_GROUP(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/group",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_CONTENT_JSON(response,text_box)

def SDWAN_TSHOOT_GROUP_DEVICE(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/group/device",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_CONTENT_JSON(response,text_box)

def SDWAN_TSHOOT_GROUP_DEVICES(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/group/devices",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_CONTENT_JSON(response,text_box)

def SDWAN_TSHOOT_GROUP_MAP_DEVICES(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/group/map/devices",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_CONTENT_JSON(response,text_box)

def SDWAN_TSHOOT_GROUP_MAP_DEVICES_LINKS(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="dataservice/group/map/devices/links",headers=headers,text_box=text_box)
    #IMPRIMO EN EL TEXT BOX
    PRINT_CONTENT_JSON(response,text_box)