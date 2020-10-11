def change():
    time=input("Enter the time in 24 hour format:")
    if  time[:2]=='00':
     return '12'+time[2:]+'AM'
    else:
        return(str(int(time[:2])-12)+time[2:]+'PM')
print(change())


