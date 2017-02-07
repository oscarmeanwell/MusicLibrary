from tkinter import *
import os, pyglet
root = Tk()

class LoadWindowOne():
    def __init__(self, parent):
        self.parent = parent
        self.parent.title('Oscars Music Player')
        self.parent.grid()
        self.parent.geometry("1100x700")
        self.parent.configure(background="steel blue")
        self.AddFrames()
        self.AddLstBoxes()
        self.AddButtons()
        self.AddScrollBar()
        self.AddArtistLst()
        self.player = pyglet.media.Player()
        
    def AddFrames(self):
        """Add The Two Frames"""
        self.LstBoxFrm = Frame(self.parent, width="4000", height="4000", bg="steel blue" )
        self.ButtonsFrm = Frame(self.parent, bg = "steel blue")
        self.LstBoxFrm.grid(row = 1, column = 0)
        self.ButtonsFrm.grid(row = 0, column = 0)

    def AddLstBoxes(self):
        """Add And Bind Listboxes"""
        self.ArtistLstBox = Listbox(self.LstBoxFrm, height = 38, width = 35, selectmode = SINGLE, bd = 4)
        self.AlbumLstBox = Listbox(self.LstBoxFrm, height = 38, width = 35, selectmode = SINGLE, bd = 4)
        self.SongLstBox = Listbox(self.LstBoxFrm, height = 38, width = 80, selectmode = SINGLE, bd = 4)
        self.ArtistLstBox.grid(row = 0, column = 1, padx = 20, pady = 20)
        self.AlbumLstBox.grid(row = 0, column = 3, padx = 20, pady = 20)
        self.SongLstBox.grid(row = 0, column = 5, padx = 20, pady = 20)
        self.ArtistLstBox.bind('<<ListboxSelect>>', self.GetArtist)
        self.AlbumLstBox.bind('<<ListboxSelect>>', self.AddSongs)
        self.SongLstBox.bind('<<ListboxSelect>>', self.GetPath)

    def AddScrollBar(self):
        """Add & Configure Scrollbars"""
        self.ArtistLstBoxScroll = Scrollbar(self.LstBoxFrm)
        self.AlbumLstBoxScroll = Scrollbar(self.LstBoxFrm)
        self.SongLstBoxScroll = Scrollbar(self.LstBoxFrm)
        self.ArtistLstBoxScroll.grid(row = 0, column = 0, padx = 20, pady = 20, sticky = 'ns')
        self.AlbumLstBoxScroll.grid(row = 0, column = 2, padx = 20, pady = 20, sticky = 'ns')
        self.SongLstBoxScroll.grid(row = 0, column = 4, padx = 20, pady = 20, sticky = 'ns')
        self.ArtistLstBox.config(yscrollcommand = self.ArtistLstBoxScroll.set)
        self.AlbumLstBox.config(yscrollcommand = self.AlbumLstBoxScroll.set)
        self.SongLstBox.config(yscrollcommand = self.SongLstBoxScroll.set)
        self.ArtistLstBoxScroll.config(command = self.ArtistLstBox.yview)
        self.AlbumLstBoxScroll.config(command = self.AlbumLstBox.yview)
        self.SongLstBoxScroll.config(command = self.SongLstBox.yview)

    def AddButtons(self):
        """Add Buttons"""
        self.PlayButton = Button(self.ButtonsFrm, text='Play', height = 2, width = 10 ,fg = 'black', activebackground = "yellow", bg = 'light blue', bd = 4, command = self.PlaySong)
        self.PauseButton = Button(self.ButtonsFrm, text='Pause', height = 2, width = 10 ,fg = 'black', activebackground = "yellow", bg = 'light blue', bd = 4, command = self.PauseSong)
        self.NextButton = Button(self.ButtonsFrm, text='>>', height = 2, width = 10 ,fg = 'black', activebackground = "yellow", bg = 'light blue', bd = 4, command = self.NextSong)
        self.PreviousButton = Button(self.ButtonsFrm, text='<<', height = 2, width = 10 ,fg = 'black', activebackground = "yellow", bg = 'light blue', bd = 4)
        self.StopButton = Button(self.ButtonsFrm, text='Stop', height = 2, width = 10 ,fg = 'black', activebackground = "yellow", bg = 'light blue', bd = 4, command = self.Stop)
        self.PlayButton.grid(row = 0, column = 1, padx = 20, pady = 20)
        self.PauseButton.grid(row = 0, column = 3, padx = 20, pady = 20)
        self.NextButton.grid(row = 0, column = 4, padx = 20, pady = 20)
        self.PreviousButton.grid(row = 0, column = 0, padx = 20, pady = 20)
        self.StopButton.grid(row = 0, column = 2, padx = 20, pady = 20)
               
    def AddArtistLst(self):
        """Add Artists to List Boxes"""
        self.DirectoryList = os.listdir()
        self.Count = 1
        for Item in self.DirectoryList:
            if '.py' not in Item:
                self.ArtistLstBox.insert(self.Count, self.DirectoryList[self.Count - 1])
            self.Count += 1
            
    def GetArtist(self, event):
        """Get Selected Artists so Albums can be added"""
        self.widget = event.widget
        self.Selection = self.widget.curselection()
        self.Value = self.widget.get(self.Selection[0])
        self.AddAlbums()

    def AddAlbums(self):
        """Add Albums"""
        self.TempDir = os.listdir(self.Value)
        self.Counter = 1
        self.AlbumLstBox.delete(0, END)
        self.SongLstBox.delete(0, END)
        for Items in self.TempDir:
            self.AlbumLstBox.insert(self.Counter, self.TempDir[self.Counter - 1])
            self.Counter += 1

    def AddSongs(self, event):
        """Add Songs to List Boxes"""
        self.Widget = event.widget
        self.NewSelection = self.Widget.curselection()
        self.NewValue = self.Widget.get(self.NewSelection[0])
        self.TempD = os.listdir(self.Value + '/' + self.NewValue)
        self.Counters = 1
        self.SongLstBox.delete(0, END)
        for Song in self.TempD:
            self.SongLstBox.insert(self.Counters, self.TempD[self.Counters - 1])
            self.Counters += 1

    def GetPath(self, event):
        """Get Path of Selected"""
        self.Widgets = event.widget
        self.NewestSelection = self.Widgets.curselection()
        self.NewestValue = self.Widgets.get(self.NewestSelection[0])
        self.FullPath = self.Value + '/' + self.NewValue + '/' + self.NewestValue
            
    def PlaySong(self):
        """Play Songs"""
        self.CurrentlyPlaying = self.Value + '/' + self.NewValue + '/' + self.NewestValue
        self.source = pyglet.resource.media(self.CurrentlyPlaying)
        self.player.queue(self.source)
        self.Tree = os.listdir(self.Value + '/' + self.NewValue)
        self.Itterator = 0
        for c in range(len(self.Tree) - 1):
            self.Itterator += 1
            print(self.Value + '/' + self.NewValue + '/', self.Tree[self.Itterator])
            self.Nxt = self.Value + '/' + self.NewValue + '/' + self.Tree[self.Itterator]
            self.NxtLoaded = pyglet.resource.media(self.Nxt)
            self.player.queue(self.NxtLoaded)
        self.player.play()
        
        
    def PauseSong(self):
        """Pause Songs"""
        self.player.pause()

    def NextSong(self):
        """Next Song"""
        self.player.next_source()

    def Stop(self):
        """Stop songs supposadly..."""
        for I in range(self.Itterator + 1):
            self.player.next_source()
            
            
        

loadwindowone = LoadWindowOne(root)
root.mainloop()
