import matplotlib.pyplot as mp
from read_csv import read_csv
import re
def generate_bar_chart(labels_pam, values):
  labels = [a for x in labels_pam for a in x]
  print(labels)
  print(values)
  
  #values = [x[f'{labels[0]} Population'] for x in values if x[f'{labels[0]} Population']]
  fig , ax = mp.subplots()
  ax.bar(labels, values)
  mp.show()

def filter_data_by_country(country, data_to_filter):
 labels = []
 values = []
 data_list_dict = read_csv()
 a= {1,2}
 b= {2,3}
 #print(a - b)
 country_filter = list(filter(lambda count: count['Country'] in country, data_list_dict))

 #print(country_filter)
 for x in country_filter:
     for key in x:
        match = (re.findall(r'\d{4,4}', key))
        if match != []:
            labels.append(match)

 year = [a for x in labels for a in x]
 index = 0
 for x in country_filter:
    for a in range(0,8):
      values.append(int(x[f'{year[index]} Population'])) 
      index += 1                     
 return labels, values   
 #print(population_countries_2020)
 #return population_countries_2020

if __name__ == '__main__':
 datos_filtrado=filter_data_by_country(['Venezuela'], 'Population')
 generate_bar_chart(datos_filtrado[0], datos_filtrado[1])
