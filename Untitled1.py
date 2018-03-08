
# coding: utf-8

# In[5]:


class Alumno:
    def __init__(self, universidad, promedio, intercambiok=False):
        self.universidad= universidad
        self.promedio= promedio
        self.intercambiok= intercambiok
    
    def intercambio(self, nueva_u):
        self.universidad=nueva_u
    
    
Nacho = Alumno("Cato", 45)
print(Nacho.intercambio)


# In[6]:


class Universidad:
    def __init__(self, lista, promedio_de_entrada):
        self.lista=lista
        self.promedio_de_entrada = promedio_de_entrada


Mari = Alumno("Cato", 50)
Nico = Alumno("UdeCh", 51)
Mati = Alumno("Cato", 49)
Regi = Alumo("UdeCh", 48)

UdeCh = Universidad([Nico, Regi], 47)
Cato = Universidad([Mari, Mati], 50)


        



# In[7]:


Mari.intercambio("UdeC")
print(Mari.universidad)


# In[ ]:


class Intercambio(alumno, universidad):
    

