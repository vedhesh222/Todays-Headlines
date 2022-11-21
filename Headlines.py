#Importing the Modules
import requests as rq
from art import *

#Dealing with Api Key
apiKey = 'Your API Key'

#Art Work
tprint("Today's-HeadLines")

#Me
print('[Me: M.Vedhesh Narayanan, Instagram: tek_vedhesh, GitHub: https://github.com/vedhesh222]')
print('')

#Getting the the Country
print('[Enter -h for any Help]')
print('')
c = input('Enter your country: ')

#Help
if c == '-h':
    print('')
    print('Country Input: \n- India, \n- US, \n- Australia, \n- Germany')
    
    print(' ')
    c = input('Now Enter your country: ')

    if c == 'India':
        print('')
        print(c+"'s "+'Headlines')
        print('')       
        c = 'in'      

    elif c == 'US':
        print('')
        print(c+"s "+'Headlines')
        print('')        
        c = 'us'

    elif c == 'Australia':
        print('')
        print(c+"'s "+'Headlines')
        print('')        
        c = 'au'

    elif c == 'Germany':
        print('')
        print(c+"'s "+'Headlines')
        print('')        
        c = 'de'
       
    else:
        print('Sorry :( Something went wrong!')

elif c == 'India':
    print('')
    print(c+"'s "+'Headlines')
    print('')       
    c = 'in'      

elif c == 'US':
    print('')
    print(c+"'s "+'Headlines')
    print('')        
    c = 'us'

elif c == 'Australia':
    print('')
    print(c+"s '"+'Headlines')
    print('')        
    c = 'au'

elif c == 'Germany':
    print('')
    print(c+"'s "+'Headlines')
    print('')        
    c = 'de'

else:
    print('Sorry :( Something went wrong!')

#Pulling the News
def headlines():
    pullNews = 'https://newsapi.org/v2/top-headlines?country='+ c +'&apiKey=' + apiKey
    pullingNews = rq.get(pullNews).json()
    pulledNews = pullingNews['articles']
    #print(pulledNews)
    
    #Pullign titles for articles
    titles = []
    for a in pulledNews:
        titles.append(a['title'])
        #print(titles)
    
    #Align
    for i in range(len(titles)):
        print(titles[i])

#Calling the Function
headlines()

#Closing it
print('')
close = input('Hit Enter to Exit...')