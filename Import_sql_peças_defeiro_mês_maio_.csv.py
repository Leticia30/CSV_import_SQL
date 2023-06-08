#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import pyodbc
conexao = pyodbc.connect("Driver={SQL Server};" + "Server=DESKTOP-LA;" + "Database=PEÇAS_DEFEITO;" + "Trusted_connection=yes")


# In[19]:


df_peçasdefeito = pd.read_csv('peças_defeito_mês_maio_.csv')
display(df_peçasdefeito)


# In[20]:


df_peçasdefeito = df_peçasdefeito.dropna(how= 'all', axis= 0)
display (df_peçasdefeito)


# In[22]:


df_peçasdefeito = df_peçasdefeito.drop('informação_aleatória', axis= 1)
display (df_peçasdefeito)


# In[27]:


print(df_peçasdefeito.dtypes)
print(type(df_peçasdefeito))


# In[ ]:


cursor = conexao.cursor()
for index,row in df_peçasdefeito.iterrows():
    display(df_peçasdefeito)
    sql = "INSERT INTO TB_PEÇAS_DEFEITO_MAIO (NOME_PEÇA, MODELO_PEÇA, FUNÇÃO_PEÇA, DEFEITO_PEÇA) VALUES (?, ?, ?, ?)"
    val = (str(row['nome_peça']), str(row['modelo_peça']), str(row['função_peça']),str(row['função_peça']))
    cursor.execute(sql, val)
    conexao.commit()
cursor.close()

