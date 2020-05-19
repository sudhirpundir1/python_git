with open('a.txt','r') as file:
    try:
        file.write('My name is Sudhir_3')
    except Exception as e:
        print('Exception Occured: ',e)
    else:
        print('No exception, File has been successfully modified')
    finally:
        print('This code is always executed...!')
        file.close()
