#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from bs4 import BeautifulSoup
import requests
import hashlib
import os

def save_html_to_file(content, filename):
    with open(filename, 'wb') as file:
        file.write(content)

def load_html_from_file(filename):
    with open(filename, 'rb') as file:
        return file.read()

hardwoodBeginnerUrl = "http://onlinecollegebasketball.org"
wantedYear = input("What Recruit Year (HSFR,HSSO,HSJR,HSSR,INT,JCFR,JCSO): ")
wantedRegion = input("What Region?(All,NE,MA,MW,WI): ")
#schoolYear= ["HSFR","HSSO","HSJR","HSSR"]

#url = "http://onlinecollegebasketball.org/top_prospects/1/6/700"  # Replace this URL with the one you want to scrape
'''
if wantedYear == "INT":
    url = hardwoodBeginnerUrl + "/top_prospects/6/0/700"
else:
    if wantedYear == "JCFR":
        wantedYearIndex = 11
    elif wantedYear == "JCSO":
        wantedYearIndex = 12
    else:
        wantedYearIndex = schoolYear.index(wantedYear) + 1
    url = hardwoodBeginnerUrl + "/"+ "top_prospects/" + str(wantedYearIndex) + "/6/700"
'''

schoolYear = {"HSFR": "1","HSSO": "2","HSJR": "3","HSSR": "4","INT": "6","JCFR": "11","JCSO": "12"}
playerRegion = {"All": "0","NE": "6","MA": "MA","MW": "4","WI":"WI"}
url = hardwoodBeginnerUrl + "/"+ "top_prospects/" + schoolYear[wantedYear] + "/" + playerRegion[wantedRegion] + "/700"



# Generate a unique filename from the URL using hashlib
file_name = hashlib.md5(url.encode()).hexdigest() + ".html"
folder_name = "RecruitSearchHTML"  # Corrected folder name

try:
    html_content = load_html_from_file(os.path.join(folder_name, file_name))
    #print("Content loaded from file.")
except FileNotFoundError:
    response = requests.get(url)
    html_content = response.content
    os.makedirs(folder_name, exist_ok=True)  # Create folder if it doesn't exist
    save_html_to_file(html_content, os.path.join(folder_name, file_name))
    #print("Content fetched from URL and saved to file.")


soup = BeautifulSoup(html_content, "html.parser")
infoList = soup.find_all("tr")[1:]


# In[ ]:




#allEvals = ['Recruiting Evaluation', 'Could be a good post player', '\nRecruiting Evaluation', 'Could be an above average shooter', 'Could really be a long-range shooter', 'Can never be a good rebounder', 'Can be a really smart player', 'Can be a good all-around defensive player', 'Will never be a good interior defender', 'Projected Height', '6\' 3"', '', 'Could be a good shooter', 'Can be a smart player', 'Can be a great all-around defensive player', 'Can be a really good ball handler', 'Will be very quick', 'Excellent all-around player', '6\' 7"', 'Will never be a good perimeter defender', 'Can be a skilled passer', 'Will be a below average ball handler', 'Will struggle in a fast pace offense', '6\' 5"', 'Can be a decent ball handler', 'Can be a speedy player', 'Will be quick as lightning', '5\' 10"', '6\' 2"', 'Above average post moves', 'Could be an excellent shooter', 'Can be a skilled passer with exceptional court vision', '6\' 1"', '5\' 9"', 'Will always be a poor defender', "7' ", 'Will flourish in a fast pace offense', 'Can be a monster on the boards', 'Will always be a bit sluggish', 'Good all-around player', '6\' 10"', "6' ", '6\' 8"', 'Could be a very good post player', '6\' 11"', '6\' 6"', 'Does not have much of a shooting touch', 'Can be a decent rebounder', 'Will flourish in a slower tempo offense', '6\' 4"', 'Can be prone to a lot of mental mistakes', 'Has no preference to play close to home', 'Will struggle in a slower tempo offense', '5\' 8"', '6\' 9"', '5\' 11"', 'Could be a dominating post player', '5\' 5"', 'Would prefer to play close to home', '5\' 6"']

heights = ["5'5", "5'6", "5'7", "5'8", "5'9", "5'10", "5'11", "6'", "6'1", "6'2", "6'3", "6'4", "6'5", "6'6", "6'7", "6'8", "6'9", "6'10", "6'11", "7'", "7'1", "7'2", "7'3", "7'4", "7'5"]

InsideShooting = {"Good":{"Above average post moves",
"Could be a good post player",
"Could be a very good post player",
"Could be a dominating post player"},"Bad": ""}
OutsideShooting = {"Good":{"Could be an above average shooter","Could be a good shooter","Could be an excellent shooter"},"Bad":{"Does not have much of a shooting touch"}}
Range = {"Good":{"Could really be a long-range shooter"},"Bad":{}}
Rebounding = {"Good":{"Can be a decent rebounder","Can be a monster on the boards"},"Bad":{"Can never be a good rebounder"}}
InsideDefense = {"Good":{},"Bad":{"Will never be a good interior defender","poor defender"}}
PerimeterDefense = {"Good":{},"Bad":{"Will never be a good perimeter defender","poor defender"}}
IQ = {"Good":{"Can be a smart player","Can be a really smart player"},"Bad":{"Can be prone to a lot of mental mistakes",}}
Passing = {"Good":{"Can be a skilled passer","Can be a skilled passer with exceptional court vision"},"Bad":{}}
Handling = {"Good":{"Can be a decent ball handler","Can be a really good ball handler"},"Bad":{"Will be a below average ball handler"}}
Speed = {"Good":{"Can be a speedy player","Will be very quick","Will be quick as lightning"},"Bad":{"Will always be a bit sluggish"}}
#Pace = {"Good":{"Will flourish in a slower tempo offense","Will flourish in a fast pace offense"},"Bad":{"Will struggle in a slower tempo offense","Will struggle in a fast pace offense"}}

recruited = input("Is Recruited?: (Y,N)") # gets if player is recruited or not

preferenceArr= [int(input("Minimum Potential: ")), int(input("Minimum SI: ")), input("Minimum Height (ex: 6'3 or 6'): "),
input("InsideShooting: "), input("OutsideShooting: "), input("Range: "), input("Rebounding: "), 
input("InsideDefense: "), input("PerimeterDefense: "),input("IQ: "),input("Passing: "),
input("Handling: "),input("Speed: ")]




#Finds the links of every player with atleast minPot and minSI

if recruited == "Y":
    playerLinks = [
        hardwoodBeginnerUrl + infoList[i].find_all("td")[2].find("a").get("href")
        for i in range(len(infoList))
        if (int(infoList[i].find_all("td")[7].text) >= preferenceArr[0]) and (int(infoList[i].find_all("td")[6].text) >= preferenceArr[1])
    ]
    #print("0")
else:
    playerLinks = [
        hardwoodBeginnerUrl + infoList[i].find_all("td")[2].find("a").get("href")
        for i in range(len(infoList))
        if (int(infoList[i].find_all("td")[7].text) >= preferenceArr[0]) and (int(infoList[i].find_all("td")[6].text) >= preferenceArr[1]) and (infoList[i].find_all("td")[11].text == "none")
    ]
    #print("1")


preference_keys = ["", "", "InsideShooting", "OutsideShooting", "Range", "Rebounding", "InsideDefense", "PerimeterDefense", "IQ", "Passing", "Handling", "Speed"]



resultDic = {}

for i in range(3, len(preferenceArr)):
    user_input = preferenceArr[i]
    preference_key = preference_keys[i - 1]  # Adjust index to match preference_keys

    if preference_key and preference_key in globals() and preference_key != "":  # Exclude empty keys
        corresponding_dict = globals()[preference_key]
        if user_input == 'Y':
            resultDic.setdefault(preference_key, set()).update(("Good", item) for item in corresponding_dict["Good"])
        elif user_input == 'N':
            resultDic.setdefault(preference_key, set()).update(("Bad", item) for item in corresponding_dict["Bad"])




            





# 

# In[ ]:


#Searches and returns links of players who fit preferences
for player in playerLinks:
    file_name = hashlib.md5(player.encode()).hexdigest() + ".html"

    
    folder_name = "PlayersHTML"  # Corrected folder name

    try:
        html_content = load_html_from_file(os.path.join(folder_name, file_name))
        #print("Content loaded from file.")
    except FileNotFoundError:
        response = requests.get(player)
        html_content = response.content
        os.makedirs(folder_name, exist_ok=True)  # Create folder if it doesn't exist
        save_html_to_file(html_content, os.path.join(folder_name, file_name))
        #print("Content fetched from URL and saved to file.")

    
    soup2 = BeautifulSoup(html_content, "html.parser")

    #Finds the recuriting Eval
    try:
        recEval = soup2.find("table").find_all("tr")[15].text
    except AttributeError:
        continue

    playerEvalheight = ""
    for i in recEval:
        if i.isdigit():
            if len(playerEvalheight) == 0:
                playerEvalheight += i
                playerEvalheight += "'"
            else:
                playerEvalheight += i


    if heights.index(playerEvalheight) >= heights.index(preferenceArr[2]):
        for key, values in resultDic.items():
            good_values = [value for qualifier, value in values if qualifier == "Good"]
            bad_values =  [value for qualifier, value in values if qualifier == "Bad"]
            if not any(good_value in recEval for good_value in good_values) and good_values != []:
                break
            elif any(bad_value in recEval for bad_value in bad_values):
                break
        else:
            print(player)





    
    #for pref in preferenceArr[3:]:

    
    #print(player)
    


        

