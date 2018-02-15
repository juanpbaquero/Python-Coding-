import pandas as pd
import os
from selenium import webdriver
import time 

os.chdir(r'E:\jp')

main={}    # diccionario principal donde se guardaran todas las observaciones . 

j=0
t = time.time()


browser = webdriver.Firefox(executable_path=r"E:\jp\geckodriver.exe")
url = 'http://carros.tucarro.com.co/carros-camionetas/_Desde_6433'    # la estrategia va a ser obtener todos los carros y hacer scrapping uno por uno 
browser.get(url) 

for ii in range(1,100000) :     #loop pensando en cada pagina 
  
    time.sleep(15)
    linkElem = browser.find_elements_by_css_selector('h2')  # la categoria h2 contiene cada carro 
    
    
    
    for cars in range(0,len(linkElem)): # outerloop in page 
        linkElem = browser.find_elements_by_css_selector('h2')  # la categoria h2 contiene cada carro 
        
        try :    
    
            linkElem[cars].click()    # click al carro  1 
            
            
            ## este try except es por si se demoro mucho en cargar la pagina 
            
            try :
                subdic={}  #  aca las caracteristicas de cada carro 
                time.sleep(5)
                browser.refresh() 
                time.sleep(5)
                linkElemI = browser.find_elements_by_css_selector('div div div dl')   # caracteristicas de la tabla mas grande 
            
            
                for caract in range(0,len(linkElemI)):
                    str1=linkElemI[caract].text.split(':\n')
                    str1=linkElemI[caract].text.split(':\n')
                    subdic[str1[0]]=str1[1]
                
            
            ## hasta aca estan los elementos de la tabla grande 
            
            
            ## aca obtenemos precio 
                linkElemII = browser.find_elements_by_css_selector('article strong') 
                subdic['Precio']= (linkElemII)[0].text
            
            ## aca obtenemos locacion 
            
                linkElemIII = browser.find_elements_by_css_selector('article dl dd') 
                subdic['Lugar']= linkElemIII[2].text
                ##browser.back()
                browser.execute_script("window.history.go(-1)")   # better than browser back 
                time.sleep(8) # seconds
                
                
                
                
                main[str(ii)+'-'+str(cars)]=subdic
                
            except: 
                subdic={}  #  aca las caracteristicas de cada carro 
                time.sleep(15)
                browser.refresh() 
                time.sleep(5)
                linkElemI = browser.find_elements_by_css_selector('div div div dl')   # caracteristicas de la tabla mas grande 
            
            
                for caract in range(0,len(linkElemI)):
                    str1=linkElemI[caract].text.split(':\n')
                    str1=linkElemI[caract].text.split(':\n')
                    subdic[str1[0]]=str1[1]
                
            
            ## hasta aca estan los elementos de la tabla grande 
            
            
            ## aca obtenemos precio 
                linkElemII = browser.find_elements_by_css_selector('article strong') 
                subdic['Precio']= (linkElemII)[0].text
            
            ## aca obtenemos locacion 
            
                linkElemIII = browser.find_elements_by_css_selector('article dl dd') 
                subdic['Lugar']= linkElemIII[2].text
                browser.execute_script("window.history.go(-1)") 
                time.sleep(8)
                main[str(ii)+'-'+str(cars)]=subdic
                     
        except:
            continue
    try: 
        siguiente = browser.find_element_by_partial_link_text('Siguien') 
    except: 
        continue 
    try:
        siguiente.click()
    except:
        break            # es decir que se termine el scrapping cuando no hayan mas paginas
    if ii%10==0:      # cada 10 paginas guarde lo que va porque esto se  esta dañando 
        string='outputC'+str(j)+'.xlsx'
        df=pd.DataFrame.from_dict(main, orient='columns', dtype=None).transpose()
        writer = pd.ExcelWriter(string)
        df.to_excel(writer,'Sheet1')
        writer.save()
        j=j+1
        main={}
        
    

elapsed = time.time() - t    


