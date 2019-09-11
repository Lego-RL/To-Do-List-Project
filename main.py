'''

This program allows you to enter items into a list & save them for later. 
'q' to quit the program.
'del {list number}' to remove an item in the list
'clear' to remove the list

Note: List will likely not be saved between programs if you click exit instead of typing 'q' to quit the program.

'''


from replit import clear
import sys

def delete(numDeleted):
  '''Deletes a specific line in a text file
  if the number at the start of the line isn't equal to
  the number the user inputted (which is passed into the function)'''

  print('\n')
  file.seek(0)
  lines = file.readlines()
  file.seek(0)
  entryNum = 1

  for line in lines:
    if line[0] != numDel:
      file.write(str(entryNum) + line[1:])
      entryNum += 1

  file.truncate()



with open("todolist.txt", "r+") as file:
  while True:
    clear()

    file.seek(0)
    words = file.readlines()
    
    for item in words:
      print(item)

    print('-' * 45)
    addTodo = input('Type something to add to the list, q to quit. \nTo remove an entry, type: "del {list number}".\nTo clear the list, type: "clear"\n\n>>> ')

    if addTodo == 'q':
      sys.exit()

    elif addTodo[:3].lower() == 'del':
      numDel = addTodo[-1]
      delete(numDel)

    elif addTodo == 'clear':
      file.truncate(0)

    else:
      file.write(f'{len(words) + 1}) {addTodo}\n')
      print('\n')