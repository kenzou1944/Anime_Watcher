# The Front end used for user to select the website they would like to open. 
#
import tkinter as tk
# import Sele ,might use for automation.
import webbrowser
import Selenium.web_scrap as ws

root = tk.Tk()
root.title("Anime Watcher")
# root.geometry('1200x300')

# left side
chk1_state = tk.BooleanVar()
chk1_state.set(False) # set check state
chk2_state = tk.BooleanVar()
chk2_state.set(False) # set check state
chk3_state = tk.BooleanVar()
chk3_state.set(False) # set check state

Websites = {
    "https://www.crunchyroll.com":chk1_state,
    "https://www.youtube.com":chk2_state,
    "https://www.google.com":chk3_state
}

def begin():
    for key,value in Websites.items():
        if value.get() == True:
            webbrowser.open(key)

tk.Label(root,
         text="""Choose your Websites to Open""",
         justify= tk.LEFT,
         padx= 20).grid(column=0, row=0)


counter = 1
for key,value in Websites.items():
    tk.Checkbutton(root, 
                   text=key[12:], 
                   var=value,
                   indicatoron = 0,
                   width =20,
                   padx = 20).grid(column=0, row=counter)
    counter += 1
btn = tk.Button(root,text="start", command=begin).grid(column=0, row=counter)

# right side inital
def inital_right():
    def insert_list():
        counter = 1
        for key,value in list_of_animes.items():
            Lb1.insert(counter,key + '      '+value[:3]+'     '+value[4:])
            counter += 1

        
    list_of_animes = {}
    app = ws.Sele(list_of_animes)

    User_input = int(input("Enter 0 to see all ongoing animes or Enter 1 to enter an anime "))
    if User_input == 0:
        list_of_animes = app.get_all_anime()
    elif User_input == 1:
        #display
        temp_list_of_animes = [
            "Dr. Stone",
            "Sword Art Online: Alicization - War of Underworld",
            "Enn Enn no Shouboutai",
            "Boku no Hero Academia 4th Season",
            "Vinland Saga",
            "Nanatsu no Taizai: Kamigami no Gekirin",
            "Shokugeki no Souma: Shin no Sara",
            "Assassins Pride",
            "Bokutachi wa Benkyou ga Dekinai!",
            "Kono Yuusha ga Ore Tueee Kuse ni Shinchou Sugiru",
            "Fairy Gone 2nd Season",
            "Choujin Koukousei-tachi wa Isekai demo Yoyuu de Ikinuku you desu!",
            "Fate/Grand Order: Zettai Majuu Sensen Babylonia",
            "Ore wo Suki nano wa Omae dake ka yo",
            "No Guns Life",
            "Granblue Fantasy The Animation Season 2",
            "Watashi, Nouryoku wa Heikinchi de tte Itta yo ne!",
            "Radiant 2nd Season",
            "Mairimashita! Iruma-kun",
            "Hataage! Kemono Michi",
            "Babylon",
            "Kono Oto Tomare! 2nd Season",
            "Beastars",
            "Kabukichou Sherlock",
            "Ahiru no Sora",
            "Honzuki no Gekokujou: Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen",
            "High Score Girl II",
            "Chihayafuru 3",
            "Phantasy Star Online 2: Episode Oracle",
            "Keishichou Tokumu-bu Tokushu Kyouaku-han Taisaku-Shitsu Dai-Nana-ka -Tokunana-",
            "Hoshiai no Sora",
            "Rifle Is Beautiful",
            "Z/X: Code Reunion",
            "Houkago Saikoro Club",
            "Diamond no Ace: Act II",
            "Stand My Heroes: Piece of Truth",
            "Chuubyou Gekihatsu Boy",
            "Shin Chuuka Ichiban!",
            "Ani ni Tsukeru Kusuri wa Nai! 3",
            "Actors: Songs Connection",
            "Africa no Salaryman (TV)",
            "Zoids Wild Zero",
            "Bananya: Fushigi na Nakamatachi",
            "Star☆Twinkle Precure",
            "Aikatsu on Parade!",
            "Urashimasakatasen no Nichijou",
            "Go! Go! Atom",
            "Egg Car",
            "Kaiju Step Wandabada",
        ]
        for anime in temp_list_of_animes:
            print(anime)
        User_input = input("Please enter one of the name listed: ")
        list_of_animes = app.get_one_anime(User_input)


    max_len = 0
    for key,value in list_of_animes.items():
        if max_len < len(key)+len(value):
            max_len = len(key)+len(value)
    Lb1 = tk.Listbox(root,width = max_len)
    insert_list()


    Lb1.grid(column= 1, row=0, rowspan=5, padx=20, pady=10)

btn = tk.Button(root,text="Retrieve", command=inital_right).grid(column=1, row=5)
root.mainloop()