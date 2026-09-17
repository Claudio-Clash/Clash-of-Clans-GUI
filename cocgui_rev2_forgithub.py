import tkinter as tk
import requests

#make a list of clan members and when you press on them you get stats
auth = {'Authorization': 'Bearer  AUTH KEY'}
#2JROV9Y2P


root = tk.Tk()
root.title("clan")

clansTags = []



    

def show_clans():
    clansList.delete(0, tk.END)
    #import clan NAMES on the LEFT LISTBOX
    for clans in clan_search():
        clansList.insert(tk.END, clans)

        

def clan_search():
    clanTag = 'https://api.clashofclans.com/v1/clans?name=' + entry.get()
    term = "#"
    raw_input = entry.get()
    clean_entry = raw_input.replace('#', '')
    if term in entry.get():
        clanTag = 'https://api.clashofclans.com/v1/clans?name=%23' + clean_entry
        
    response = requests.get(clanTag,auth)
    search_json = response.json()
    items = search_json.get('items', []) 
    clans = [f"{clan['name']} - {clan['tag']}" for clan in items]
    global clansTags
    clansTags = [clan['tag'] for clan in items]
    #for clanName in search_json['items']:
    return clans
        #return(clanName)




def clan_members():
    cursorData = clansList.curselection()
    if cursorData:
        index = cursorData[0]
        tag = clansTags[index]
        clean_tag = tag.replace('#', '')
        retrieveMembers = 'https://api.clashofclans.com/v1/clans/%23'+clean_tag+'/members'
        response = requests.get(retrieveMembers,auth)
        search_json = response.json()
        items = search_json.get('items', []) 
        members = [f"{member['name']} - {member['tag']}" for member in items]
        return members


def clan_window():
    members = clan_members()
    clanDataWindow = tk.Toplevel(frame)

    memberList=tk.Listbox(clanDataWindow)
    memberList.pack(fill='both',expand=True)

    for member in members:
        memberList.insert(tk.END,member)



frame = tk.Frame(root)
frame.pack(fill='both',expand=True,padx=10,pady=10)

titleMembers = tk.Label(frame,text="Members of ...",)
titleMembers.pack()

entry = tk.Entry(frame)
entry.pack()

addButton = tk.Button(frame,text='search',command=show_clans)
addButton.pack()

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT,fill='y')

clansList = tk.Listbox(frame,yscrollcommand=scrollbar.set)
clansList.pack(fill='both',side='left',expand=True)

scrollbar.config(command=clansList.yview)


clanDataButton = tk.Button(frame,text='open clan data',command=clan_window)
clanDataButton.pack()






root.mainloop()