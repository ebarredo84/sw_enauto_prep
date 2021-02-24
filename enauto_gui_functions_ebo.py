#------USER INTERFACE (VIEW)----------
import tkinter as tk

#------CONTROLLER--------------------
import json
import base64

def PRINT_STATUS_CODE(response,text_box):
    #IMPRIMO EN EL TEXT BOX
    text_box.config(state="normal")                 #habilito la escritura
    text_box.delete("1.0", tk.END)                  #para borrar el texto
    text_box.insert("1.0","Request status: "+str(response.status_code)+"\n")
    text_box.config(state="disabled")               #solo lectura

def PRINT_HEADERS(headers,text_box):
    text_box.config(state="normal")                 #habilito la escritura
    text_box.delete("1.0", tk.END)                  #para borrar el texto
    text_box.insert("1.0","Headers: "+str(headers)+"\n")
    text_box.config(state="disabled")               #solo lectura

def PRINT_RESPONSE_JSON(resp,text_box):
    response_json = resp.json()                                     
    json_formatted_str = json.dumps(response_json, indent=4)
    #print(json_formatted_str)
    #IMPRIMO EN EL TEXT BOX
    text_box.config(state="normal")                 #habilito la escritura
    text_box.insert(tk.END,json_formatted_str+"\n")
    text_box.config(state="disabled")               #solo lectura

def PRINT_RESPONSE(resp,text_box):
    json_formatted_str = json.dumps(resp, indent=4)
    #print(json_formatted_str)
    #IMPRIMO EN EL TEXT BOX
    text_box.config(state="normal")                 #habilito la escritura
    text_box.insert(tk.END,json_formatted_str+"\n")
    text_box.config(state="disabled")               #solo lectura

def PRINT_CONTENT_JSON(resp,text_box):
    json_formatted_str=json.dumps(json.loads(resp.content),indent=4)
    #IMPRIMO EN EL TEXT BOX
    text_box.config(state="normal")                 #habilito la escritura
    text_box.insert(tk.END,json_formatted_str+"\n")
    text_box.config(state="disabled")               #solo lectura

def PRINT_TABLE_IN_TEXT(text_box,dictionary,**kwargs):
    num_arg=len(kwargs)

    text_box.config(state="normal")
    #----------IMPRIME 2 KEY PAIRS VALUES
    if num_arg==6:
        print_header='{0:'+kwargs['size1']+'s}{1:1}{2:'+kwargs['size2']+'s}'
        text_box.insert(tk.END,print_header.format(kwargs['name1'], "|", 
                                                    kwargs['name2'])+"\n")
        text_box.insert(tk.END,'-'*140+"\n")
        d1=kwargs['data1']
        d2=kwargs['data2']
        for ITEM in dictionary:
            text_box.insert(tk.END,print_header.format(str(ITEM[d1]),"|", 
                                                        str(ITEM[d2]))+"\n")
    #----------IMPRIME 3 KEY PAIRS VALUES---------------
    elif num_arg==9:
        print_header='{0:'+kwargs['size1']+'s}{1:1}{2:'+kwargs['size2']+'s}{3:1}{4:'+kwargs['size3']+'s}'
        text_box.insert(tk.END,print_header.format(kwargs['name1'], "|",
                                                    kwargs['name2'], "|", 
                                                    kwargs['name3'])+"\n")
        text_box.insert(tk.END,'-'*140+"\n")
        d1=kwargs['data1']
        d2=kwargs['data2']
        d3=kwargs['data3']
        for ITEM in dictionary:
            text_box.insert(tk.END,print_header.format(str(ITEM[d1]),"|", 
                                                        str(ITEM[d2]), "|", 
                                                        str(ITEM[d3]))+"\n")
    #----------IMPRIME 4 KEY PAIRS VALUES---------------
    elif num_arg==12:
        print_header='{0:'+kwargs['size1']+'s}{1:1}{2:'+kwargs['size2']+'s}{3:1}{4:'+kwargs['size3']+'s}{5:1}{6:'+kwargs['size4']+'s}'
        text_box.insert(tk.END,print_header.format(kwargs['name1'], "|",
                                                    kwargs['name2'], "|",
                                                    kwargs['name3'], "|", 
                                                    kwargs['name4'])+"\n")
        text_box.insert(tk.END,'-'*140+"\n")
        d1=kwargs['data1']
        d2=kwargs['data2']
        d3=kwargs['data3']
        d4=kwargs['data4']
        for ITEM in dictionary:
            text_box.insert(tk.END,print_header.format(str(ITEM[d1]),"|", 
                                                        str(ITEM[d2]), "|",
                                                        str(ITEM[d3]), "|",
                                                        str(ITEM[d4]))+"\n")
    #----------IMPRIME 5 KEY PAIRS VALUES---------------
    elif num_arg==15:
        print_header='{0:'+kwargs['size1']+'s}{1:1}{2:'+kwargs['size2']+'s}{3:1}{4:'+kwargs['size3']+'s}{5:1}{6:'+kwargs['size4']+'s}{7:1}{8:'+kwargs['size5']+'s}'
        text_box.insert(tk.END,print_header.format(kwargs['name1'], "|",
                                                    kwargs['name2'], "|",
                                                    kwargs['name3'], "|",
                                                    kwargs['name4'], "|", 
                                                    kwargs['name5'])+"\n")
        text_box.insert(tk.END,'-'*140+"\n")
        d1=kwargs['data1']
        d2=kwargs['data2']
        d3=kwargs['data3']
        d4=kwargs['data4']
        d5=kwargs['data5']
        for ITEM in dictionary:
            text_box.insert(tk.END,print_header.format(str(ITEM[d1]),"|", 
                                                        str(ITEM[d2]), "|",
                                                        str(ITEM[d3]), "|",
                                                        str(ITEM[d4]), "|", 
                                                        str(ITEM[d5]))+"\n")    
    #----------IMPRIME 6 KEY PAIRS VALUES---------------
    elif num_arg==18:
        print_header='{0:'+kwargs['size1']+'s}{1:1}{2:'+kwargs['size2']+'s}{3:1}{4:'+kwargs['size3']+'s}{5:1}{6:'+kwargs['size4']+'s}{7:1}{8:'+kwargs['size5']+'s}{9:1}{10:'+kwargs['size6']+'s}'
        text_box.insert(tk.END,print_header.format(kwargs['name1'], "|",
                                                    kwargs['name2'], "|",
                                                    kwargs['name3'], "|",
                                                    kwargs['name4'], "|",
                                                    kwargs['name5'], "|", 
                                                    kwargs['name6'])+"\n")
        text_box.insert(tk.END,'-'*140+"\n")
        d1=kwargs['data1']
        d2=kwargs['data2']
        d3=kwargs['data3']
        d4=kwargs['data4']
        d5=kwargs['data5']
        d6=kwargs['data6']
        for ITEM in dictionary:
            text_box.insert(tk.END,print_header.format(str(ITEM[d1]),"|", 
                                                        str(ITEM[d2]), "|",
                                                        str(ITEM[d3]), "|",
                                                        str(ITEM[d4]), "|",
                                                        str(ITEM[d5]), "|", 
                                                        str(ITEM[d6]))+"\n")
    text_box.config(state="disabled")