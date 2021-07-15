# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 13:32:15 2020

@author: mvidal2
"""
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support.ui import Select
import pandas as pd
from selenium.common.exceptions import TimeoutException

root = tk.Tk()
root.title("Yo-Robot")
root.geometry("840x800")
b = tk.StringVar()
a = tk.IntVar()
X= tk.StringVar()
db1=tk.StringVar()
Y=tk.StringVar()
db3=tk.Listbox()
#num_via = tk.IntVar(value=1)
num_via = tk.StringVar()
tipo = tk.StringVar()
clase = tk.StringVar(value='Catálogo')

##############################################################################

def mfileopen():
    file1 = filedialog.askopenfile()
    #label16=tk.Label(text=file1).pack()
    file2=file1.name
    f=open(file2)
    label17=tk.Label(text=f.read()).pack()

def mquit():
    mess = messagebox.askyesno(title='quit', message='are you sure to quit') #Para cerrar la ventana
    if mess==1:
        root.destroy()   

def cargar_archivo():
    db1=pd.read_excel('Revision2.xlsx') #debe de estar en la misma carpeta
    X=db1['RUT']
    Observaciones = []
    #db2=db1['RUT'].unique()
    #db3=db2.tolist()

##############################################################################
    
def procesar():
    driver = webdriver.Firefox()
    driver.get("http://www.google.com/")

    #open tab
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 

    # Load a page 
    driver.get('https://leifs.mycmsc.com/psp/leifsprd/EMPLOYEE/ERP/?cmd=logout')

    username = driver.find_element_by_id("userid") #input id o name
    password = driver.find_element_by_id("pwd") #input id o name

    username.send_keys("311800219")
    password.send_keys("Sepulveda8323/")

    driver.find_element_by_name("Submit").click() #name
###############################################################################

    #Comienzo del ciclo
    #Main Menu
    driver.find_element_by_id("pthnavbca_PORTAL_ROOT_OBJECT").click() #ID

    #Vendors
    driver.find_element_by_id("fldra_EPCO_VENDORS").click() #ID

    #Vendor Information
    #driver.find_element_by_id("fldra_EPCO_REQUISITIONS").click() #ID
    driver.implicitly_wait(2)
    driver.find_element_by_id("fldra_EPAP_VENDORS").click() #CSS Selector

    #Vendor Information
    #driver.find_element_by_id("fldra_EPCO_REQUISITIONS").click() #ID
    driver.implicitly_wait(2)
    driver.find_element_by_css_selector("#fldra_EPAP_VENDOR_APPROVE").click() #CSS Selector

    #Vendor Information
    #driver.find_element_by_id("fldra_EPCO_REQUISITIONS").click() #ID
    driver.implicitly_wait(2)
    driver.find_element_by_css_selector("#crefli_EP_APPROVE_VENDOR_GBL > a:nth-child(1)").click() #CSS Selector
                                    
###############################################################################

    #for w in ["61607600-0","61607800-3","61608200-0"]:
    for n in range (len(db1['RUT'])):
        w=str(Y[n]) #RUT
        driver.switch_to.frame("ptifrmtgtframe")
    
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, "VNDR_UNCERT_VW_SETID"))).clear()
        #driver.find_element_by_id("VNDR_UNCERT_VW_SETID").click()
        #driver.implicitly_wait(1)
        #driver.find_element_by_id("VNDR_UNCERT_VW_SETID").clear()
        driver.implicitly_wait(1)
        driver.find_element_by_id("VNDR_UNCERT_VW_SETID").send_keys("CHL00")

        driver.find_element_by_id("VNDR_UNCERT_VW_SETID").click()
        driver.implicitly_wait(1)
        driver.find_element_by_id("VNDR_UNCERT_VW_VENDOR_ID").clear()
        driver.implicitly_wait(1)
        driver.find_element_by_id("VNDR_UNCERT_VW_VENDOR_ID").send_keys(w)
        driver.implicitly_wait(1)
        driver.find_element_by_id("#ICSearch").click()
        #"No matching values were found."
        repetido=(By.CLASS_NAME, "PSSRCHINSTRUCTIONS")
        try: 
            WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element((repetido),"No matching values were found."))
            print("valor repetido " + "RUT " + w)
            break
        except TimeoutException:
            #continue
###############################################################################
            #if driver.find_element_by_class_name("PSSRCHINSTRUCTIONS").text == "No matching values were found.":
            #print("valor repetido " + "RUT " + w)
            #break
            #else:
            #continue
       
     
            #WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "AP_WF_WRK_PB_APPROVE$39$"))).click()
    
    
###############################################################################
            #Segunda pantalla    
            #driver.switch_to.default_content()
            #time.sleep(3)
            #driver.switch_to.frame("ptifrmtgtframe")
    
            WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, "AP_WF_WRK_PB_APPROVE$39$"))).click()
        
            driver.switch_to.default_content()
            WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#pthnavbccref_EP_APPROVE_VENDOR_GBL > a:nth-child(1)"))).click()#CSS Selector

            b=print("Trabajo terminado " + "RUT " + w)
            

"""
href=driver.find_element_by_xpath('/html/body/map/area').get_attribute('href')
driver.get(href)
https://stackoverflow.com/questions/30324760/how-to-get-attribute-of-element-from-selenium
https://www.w3schools.com/tags/ref_attributes.asp
"""

##############################################################################
#Gadgets Tkinter

button2 = tk.Button(root,text='Open File',font=('arial',10,'bold'), command=mfileopen)
button2.place(x=100,y=20)

button3 = tk.Button(root,text='Salir',command= root.destroy,font=('arial',10,'bold')) #Fg = letter, bg = Fondo
button3.place(x=100,y=50)

button4 = tk.Button(root,text='Procesar',font=('arial',10,'bold'), command=procesar)
button4.place(x=100,y=80)

T = tk.Text(root, height=200, width=150)
T.place(x=300,y=20)
#T.pack()
T.insert(tk.END, b)

#Ingreso de texto
text1= tk.Entry(root,textvariable= b)
text1.place(x=100,y=120,width=150, height=200)

root.mainloop()
