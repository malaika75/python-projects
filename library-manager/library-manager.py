#ek file bnaye gy isme user ki files add hongi us file ko save kr lengy ek variable me phir uspr functions bnaye gy 
#ek function jo file jo user add kry ga agr exist krti hy tu  ussy load kry or open kry
#ek function jo user ki file ko w write mode me open kr ky save kry ga us file me jo humny bariable me store kia hy 
#ek function jo new books ko add krny ka kaam kry ga hum isme inputs bnaye gy title , auther , year, genre, read
# ye sab add krny ky liye inko save bhi krna hoga jo bhi user de ga inputs me tu ussy hum dictionary me save kr lengy or phir save kr ky save function ko call kr ky or phir success message print krwa dengy 
#ek function bnaye gy book remove krny ky liye or phir un books ko save krny ky liye 
#ek function jisse search kr ky book ko dhondh saky isme hum ye likh sakty hy ky 
# book for book in library if search_term in book {search_by} is trah serch kr ky hum show krwa sakty hy 
#ek function humny list ka bnana hy jo puri library or usky read ya unread show kry 
# ek function jo statistics show kry ga ky kitny reads hy kitni books hy isme hum total book ki length or read ki lengh ko divede kr ky or 100 se multiply kr ky uski percentage nikaly gy or dekaye gy user ko
# ab hum ek main function bnaye gy or isme while true lga dengy taky loop chalta rahy jb tk user exit na kry ky jisse user dekhy ga ky usey konsa kaam krna hy library me usey sari choice dengy wo jo bhi select kry ga usy input me likh dy ga hum us input ki base pr functions ko call kr dengy 
# phir end me hum likh dengy if __name__ ==  '__main __': phir nechy main() is trah likh kr main function ko call kr dengy is ka mtlb hy ye cli main function se start o 


import json 
import os
import streamlit as st

data_file = 'library.txt'

def load_file():
    if os.path.exists(data_file):
     with open(data_file ,'r') as file:
      return json.load(file)


def save_file(library):
    with open(data_file , 'w') as file:
       json.dump(library , file)


def add_file(library):
   title = input('Enter book title ')
   author = input('Enter book author ')
   year = input('Enter publish year ')
   genre = input('Enter book type ')
   read = input('have you read this book :yes/on ').lower() == 'yes'
   
   new_addition = {
   'title' : title,
   'author': author,
   'year' :year,
   'genre':genre,
   'read' :read
}
   library.append(new_addition)
   save_file(library)
   print(f'New book {title} added successfully in your library')


def remove(library):
   if not library:
      print('library is empty')
      return

   file_name = input('Enter title for remove book from library ').strip().lower()
   new_library = [book for book in library if book['title'].strip().lower() != file_name]

   if len(library) == len(new_library):
      print('book not found')
   else:
      print(f'removed {file_name} book successfully')
      library[:] = new_library
      #library[:] = new_library Original list modify hoti hai purani list ko new list se replace krny ky liye hum ayse likhty hy 
      save_file(library)


def search(library):
   if not library:
      print('library is empty')
      return
   found = False
   search_bar = input('search book by title or author ').strip().lower()
   for book in library:
      if search_bar in book['title'].lower() or search_bar in book['author'].lower():
        print(f'[title: {book['title']} | Author: {book['author']} | genre: {book['genre']}]')
        found = True
        break
   if not found:
      print('404 not found')


def display_books(library):
  if library:
    for book in library:
     status = "Read" if book['read'] else 'unread'
     print(book , status)
  else:
     print('your library is empty')


def statistics(library):
   book_stats = len(library)
   read_stats = len([book for book in library if book['read'] ])
   percentage = (read_stats / book_stats ) * 100 if book_stats > 0 else 0
   print(f"total books: {book_stats}")
   print(f"Read percentsge: {percentage:.2f}%")

def main():
   library = load_file()
   while True:
      print("Wellcome! to the library")
      print("1. Add a new book")
      print("2. search book")
      print("3. Remove book")
      print("4. Diplay all books")
      print("5. Display statistics")
      print("6. exit")

      choice =  input("Enter task number here to continue ")
      if choice == "1":
         add_file(library)
      elif choice == "2":
         search(library)
      elif choice == "3":
         remove(library)
      elif choice == "4":
         display_books(library)
      elif choice == "5":
         statistics(library)
      elif choice == "6":
         print("GoodBye")
         break


if __name__ == '__main__':
   main()