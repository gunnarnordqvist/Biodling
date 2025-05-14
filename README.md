# Experiment - AI-genererad [webbplats](https://gunnarnordqvist.github.io/Biodling/) om Bin och biodling

Detta är ett experiment för att se hur långt jag lyckades få Gemini 2.5 Flash. 
Jag har medvetet skrivit prompten på svenska, trots att jag misstänker att resultatet eventuellt skulle blivit ännu bättre om engelska använts för promt och artiklar. 
Jag har startat prompten nedan och efter det bara sagt "godkänt" efter respektive iteration.
Jag valde att bara använda mobiltelefonen för att genomför detta, för att inte frestas att göra för mycket själv.

## Anpassningar
Jag gjorde inställningarna i GitHub manuellt, det är möjligt att det skulle gått att få AI att automatisera det också, men jag tyckte inte att det var fokus för mitt arbete.
På grund av begränsningar i gränssnittet har jag kopierat svaren och kopierat in scriptet ```./github/scripts/create.py ```.
Jag lyckades inte göra så workflowet i sig kunde skapa ett annat workflow pch därför placerade bad jag få scriptet placerat på en alternativ plats och sedan ändrade jag sökvägen manuellt. 
Det blev rtt ps små praingfel och då lät jag GitHub Copilot åtgärda dessa genom att klistra in länken till körningen av det misslyckade workflowet.

## Prompt
Följande prompt användes:

```code

Website om Bin

Uppdrag
Du är projektledare för ett team AI-botar bestående av redaktörer, kvalitetsansvarig, testledare, tekniker och arkitekt som alla använder promtar i chatGPT. Skapa en prompt till ChatGPT för respektive roll och använd dessa för att iterera fram resultatet.
Du ska rapportera status till mig löpande.
Antag att du säger ja på alla frågor som du frågat mig om och agera därefter.

Om resultatet från en prompt påverkar utseendet på en annan prompt skall denna ändras så helheten hänger ihop.

Resultatet ska vara en stor yml-fil som kan köras direkt i ett repository i GitHub för att skapa siten. Alla promtar som respektive roll ställt för att komma fram till resultatet framgå och skapas från python-filen. Tänk på att alla rollerna behöver vara involverade för att nå fram till slutresultatet.

Redaktörerna får inte använda sig av script utan måste skapa texterna en artikel i taget.

Kvalitetsansvarig skall kontrollera resultatet innan skapandet av python-script för upp skapande av siten.

Mål
Teamet ska ha skapat en site på svenska med 50 artiklar om bin med minst 1500 tecken  i vardera. 
Varje artikel måste innehålla unikt material och får inte innehålla mer än 5 % återupprepning med övriga artiklar. 
En termlista med samtliga termer som används skall också finnas.
Helt verkligt skriven (inga placeholders).
Möter 1750 tecken ± 250.

Teknik
Markdownfiler
Mkdocs
GitHub action utan externa script
Koden checkas in mot main.

Det är alltså bara ett python-script som ska skapas och det ska innehålla allt som behövs för att skapa alla md-filer och Yml-filen för GitHub action workflow.

Arbetet ska ske iterativt i sekvens och presentera fem artiklar som första batch och öka med 5 per batch om resultatet av föregående iteration var bra.
Jag är projektägaren och det är jag som bestämmer om nästa iteration får startas. Jag vill ha en demo av resultatet efter varje iteration. 
Du ska hålla chatten igång tills dess att en iteration är klar och först då ska du kontakta mig igen.
Efter varje iteration skall scriptet presenteras.

DU MÅSTE LÄGGA ALLT SOM BEHÖVS I ETT SCRIPT!

Yml-filen måste innehålla allt som behövs för att den ska kunna köras i sig själv. Inga ytterligare script ska behövas. Scriptet skall placeras på den alternativa platsen. ./github/workflow
```

### Slutsats
Detta ger en fingervisning om vad denna modellen kan göra och hur snabbt utvecklingen inom AI går. Jag har gjort motsvara test med GPT 3.5, GPT-4o, o4-mini och o4-mini-high, men ingen av dessa gav i närheten lika bra resultat. Gemini 2.0 gav ett liknande resultat från början men tappade snabbt bort sig.
Resultatet visar tydligt att nivån på vad allmänt tillgängliga LLM:er kan göra ökar snabbt. 
Det är redan på en sådan hög nivå att utan djup kännedom om området som hanteras är det väldigt svårt att veta om det som står är sant eller ej. 

/Gunnar Nordqvist 
