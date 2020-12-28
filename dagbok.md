25/12

Jag bestämde att skapa ett program som skriver dagens datum, vädret och temperaturen till en fil.
Först började jag leta efter ett väder api, jag försökte att få det från en vanlig hemsida men jag lyckades inte. Tillslut hittade jag ett api som lämnade data om vädret i en stad i Indien. När Jag ändrade stadens namn i länken mot Göteborg så fick jag den data jag ville.
För att få date använde jag date funktion som finns i Linux.
Jag började skapa ett python program och började försöka skriva ut den data som jag behövde för att testa. Temperaturen jag fick var i Kelvin och då var jag tvungen att omvandla det till Celsius. 

26/12
Mitt mål var att skriva den data som jag fick till en fil. Jag skapade en fil och skrev i den datan men jag fick ett problem, den ville inte skriva temperaturen i filen. Din gissning var att det var på grund av att temperaturen var float, därför omvandlade jag temperaturen till string och då lyckades jag skriva in informationen i filen.

27/12
All min code fanns i en fil, det var inte snyggt tänkte jag. På grund av det bestämde jag att dela upp det i filer, klasser och funktioner.
Skapde en fil som hade en funktion som returnerar datumet. En fil som har funktioner som returnerar vädrets information. Jag ville att funktionerna kommunicerar med varandra då fick jag ett problem att jag inte kunde göra det.  Jag skapade en class med init funktionen, viste inte hur man använder det men efter några timmar lyckades jag. Hade problem med instances.
Sen skapade jag en fil som innehåller en funktion som skriver in informationen vi fick från filerna date och väder i en text fil. Funktionen kunde inte nå informationen från andra filerna och då skapade jag en class därefter gick det bra när jag testade körde det i själva filen.

I main filen körde jag programmet men då funkade programmet inte. Den sa att den inte kunde hitta fil som innehåller date. Problemet var att jag inte skrev från vilken mapp jag ville importera filen. Programmet funkar!
Testade programmet i Windows och i Linux. Filen skapades och informationen skrevs i den!


Tjänster i Linux
Systemlog
Cups 
Ntp
Kudzu upptäcker hårdvara som är ni eller modifierad
httpd tillhandahåller en Apache-webbserver 
smtp skickar och tar emot e-post
cron som används för att utföra schemalagda uppgifter
gpm som stöder musfunktionalitet
	

