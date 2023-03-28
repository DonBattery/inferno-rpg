# Inferno RPG

Magyar szöveges Discord kaland játék

![Inferno logo](doc/icon.png)

**Vigyázat Hunglis! Danger Hunglis!**  
Beware this repository heavily uses Hungarian language both in documentation and code.  

Mind a dokumentációban mind a kódban keverve fordulnak elő magyar és angol szavak.  

A cél elsősorban az, hogy egy magyar nyelven játszható játékot készítsünk. Illetve, hogy a kód-ban is magyar nyelvű kommentek legyenek a honi gyerekek okulása véget.  

Viszont csak pár változónak és funkciónak van magyar neve. A legtöbbnek angol megfelelője van, ez lehet sokakat zavar de meg kell tanulni együtt élni vele.  

## Mi ez?
Az InfernoRPG egy szöveges kalandjáték, amit Discordon lehet játszani. A program Python3 nyelven íródott és a [discord.py](https://discordpy.readthedocs.io/en/stable) package-t használja, hogy létre hozzon egy bot-ot, ami egy token segítségével csatlakozik a Discord-hoz (hasonlóan egy igazi felhasználóhoz). Amely szerverekre (guild-ekbe) meg van hívva, ott tudja olvasni az üzeneteket. A `!felkijáltójeles` parancsokra reagál (már amelyiket ismeri) és amelyik csatornában kiadták a parancsot ott fog válaszolni rájuk.  

## Hogyan játszhatom a játékot?
Csak meg kell hívnod az InfernoRPG bot-ot a Discord szerveredre, és már el is kezdhetsz játszani a barátaiddal. A `!help` paranccsal tájékozódhatsz a kiadható parancsokról.  

## Hogyan alakíthatom át a játékot?
Ez egy szabad szoftver, ami első sorban a tanulást szolgálja. Nyugodtan megklónozhatod, megforkolhatod a repót. Bármit változtathatsz a kódon és bárhogy felhasználhatod a részeit vagy az egészet (az eredeti szerzők semmilyen felelőséget nem válalnak az esetlegesn keletkezett hibákért)  

A lokális futtatáshoz minimum Python 3.10 szükséges. Miután megklónoztad a repót, lépj be az app alkönyvtárba és add ki a `pip install -r requirements.txt` parancsot, ez felteszi a pitonos package-ket, amiket a program használ. Ez után futtathatod a programot a `DISCORD_TOKEN=a_te_botod_discord_tokence python bot.py` paranccsal. A **DISCORD_TOKEN** egy környezeti változó, ami akár a .env file.ból is jöhet. Értéke a te bot-od tokenje.  

### Maga a Discord Bot
Ahhoz, hogy a saját Discord botot futtassuk, előszőr meg kell őt kreálni és meg kell hívni a saját szerverünkre. [Leírás](doc/discord_bot_creation/create_the_discord_bot.md)  
