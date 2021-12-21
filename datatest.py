
import json
import pandas as pd


df = pd.read_csv ('C:\\Users\\anton\\OneDrive\\Skrivbord\\human-computer-interaction\\final_project\\HCI-2021-22_ProjectData\\2-All-Data\\PostQuestionnaire.csv', delimiter=';')
#print(df.columns)
#print (df['How mentally demanding was the task?'])
#print(df.iloc[0,2])

txt = pd.read_csv ('C:\\Users\\anton\\OneDrive\\Skrivbord\\human-computer-interaction\\final_project\\HCI-2021-22_ProjectData\\2-All-Data\\P4\\EgoVehicle_Data_ID4_17_11_21_10_19_04.txt', delimiter=',')

#print(txt.columns)
#print(txt)


f = open('C:\\Users\\anton\\OneDrive\\Skrivbord\\human-computer-interaction\\final_project\\HCI-2021-22_ProjectData\\2-All-Data\\P4\\Annotation_P4a_merged.json')
data = json.load(f)

print(type(data))
print(type(data['annotations']))
for i in data['annotations']:
    #print(i['class'])
    if (i['class'] == 'Attention_on'):
        for j in i['instances']:
            #print(j['holds'])
            if (j['holds'] == 'Obj_Property'):
                print(j)




#jso = pd.read_json('C:\\Users\\anton\\OneDrive\\Skrivbord\\human-computer-interaction\\final_project\\HCI-2021-22_ProjectData\\2-All-Data\\P4\\Annotation_P4a_merged.json')

#print(jso['annotations'])