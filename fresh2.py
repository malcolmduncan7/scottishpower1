from cmath import rect
import fitz
import pandas as pd 
import os
import re



def make_text(words):#<-- possibly sourse of problem
    line_dict = {} 
    words.sort(key=lambda w: w[0])
    for w in words:  
        y1 = round(w[3], 1)  
        word = w[4] 
        line = line_dict.get(y1, [])  
        line.append(word)  
        line_dict[y1] = line  
    lines = list(line_dict.items())
    lines.sort()  
    return "j".join([" ".join(line[1]) for line in lines])



#changes working directory
os.chdir(r'C:/Users/malco/Desktop/bill') 
#to access a supported document
doc = fitz.open('bill-691004013000.pdf') 
#a Page must be created
page = doc[0]
#extracting text from document 
words = page.get_text("blocks") 

#all pages of the pdf appeneded to all_blocks and all_blocks text for each page
all_blocks = []
for pageno in range(0,len(doc)-1): 
    page = doc[pageno] #<-- goes through  all pages
    words = page.get_text("blocks") #<-- gets blocks of text with rectangle coordinates 
    rec = page.rect #<-- rect is a tuple of 4 numbers to get coordinates for the blocks
    mywords = [w for w in words if fitz.Rect(w[:4]) in rec] #<-- my_words is words in rectangle from rec
    blk = make_text(mywords) #<-- calls function to make_text possibly sourse of problem
    all_blocks.append(blk) #<-- appends blk to all_blocks list

#splitting the list of all_annots after j set out in function make_text
cont=[]
for i in range(0,len(all_blocks)):
    cont.append(all_blocks[i].split('j')) #splits the list of all_blocks after j set out in function make_text the orginal code was cont.append(all_blocks[i].split('j',1)) but did not work, the 1 represents the number of splits to be made which would be one split per block after j 
    
#liss filter unwanted text --- this part is fine 
liss = [] #<-- replaces unwanted character and appends to list
for i in range(0,len(cont)): 
    lis=[]
    for j in cont[i]:
        j=j.replace('.','')
        j=j.replace('#','')
        j=j.replace('*','')
        j=j.replace(':','')
        j=j.strip()
        #print(j)
        lis.append(j)
    liss.append(lis)
    
#this part doesnt work because splitting the text is wrong due to the function make_text I think  
keys=[]
values=[]
for i in liss:
    keys.append(i[0])
    values.append(i[1])
for i in range(0, len(values)):
    for j in range(0,len(values[i])):
        if values[i][j]>='A' and values[i][j]<='Z':
            break            
    if j==len(values[i])-1:
       values[i]=values[i].replace(' ','')   

report=dict(zip(keys,values))



       
#print(rec)
#print(cont) 
print(liss[4][18])   
#print(keys)
#print(values[6][10])
#print(report) 
#print(value)  
#print(all_blocks[4][16])


      





#creating a dataframe 
#df = pd.DataFrame(words) 
#df = pd.Series(words) 
#create list of column 4 that contain the word 'units' from df
"""
units = df[4][df[4].str.contains('units')]
starting_balance = df[4][df[4].str.contains('starting balance')]
meter_no = df[4][df[4].str.contains('Meter number')]
standing_charge = df[4][df[4].str.contains('standing charge')]
month = df[4][df[4].str.contains('Mar')]
read = df[4][df[4].str.contains('read')]
gas  = df[4][df[4].str.contains('Gas units')]
elec = df[4][df[4].str.contains('Electricity units')]

#  remove '\n*' from gas and elec 
gas = gas.str.replace('\n*', '')
"""
#


#elec = elec.str.replace('\n*', '')

#what is wildcard for string matching?   

#how to filter results to get rid of certain text?
#should i put results into new dataframe and then filter?
#how to loop through pages in pdf and extract blocks?

#print(df[35])




#----dataframe methods----
#convert list to a dataframe
#df = pd.DataFrame(words)
#get text from dataframe 17th row and column 4th to last column
#text = df.iloc[22,4:].values.tolist()
#search dataframe for a specific word and return the [4]th column
#df[df[0] == 'read'].iloc[:,5]
#print(text)




