##The purpose of this script is to populate database with data with need.
##It's a more autonomous process that can immediately populate the database
##in case the database file is deleted or needed to be deleted

import os


def populate():

    #add question to poll object
    first_poll = add_poll("What country have you always wanted to visit?")

    #array of countries
    countries = ["Afghanistan","Albania","Algeria","Andorra","Angola","Antigua and Barbuda",
                 "Argentina","Armenia","Aruba","Australia","Austria","Azerbaijan",
                 "Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize",
                 "Benin","Bhutan","Bolivia","Bosnia and Herzegovina","Botswana","Brazil",
                 "Brunei","Bulgaria","Burkina Faso","Burma","Burundi",
                 "Cambodia","Cameroon","Cape Verde","Central African Republic","Chad",
                 "Chile","China","Colombia","Comoros","Democratic Republic of the Congo",
                 "Republic of the Congo","Costa Rica","Cote d'Ivoire","Croatia","Cuba",
                 "Curacao","Cyprus","Czech Republic","Denmark","Djibouti","Dominica",
                 "Dominican Republic","East Timor","Ecuador","Egypt","El Salvador","Equatorial Guinea",
                 "Eritrea","Estonia","Ethiopia","Fiji","Finland","France","Gabon",
                 "The Gambia","Georgia","Germany","Ghana","Greece","Grenada","Guatemala",
                 "Guinea","Guinea-Bissau","Guyana","Haiti","Holy See","Honduras","Hong Kong",
                 "Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Isreal","Italy",
                 "Jamaica","Japan","Jordan","Kazakhstan","Kenya","Kiribati","North Korea","South Korea",
                 "Kosovo","Kuwait","Kyrgyzstan","Laos","Latvia","Lebanon","Lesotho","Liberia",
                 "Libya","Liechtenstein","Lithuania","Luxembourg","Macau","Macedonia","Madagascar",
                 "Malawi", "Malaysia","Maldives","Mali","Malta","Marshall Islands","Mauritania",
                 "Mauritius","Mexico","Micronesia","Moldova","Monaco","Mongolia","Montenegro","Morocco",
                 "Mozambique","Namibia","Nauru","Nepal","Netherlands","Netherlands Antilles","New Zealand",
                 "Nicaragua","Niger","Nigeria","North Korea","Norway","Oman","Pakistan","Palau",
                 "Palestinian Territories","Panama","Papua New Guinea","Paraguay","Peru","Philippines",
                 "Poland","Portugal","Qatar","Romania","Russia","Rwanda","Saint Kitts and Nevis",
                 "Saint Lucia","Saint Vincent and the Grenadines","Samoa","San Marino","Sao Tome and Principe",
                 "Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Sint Maarten",
                 "Slovakia","Slovenia","Solomon Islands","Somalia","South Africa","South Korea","South Sudan",
                 "Spain","Sri Lanka","Sudan","Suriname","Swaziland","Sweden","Switzerland","Syria",
                 "Taiwan","Tajikistan","Tanzania","Thailand","Timor-Leste","Togo","Tonga","Trinidad and Tobago",
                 "Tunisia","Turkey","Turkmenistan","Tuvalu","Uganda","Ukraine","United Arab Emirates",
                 "United Kingdom","Uruguay","Uzbekistan","Vanuatu","Venezuela","Vietnam","Yemen",
                 "Zambia","Zimbabwe"]

    
    for i in range(0, len(countries)):
        add_country(question=first_poll,nation=countries[i],votes=0)
        
##    first_poll = add_poll('What country have you always wanted to visit?')

##    add_country(
##    add_country(question=first_poll, nation=countries[0],votes=0)

    #print all question objects
    for q in Question.objects.all():
        print str(q)

    #print all country objects filtered under Question object
    for c in Country.objects.filter(poll=first_poll):
        print str(c)


def add_poll(question):
    p = Question.objects.get_or_create(question=question)[0]
    return p

def add_country(question, nation, votes=0):
    c = Country.objects.get_or_create(poll=question,choice_text=nation, votes=votes)[0]
    return c



if __name__ == '__main__':
    print "Starting polls application script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    from polls.models import Question, Country
    populate()
