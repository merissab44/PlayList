from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None


  # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):
    #create a new song object
    new_song = Song(title)
    #set the new song to the first song 
    new_song.next = self.__first_song
    #set the head to the new song
    self.__first_song = new_song



  # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index. The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index.

  def find_song(self, title):
    current_song = self.__first_song
    counter = 0

    while current_song != None:
      if current_song.get_title() == title:
        return counter
      counter += 1
      current_song = current_song.next
    return -1


  # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):
    current_song = self.__first_song
    previous_song = None

    while current_song.get_title() != None:
      if current_song.get_title() != title:
        previous_song = current_song
        current_song = current_song.next
      # If the previous song points to the song I want to remove
      # then set the pointer to the next next song
      if current_song.get_title() == title:
        if previous_song == None:
          self.__first_song = None
          return
        if current_song.next == None:
          previous_song.next = None
          return
        previous_song.next = current_song.next
        return



  # TODO: Create a method called length, which returns the number of songs in the playlist.

  def length(self):
   counter = 0
   current_song = self.__first_song

   while current_song != None:
     counter +=  1
     current_song = current_song.next
    
   return counter
  # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
    current_song= self.__first_song
    counter = 1
    while current_song != None:
      print (f"{counter}. {current_song}")
      current_song = current_song.next
      counter += 1
