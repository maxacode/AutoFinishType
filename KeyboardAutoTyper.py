try:
    #Importing custom module that interacts with the OS keyboard - #https://pypi.org/project/keyboard/
    import keyboard

    print("Running Secure Keyboard Shortcuter")

    #Adding a shortcut's
    keyboard.add_abbreviation('@1', 'maxderevencha@gmail.com')
    print('@1', ' : maxderevencha@gmail.com')
    
    keyboard.add_abbreviation('@2', 'max@hacked.fyi')
    print('@2', ' : max@hacked.fyi')
    
    keyboard.add_abbreviation('@3', 'max@callitclosed.com')
    print('@3', ' : max@callitclosed.com')
    
    
    keyboard.add_abbreviation('2898', '2898 Gipper Circle, Sanford Florida, 32773')
    print('2898', ' : 2898 Gipper Circle')
    
    keyboard.add_abbreviation('417', '417-522-8598')
    print('417', ' : 417-522-8598')
    
    keyboard.add_abbreviation('teh', 'the')
    keyboard.add_abbreviation('Teh', 'The')
    
    keyboard.add_abbreviation('MD', 'Maksim Derevencha')
    print('MD', ' : Maksim Derevencha')
    
    keyboard.add_abbreviation('mdlin', 'www.linkedin.com/in/max-derevencha')
    print('mdlin', ' : www.linkedin.com/in/max-derevencha')
    
    keyboard.add_abbreviation('gv', '407-900-3908')
    print('gv', ' : 407-900-3908')
    
    #Run until closed sorta like "While True"
    keyboard.wait()

#Exceptions just in case.
except Exception as e:
    print(e)
    input('')