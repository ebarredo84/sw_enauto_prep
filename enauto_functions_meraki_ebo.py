#------USER INTERFACE (VIEW)----------
import tkinter as tk
from enauto_gui_functions_ebo import *

#------CONTROLLER--------------------
import json
import base64
from enauto_functions_interface_ebo import *

def MERAKI_GET_HEADERS(ans1,text_box):
    headers=SANDBOX_AUTHENTICATION(ans1,text_box)
    return headers

def MERAKI_DASHBOARD_ORGANIZATIONS(ans1,headers,text_box):
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="organizations",headers=headers,text_box=text_box)
    PRINT_TABLE_IN_TEXT(text_box,response.json(),
                        size1="30",name1="Organization ID",data1='id',
                        size2="30",name2="Organization Name",data2='name')

def MERAKI_DASHBOARD_NETWORKS(ans1,headers,text_box):
    org_id=input("Por favor introducir un organization Id, por ejemplo 681155\n")
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="organizations/"+org_id+"/networks",headers=headers,text_box=text_box)
    PRINT_TABLE_IN_TEXT(text_box,response.json(),
                        size1="15",name1="Organization ID",data1='organizationId',
                        size2="30",name2="Network ID",data2='id',
                        size3="40",name3="Network Name",data3='name')

def MERAKI_DASHBOARD_DEVICES(ans1,headers,text_box):
    network_id=input("Por favor introducir un netwokr Id, por ejemplo L_783626335162466320\n")
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="networks/"+network_id+"/devices",headers=headers,text_box=text_box)
    PRINT_TABLE_IN_TEXT(text_box,response.json(),
                        size1="30",name1="Firmware",data1='firmware',
                        size2="15",name2="Model",data2='model',
                        size3="20",name3="Serial",data3='serial',
                        size4="20",name4="Lan IP",data4='lanIp',
                        size5="20",name5="Latitud",data5='lat',
                        size6="20",name6="Longitud",data6='lng')

def MERAKI_DASHBOARD_SSID(ans1,headers,text_box):
    network_id=input("Por favor introducir un netwokr Id, por ejemplo L_783626335162466320\n")
    #SELECCIONO ENTRE LOS DOS DNAC, EJECUTO EL GET, IMPRIMO RESPUESTA
    response=GET_FUNCTION_EBO(ans1=ans1,services="networks/"+network_id+"/ssids",headers=headers,text_box=text_box)
    PRINT_TABLE_IN_TEXT(text_box,response.json(),
                        size1="40",name1="SSID Name",data1='name',
                        size2="30",name2="Auth Mode",data2='authMode',
                        size3="20",name3="IP Assig Mode",data3='ipAssignmentMode',
                        size4="20",name4="Band Selection",data4='bandSelection')