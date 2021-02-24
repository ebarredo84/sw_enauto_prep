#--------------------DNAC MENUS NIVEL 1-----------------------------
DNAC_L1_MENU="""Estás usando DNA CENTER SANDBOX ALWAYS ON     
1) SANDBOX DNAC2     (https://sandboxdnac2.cisco.com)   "USER ESTE MEJOR"
2) SANDBOX DNAC      (https://sandboxdnac.cisco.com)    "ESTÁ MIGRANDO AL 2"
¿Que opción deseas usar?"""
#--------------------DNAC MENUS NIVEL 2-----------------------------
DNAC_L2_MENU="""Estás usando DNA CENTER SANDBOX ALWAYS ON
    1)  POST FOR AUTHENTICATION       (POST /system/api/v1/auth/token) 
    2)  SITE MENU                       
    3)  TOPOLOGY MENU                                
    4)  DEVICES MENU                         
    5)  CLIENTS MENU  
    6)  CONFIG TEMPLATES MENU              
    7)  COMMAND RUNNER MENU                 
    8)  NETWORK DISCOVERY MENU             
    9)  PATH TRACE MENU                    
    A)  TASK MENU                   
    B)  FILE MENU                
    C)  EVENT MENU              
    ¿Que opción deseas usar?"""

#--------------------DNAC MENUS NIVEL 3 -----------------------------
DNAC_SITE_MENU="""Estás usando SITE API
        1) GET SITE                      (GET /intent/api/v1/site)
        2) GET SITE HEALTH               (GET /intent/api/v1/site-health?timestamp="1612209600000")
        ¿Que opción deseas usar?"""

DNAC_TOPOLOGY_MENU="""Estás usando TOPOLOGY API
        1) GET FOR PHYSICAL TOPOLOGY     (GET /intent/api/v1/topology/physical-topology)
        2) GET FOR SITE TOPOLOGY         (GET /intent/api/v1/topology/site-topology)
        ¿Que opción deseas usar?"""
        
DNAC_DEVICES_MENU="""Estás usando DEVICE API
        1) GET FOR NETWORK DEVICES       (GET /intent/api/v1/network-device)
        2) GET FOR INTERFACES            (GET /intent/api/v1/interface)
        ¿Que opción deseas usar?"""

DNAC_CLIENTS_MENU="""Estás usando CLIENTS API
        1) GET CLIENTS HEALTH            (GET /intent/api/v1/client-health?timestamp="1612209600000")
        2) GET CLIENT ENRICHMENT DETAILS (GET /dna/intent/api/v1/client-enrichment-details) (se requiere una mac, pero no hay usuarios)
        3) GET ISSUES ENRICHMENT DETAILS (GET /dna/intent/api/v1/issue-enrichment-details)  (se requiere una mac, pero no hay usuarios)
        ¿Que opción deseas usar?"""

DNAC_CONFIG_TEMPLATES_MENU="""Estás usando COMMAND RUNNER API
        1) GET FOR PROJECT LIST            (GET /intent/api/v1/template-programmer/project)
        2) GET FOR TEMPLATE LIST           (GET /intent/api/v1/template-programmer/template)
        3) GET FOR TEMPLATE DETAILS        (GET /intent/api/v1/template-programmer/template/{templateId})
        4) POST FOR A NEW TEMPLATE         (POST /intent/api/v1/template-programmer/project/{projectId}/template)    (FALTA DISEÑAR EL BODY)
        5) DEPLOY FOR A TEMPLATE           (POST /intent/api/v1/template-programmer/template/deploy)                 (BAD REQUEST)
        6) GET FOR TEMPLATE DEPLOY STATUS  (GET /v1/template-programmer/template/deploy/status/deploymentId)         (FALTA EL ANTERIOR)
        ¿Que opción deseas usar?"""

DNAC_COMMAND_RUNNER_MENU="""Estás usando COMMAND RUNNER API
        1) GET FOR LEGIT READS           (GET /intent/api/v1/network-device-poller/cli/legit-reads)
        2) POST FOR COMMAND              (POST /intent/api/v1/network-device-poller/cli/read-request)
        ¿Que opción deseas usar?"""

DNAC_NETWORK_DISCOVERY_MENU="""Estás usando NETWORK DISCOVERY API
        1) GET FOR DISCOVERY COUNTS      (GET /intent/api/v1/discovery/count)
        2) GET FOR DISCOVERY LIST        (GET /intent/api/v1/discovery/1/"+str(count))
        3) GET FOR DISCOVERY SUMMARY     (GET /intent/api/v1/discovery/3206/summary NO AGREGA VALOR APARENTE)
        ¿Que opción deseas usar?"""

DNAC_PATH_TRACE_MENU="""Estás usando PATH TRACE API
        1) POST FOR PATH TRACE              (POST /intent/api/v1/flow-analysis)                   
        2) GET FOR FLOW ANALYSIS            (GET /intent/api/v1/flow-analysis)                    (ALGO PASA CON ESTE GET)     
        3) GET FOR FLOW ANALYSIS WITH ID    (GET /intent/api/v1/flow-analysis/{flowAnalysisId})
        4) DELETE FOR FLOW ANALYSIS WITH ID (DELETE /intent/api/v1/flow-analysis/{flowAnalysisId} 
        ¿Que opción deseas usar?"""

DNAC_TASK_MENU="""Estás usando TASK API
        1) GET FOR TASK LIST             (GET /intent/api/v1/task)
        2) GET FOR TASK BY ID            (GET /intent/api/v1/task/taskId)
        ¿Que opción deseas usar?"""

DNAC_FILE_MENU="""Estás usando FILE API
        1) GET FOR NAMESPACE LIST        (GET /intent/api/v1/namespace)
        2) GET FOR FILES BY NAMESPACE    (GET /intent/api/v1/namespace/nameSpace)
        3) GET FOR FILE BY FILE ID       (GET /intent/api/v1/files/fileId)
        ¿Que opción deseas usar?"""

DNAC_EVENT_MENU="""Estás usando EVENT API
        1) GET FOR EVENTS                (GET /intent/api/v1/events?tags=ASSURANCE)
        2) GET FOR EVENT SUBSCRIPTION    (GET /intent/api/v1/event/subscription)
        3) GET FOR EVENT NOTIFICATIONS   (GET /intent/api/v1/event/event-series    (NO HAY NOTIFICACIONES)
        4) POST FOR EVENT SUBSCRIPTION   (POST /intent/api/v1/event/subscription)  (NO HAY PERMISO)
        ¿Que opción deseas usar?"""