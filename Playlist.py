from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None

  def add_song(self, title):
    #create a new song object
    #Make sure the song object is title cased
    new_song = Song(title.title())
    #set the new song to the first song 
    new_song.next = self.__first_song
    #set the head to the new song
    self.__first_song = new_song

  def find_song(self, title):
    current_song = self.__first_song
    index = 0

    while current_song != None:
      #if we find the song title passes, return it's index
      if current_song.get_title() == title:
        return index
      # if we didn't find it, increase the index and move to the next song
      index += 1
      current_song = current_song.next
      #If we don't find the song in the list, return -1.
    return -1

  #We need to keep track of the previous song and the current song
  def remove_song(self, title):
    current_song = self.__first_song
    previous_song = None

    while current_song.get_title() != None:
      #if the song title does not equate to our title passed, move through the list
      if current_song.get_title() != title:
        previous_song = current_song
        current_song = current_song.next

      #if there is no previous song, we're on the first song so set it to None
      if current_song.get_title() == title:
        if previous_song == None:
          self.__first_song = None
          return
          #if the next pointer is None then we're on the last song
          # In that case set the previous song's next pointer to None
        if current_song.next == None:
          previous_song.next = None
          return
          #If the song is the first or last song, set the previous song's next pointer
          # to the current songs next pointer
        previous_song.next = current_song.next
        return

  def length(self):
   counter = 0
   current_song = self.__first_song
  # while there are songs in the list update the counter
   while current_song != None:
     counter +=  1
     current_song = current_song.next
    
   return counter

  def print_songs(self):
    #set the current song to the first song
    current_song= self.__first_song
    #set the counter = 1
    counter = 1
    # while there are songs in the list print the number it's on and the name
    while current_song != None:
      print (f"{counter}. {current_song}")
      # set the song to the next song
      current_song = current_song.next
      #increase the counter 
      counter += 1
