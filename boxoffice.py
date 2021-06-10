import requests
from requests.api import head
from requests_html import HTML
import pandas as pd

url="https://www.boxofficemojo.com/year/world/"

def url_to_file(url ,filename='world.html'):
    r=requests.get(url)
    if r.status_code==200:
        html_text=r.text
        with open(filename , 'w') as f:
            f.write(html_text)
        return html_text
    return ""        
html_text=url_to_file(url)    
r_html=HTML(html=html_text)
table_class=".imdb-scroll-table"

r_table=r_html.find(table_class)

table_data=[]
header_name=[]

if len(r_table) ==1:

    #print(r_table[0].text)
    parsed_table=r_table[0]
    rows=parsed_table.find("tr")
    header_rows=rows[0]
    
    
    header_name.append(header_rows.text.split('\n'))
   # header_name=[x.text for x in header_rows]
    
    for row in rows[1:]:
        #print(row.text)
        cols=row.find("td")
        row_data=[]
        for i ,col in enumerate(cols):
           # print(i , x.text ,'\n\n')
           row_data.append(col.text)
    #print(r_table)
        table_data.append(row_data)

print(header_name)
print(table_data)        
df=pd.DataFrame(table_data , columns=header_name)
df.to_csv("boxoffice.csv" , index=False)
