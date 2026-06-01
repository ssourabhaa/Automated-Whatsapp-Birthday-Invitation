import pywhatkit

# Guest names and whatsapp phone numbers to send message
guestDetails = {'Suvarna' : '+91xxxxxxxxxx',
                'Sanu' : '+91xxxxxxxxxx',
                'Vinay' : '+91xxxxxxxxxx',
                'Suman': '+91xxxxxxxxxx',
                'Ashwini' : '+91xxxxxxxxxx',
                'Aruna' : '+91xxxxxxxxxx',
                'Santosh': '+91xxxxxxxxxx',
                'Yogesh': '+91xxxxxxxxxx',
                'Satish': '+91xxxxxxxxxx',
                'Mahesh': '+91xxxxxxxxxx',
                'Sameeksha': '+91xxxxxxxxxx',
                'Girish': '+91xxxxxxxxxx'}

message = """
Hi {name} & Family, 😄 \n
We are excited to celebrate Hruday\'s 12th birthday on 25th Oct and \
would love for you to join us! 🥳 It'll be a fun filled day with cake cutting 🎂, \
exciting games 🎲 and great memories ❤️! Your presence will make it extra special 🥰 
* Date: 25th Oct 2024 
* Time: 6:00pm onwards
* Venue: XYZ road 2nd cross, Bangalore

With Love ❤️,
Hruday & Family"""

imagePath = r'C:\Users\Sourabha\Documents\bday_image.jpg'

# Iterate through dictionary to get each guest name and guest phone number
for guestName, guestPhoneNumber in guestDetails.items():
    guestMessage = message.format(name = guestName)
    try:
        pywhatkit.sendwhats_image(guestPhoneNumber, imagePath)
        pywhatkit.sendwhatmsg_instantly(guestPhoneNumber, guestMessage)
        print(f'Sent message to {guestName}.')   
    except Exception as e:
        print(f'Error sending message to {guestName}: {e}')
print('Completed sending birthday invitation to guests.')