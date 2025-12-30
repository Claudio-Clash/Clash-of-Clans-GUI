import tkinter as tk
import requests

#make a list of clan members and when you press on them you get stats
auth = {'Authorization': 'Bearer AUTH KEY'}
#2JROV9Y2P


root = tk.Tk()
root.title("clan")




def show_clans():
    clansList.delete(0, tk.END)
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
    clans = [clan['name'] for clan in items]
    #for clanName in search_json['items']:
    return clans
        #return(clanName)




frame = tk.Frame(root)
frame.pack(side='left',fill='both',expand=True,padx=10,pady=10)

titleMembers = tk.Label(frame,text="Members of ...",)
titleMembers.pack()

entry = tk.Entry(frame)
entry.pack()
addButton = tk.Button(frame,text='search',command=show_clans)
addButton.pack()



clansList = tk.Listbox(frame)
clansList.pack(fill='y',side='right',expand=True)



root.mainloop()