



#--------------------SD WAN MENUS NIVEL 1-----------------------------
SDWAN_L1_MENU="""Estás usando SD WAN SANDBOX ALWAYS ON
1) SANDBOX SDWAN1    (https://sandbox-sdwan-1.cisco.com:443/)   "USAR ESTE"
2) SANDBOX SDWAN     (https://sandboxsdwan.cisco.com:8443/)     "ESTE TIENE PROBLEMAS DE AUTHENTICACIÓN"
¿Que opción deseas usar?"""
#--------------------SD WAN MENUS NIVEL 2-----------------------------
SDWAN_L2_MENU="""Estás usando SD WAN SANDBOX ALWAYS ON
    1) POST SECURITY                     (POST /j_security_check)
    2) CERTIFICATE MANAGEMENT API MENU
    3) DEVICE INVENTORY API MENU
    4) ADMINISTRATION API MENU
    5) CONFIGURATION API MENU            
    6) MONITORING API MENU
    7) REAL-TIME MONITORINGGET API MENU
    8) TROUBLESHOOT API MENU
    ¿Que opción deseas usar?"""
#--------------------SD WAN MENUS NIVEL 3-----------------------------
SDWAN_CERTIFICATION_MANAGEMENT_MENU="""Estás usando Certification Management API
    Estás usando CERTIFICATION MANAGEMENTE API
    1)  CERTIFICATE DEVICE DETAILS                  (GET /certificate/device/details)                           
    2)  VSMART LIST CERTIFICATE                     (GET /certificate/vsmart/list)
    3)  VEDGE LIST CERTIFICATE                      (GET /certificate/vedge/list)
    4)  CSR (certificate signing request) DETAILS   (GET /certificate/csr/details)        (MUESTRA LOS CAMPOS DE LOS CSR)
    ¿Que opción deseas usar?"""

SDWAN_DEVICE_INVENTORY_MENU="""Estás usando Device Inventory API
    Estás usando DEVICE INVENTORY API
    1)  DEVICE VEDGES                               (GET /system/device/{deviceCategory=vedges})                          
    2)  DEVICE CONTROLLERS                          (GET /system/device/{deviceCategory=controllers})
    3)  DEVICE VEDGES STATUS                        (GET /system/device/controllers/vedge/status)
    4)  DEVICE MANAGMENTE SISTEM IP                 (GET /system/device/management/systemip
    ¿Que opción deseas usar?"""

SDWAN_ADMINISTRATION_MENU="""Estás usando ADMINISTRATION API
    1)  AUDITLOG                                    (GET /auditlog)                      (MUCHA INFORMACIÓN, TIEMPO LARGO DE ESPERA)
    2)  USER                                        (GET /admin/user)                    (USERNAME Y GROUP)
    3)  USER GROUP KEY VALUES                       (GET /admin/usergroup/keyvalue)      (ENLISTA LOS TIPOS DE GRUPOS)
    incluir GET /device/action/reboot
    ¿Que opción deseas usar?"""

SDWAN_CONFIGURATION_MENU="""Estás usando CONFIGURATION API
    1)  DEVICE FEATURELIST      	                (GET /device/featurelist?deviceId=X.Y.Z.W)                  (SE REQUIERE UNA IP)
    2)  DEVICE TEMPLATE          	                (GET /template/device)                                      *****
    3)  GET FEATURE TEMPLATE	                    (GET /template/feature?summary=false)
    4)  PUT FEATURE TEMPLATE                        (PUT /template/feature/{templateId})                        (EN PRUEBAS)
    5)  DELETE FEATURE TEMPLATE                     (DEL /template/feature/{templateId})                        (EN PRUEBAS)
    6)  DEVICE RUNNING CONFIG TEMPLATE          	(GET /template/config/running/{deviceUUID})                 (SE REQUIERE UN UUID)
    7)  GET CLI CONTROLLER DEVICE CONFIG TEMPLATE   (GET /template/config/device/mode/cli?type=controller)
    8)  GET CLI VMANAGE DEVICE CONFIG TEMPLATE      (GET /template/config/device/mode/cli?type=vmanage)
    9)  POST CLI DEVICE CONFIG TEMPLATE             (POS /template/config/device/mode/cli)                      (EN PRUEBAS)*****    
    A)  GET ATTACHED DEVICE TEMPLATE                (GET /template/device/config/attached/{masterTemplateId})   (EN PRUEBAS)*****
    B)  POST ATTACHED DEVICE TEMPLATE               (POS /template/device/config/attachfeature                  (EN PRUEBAS)*****
    ¿Que opción deseas usar?"""

SDWAN_MONITORING_MENU="""Estás usando MONITORING API
    1)  ALARMS                                      (GET /alarms)                                              (NO HAY ALARMAS)
    2)  ALARMS STATS                                (GET /alarms/stats)
    3)  DEVICES                                     (GET /device)                                               ****(DEVASC)
    4)  DEVICES STATUS                              (GET /device/status)                                       (OBTENGO POCA INFORMACIÓN)
    5)  DEVICE COUNTERS                             (GET /device/counters)
    6)  DATA DEVICES STATS                          (GET /data/device/statistics)                              (MUESTRA TIPOS)
    7)  EVENT LISTENERS                             (GET /event/listeners)                                     
    8)  EVENT TYPE (KEY VALUES)                     (GET /event/types/keyvalue)                                (MUESTRA TIPOS DE EVENTOS)
    ¿Que opción deseas usar?"""

SDWAN_RT_MONITORING_MENU="""Estás usando REAL TIME MONITORING API
    1) ARP                                          (GET /device/arp)                                          (SE REQUIERE UNA IP)
    2) CONTROL SUMMARY                  	        (GET /device/control/summary)                              (SE REQUIERE UNA IP)
    3) WAN INTERFACE CONTROL                        (GET /device/control/waninterface)                         (SE REQUIERE UNA IP)
    4) DHCP INTERFACE                  	            (GET /device/dhcp/interface)                               (SE REQUIERE UNA IP)
    5) DHCP SERVER                     	            (GET /device/dhcp/server)                                  (SE REQUIERE UNA IP)
    6) DHCPV6 INTERFACE                	            (GET /device/dhcpv6/interface)                             (SE REQUIERE UNA IP)
    7) INTERFACE                        	        (GET /device/interface)                                    (SE REQUIERE UNA IP)
    8) ROUTE TABLE IP                  	            (GET /device/ip/routetable)                                (SE REQUIERE UNA IP, ERROR CON RUTAS CONECTADAS)
    incluir GET /device/app-route/statistics
    incluir GET /device/users
    incluir GET /device/bfd/history
    ¿Que opción deseas usar?"""

SDWAN_TROUBLESHOOT_MENU="""Estás usando TROUBLESHOOT MONITORING API
    1)  DEVICE ACTIVE COUNT TASK STATUS          	(GET /device/action/status/tasks/activeCount)
    2)  DEVICE CLEAN STATUS                     	(GET /device/action/status/clean)                          (SE REQUIERE CLEANSTATUS, EN PRUEBAS)
    3)  GROUP LIST                                  (GET /group)
    4)  DEVICE GROUPS                               (GET /group/device)
    5)  DEVICES IN A GROUP                          (GET /group/devices)                                       (SE REQUIERE GROUPID, EN PRUEBAS)
    6)  DEVICES GROUP MAP                       	(GET /group/map/devices)
    7)  LINKS DEVICES GROUP MAP                 	(GET /group/map/devices/links)                             (SE REQUIERE GROUPID, EN PRUEBAS)
    ¿Que opción deseas usar?"""