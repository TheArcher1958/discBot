import requests, re

def getStats(player):
    rget = (requests.get('https://plancke.io/hypixel/player/stats/' + player + '#SkyWars')).text
    ind = rget.index("SkyWars </a>")
    newMessage = rget[ind:ind+500]
    findNum = re.compile(r'[0-9,]')
    killsIndex = (re.compile(re.escape("<li><b>Kills:</b> ") + r'[0-9,]*')).findall(newMessage)
    lossesIndex = (re.compile(re.escape("<li><b>Deaths:</b> ") + r'[0-9,]*')).findall(newMessage)
    winsIndex = (re.compile(re.escape("<li><b>Wins:</b> ") + r'[0-9,]*')).findall(newMessage)
    assistsIndex = (re.compile(re.escape("<li><b>Assists:</b> ") + r'[0-9,]*')).findall(newMessage)
    kills = "".join(findNum.findall(killsIndex[0]))
    deaths = "".join(findNum.findall(lossesIndex[0]))
    wins = "".join(findNum.findall(winsIndex[0]))
    assists = "".join(findNum.findall(assistsIndex[0]))
    return [kills,deaths,wins,assists]

def status(player):

    rget = (requests.get('https://plancke.io/hypixel/player/stats/' + player)).text
    ind = rget.index("Lastlogin: ")
    newMessage = rget[ind:ind + 500]
    findNum = re.compile(r'[0-9,\-: EDT]')
    lastLoginIndex = (re.compile(re.escape("Lastlogin: </b>") + r'[0-9,\-: EDT]*')).findall(newMessage)
    #print(lastLoginIndex)
    lastLogin = "".join(findNum.findall(lastLoginIndex[0]))
    #print(lastLogin)
    findNum2 = re.compile(r'[A-Z]')
    ind2 = newMessage.index("Status</h4>")
    onlineIndex = newMessage[ind2+15:ind2+22]
    #print(onlineIndex)
    onlineStatus = "".join(findNum2.findall(onlineIndex))
    #print(onlineStatus)
    if onlineStatus != "O":
        onlineIndex = newMessage[ind2+55:ind2+80]
        onlineStatus = "".join(findNum2.findall(onlineIndex))
        lastOnlineStatus = "Online!\nGameType: " + onlineStatus
    else:
        lastOnlineStatus = "OFFLINE"
    #print(onlineStatus)
    return [lastLogin[2:], lastOnlineStatus]

def serverCount(ip):
    rget = (requests.get('https://mcsrvstat.us/server/' + ip)).text
    ind = rget.index("Players</td>")
    newMessage = rget[ind:ind + 80]
    ind2 = newMessage.index("Players</td>")
    onlineIndex = newMessage[ind2+15:ind2+60]
    findNum2 = re.compile(r'[0-9 ]')
    onlineStatus = "".join(findNum2.findall(onlineIndex))
    ind3 = onlineStatus.index("  ")
    final = onlineStatus[0:ind3] + " / " + onlineStatus[ind3+2:]
    return final



