try:
    #Importing custom module that interacts with the OS keyboard - #https://pypi.org/project/keyboard/
    import keyboard

    print("Running Secure Keyboard Shortcuter")

    #Adding a shortcut's
    keyboard.add_abbreviation('@@', 'maxderevencha@gmail.com')
    #keyboard.add_abbreviation('randompass', 'Open ')
    keyboard.add_abbreviation('2898', '2898 Gipper Circle, Sanford Florida, 32773')
    keyboard.add_abbreviation('417', '417-522-8598')
    
    #Run until closed sorta like "While True"
    keyboard.wait()

#Exceptions just in case.
except Exception as e:
    print(e)
