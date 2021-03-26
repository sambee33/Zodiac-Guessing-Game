#opener
print()
import urllib.request
import http.cookiejar

cj = http.cookiejar.MozillaCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

#loop setup
keepgoing = True 
URLstart = "http://en.wikipedia.org/wiki/"
score = 0
plays = 0
tutorial= input("Welcome to the zodiac game! Before we start, do you need a list of the signs? (Y/N) ")
if tutorial == "Y":
    print("The signs are: Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Sagittarius, Capricorn, Aquarius and Pisces!")
    print()
#game loop
while keepgoing == True:
    plays = plays + 1 
    person = input("Whose sign do you want to guess?" + "\n" + "Public figures only, I'm not psychic! ")
    if person.lower() == "zendaya":
        print("ZENDAYA IS MEECHEE!")
    URLend = person.replace(" ","_")
    completedURL = URLstart + URLend
    websitefile = opener.open(completedURL)
    decodedfile = websitefile.read().decode('utf-8')
    bdayindex = decodedfile.find('"bday">')
    if bdayindex > -1:
        bday = decodedfile[bdayindex+12:bdayindex+17]
        month = decodedfile[bdayindex+12:bdayindex+14]
        day = decodedfile[bdayindex+15:bdayindex+17]
        if month == "01":
            if int(day) <= 19:
                zodiac = "Capricorn"
            else:
                zodiac = "Aquarius"
        elif month == "02":
            if int(day) <= 18:
                zodiac = "Aquarius"
            else:
                zodiac = "Pisces"
        elif month == "03":
            if int(day) <= 20:
                zodiac = "Pisces"
            else:
                zodiac = "Aries"
        elif month == "04":
            if int(day) <= 19:
                zodiac = "Aries"
            else:
                zodiac = "Taurus"
        elif month == "05":
            if int(day) <= 20:
                zodiac = "Taurus"
            else:
                zodiac = "Gemini"
        elif month == "06":
            if int(day) <= 20:
                zodiac = "Gemini"
            else:
                zodiac = "Cancer"
        elif month == "07":
            if int(day) <= 21:
                zodiac = "Cancer"
            else:
                zodiac = "Leo"
        elif month == "08":
            if int(day) <= 22:
                zodiac = "Leo"
            else:
                zodiac = "Virgo"
        elif month == "09":
            if int(day) <= 22:
                zodiac = "Virgo"
            else:
                zodiac = "Libra"
        elif month == "10":
            if int(day) <= 22:
                zodiac = "Libra"
            else:
                zodiac = "Scorpio"
        elif month == "11":
            if int(day) <= 21:
                zodiac = "Scorpio"
            else:
                zodiac = "Sagittarius"
        elif month == "12":
            if int(day) <= 21:
                zodiac = "Sagittarius"
            else:
                zodiac = "Capricorn"
        else:
            print("Birthday unknown, sorry!")
    zodiacguess = input("Guess their sign: ")
    if zodiac.lower() == zodiacguess.lower():
        print("Congrats! You got it right!")
        print()
        score = score + 1
    else:
        print("Sorry, that's not correct.")
        print("The correct answer was " + zodiac + ".")
        print()
    stopper = input("Would you like to play again? (Y/N) ")
    if stopper.lower() == "n":
        keepgoing = False
        print()
        print("Bye! Thanks for playing!")
        print("Your final score was: " + str(score))
        accrating = score/plays
        accpercent = (score/plays)*100
        print("You had an accuracy rating of " + str(accpercent) + " percent!")
        if accpercent <= 25:
            print("Come on, even Costar can do better!")
        elif accpercent in range(26,51):
            print("Not bad, keep working on your ESP!")
        elif accpercent in range(51,76):
            print("Very impressive!")
        elif accpercent in range(76,100):
            print("Are you psychic or something?")
        elif accpercent == 100:
            print("A perfect score!!! Sure you didn't cheat?")
     
    
