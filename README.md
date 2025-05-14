# Experiment - AI-genererad https://gunnarnordqvist.github.io/Biodling/](webbplats) om Bin och biodling

Detta är ett experiment för att se hur långt jag lyckades få Gemeni 2.5 Flash. 
Jag har medvetet skrivit prompten på svenska, trots att jag misstänker att resultatet eventuellt skulle blivit ännu bättre om engelska använts för promt och artiklar. 
Jag har startat prompten nedan och efter det bara sagt "godkänt" efter respektive iteration.
På grund av begränsningar i gränssnittet har jag kopierat svaren och kopierat in scriptet ./github/scripts/create.py .
Jag lyckades inte göra så workflowet i sig kunde skaåa ett annat workflow pch därför placerade bad jag få scriptet placerat på wn alternativ plsts och sedan ändrade jag sökvägen manuellt. 

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

Detta ger en fingervisning om vad denna modellen kan göra och hur snabbt utvecklingen inom AI går. Jag har gjort motsvara test med GPT 3.5, GPT-4o, o4-mini och o4-mini-high, men ingen av dessa gav i närheten lika bra resultat. Gemini 2.0 gav ett liknande resultat från början men tappade snabbt bort sig.
/Gunnar Nordqvist 
