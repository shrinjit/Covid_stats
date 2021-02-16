from django.shortcuts import render
import requests
import json 
from pprint import pprint
## importing the REQUESTs module and the API secret key of my account to get the updates 

import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "4eb873a0cbmsh94eca0b32127851p1cb58ejsn90f738844398",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

# print(response.text)   ## to check the text 






def helloworld(request):
    total_number_of_results=0
    total_number_of_results=int(response['results'])
    list_of_data=[]
    


    if request.method=="POST":
        selectedcountry=request.POST['selectedcountry']
        print(selectedcountry)       
        for currentresult in range(0,total_number_of_results):
            if selectedcountry==response['response'][currentresult]['country']:
                new=response['response'][currentresult]['cases']['new']
                active=response['response'][currentresult]['cases']['active']
                critical=response['response'][currentresult]['cases']['critical']
                recovered=response['response'][currentresult]['cases']['recovered']
                total=response['response'][currentresult]['cases']['total']
                death=int(total)-int(active)-int(recovered)

        context={'selectedcountry':selectedcountry,'new':new,'active':active,'critical':critical,'recovered':recovered,'total':total,'death':death}
        return render(request,'covid.html',context)



    for currentresult in range(0,total_number_of_results):
         list_of_data.append(response['response'][currentresult]['country'])

    context={'list_of_data':list_of_data}
   
    return render(request,'covid.html',context)