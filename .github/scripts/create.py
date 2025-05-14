import os

# --- Prompts Used in Iterations 1, 2, 3, 4, 5 & 6 ---

# Prompt used for the Arkitekt role to design the structure (Iteration 1)
ARKITEKT_PROMPT_ITER1 = """
Designa filstrukturen för en MkDocs webbplats om bin. Inkludera en mapp för Markdown-artiklar ('docs/'), en fil för ordlistan ('docs/ordlista.md'), en grundläggande 'docs/index.md' för startsidan, en 'mkdocs.yml' konfigurationsfil i projektets rot, och en plats för en GitHub Actions workflow-fil i '.github/workflows/'. Beskriv hur navigationen i 'mkdocs.yml' bör struktureras för de första 5 artiklarna och ordlistan. Föreslå ett tema.
"""
# Prompt used for the Arkitekt role to review structure (Iteration 2, 3, 4, 5 & 6)
ARKITEKT_PROMPT_REVIEW = """
Granska den nuvarande MkDocs-strukturen och 'mkdocs.yml' baserat på {num_articles} artiklar totalt. Säkerställ att navigationen hanterar det ökade antalet artiklar på ett överskådligt sätt. Bekräfta att den befintliga filstrukturen fortfarande fungerar.
"""


# Prompt used for the Tekniker role to create the initial script outline (Iteration 1)
TEKNIKER_PROMPT_OUTLINE_ITER1 = """
Skapa en Python-script outline som kan generera den filstruktur Arkitekten har designat. Scriptet ska kunna skapa mapparna 'docs' och '.github/workflows'. Det ska ha platshållare för innehållet i 'docs/index.md', artikelfilerna, 'docs/ordlista.md', 'mkdocs.yml' och GitHub Actions YML-filen. Inkludera struktur för att lagra och senare visa de prompts som använts.
"""
# Note: Tekniker's main task in subsequent Iterations was to update the script based on new content and configs.
# No fundamentally new 'outline' prompt was needed, rather implementation instruction based on iteration goals.


# Template prompt used for the Redaktör role to generate each article
REDAKTOR_PROMPT_TEMPLATE = """
Skriv en unik artikel på svenska om {topic}. Artikeln ska vara faktabaserad, lättläst och ha en längd på minst 1500 tecken, sikta på 1750 tecken (± 250 tecken). Fokusera strikt på det angivna ämnet och undvik att upprepa grundläggande fakta som sannolikt finns i andra bi-relaterade artiklar. Skriv i löpande text, lämplig att klistra in i en Markdown-fil (ingen Markdown-formatering utöver rubrik)."
"""
# Specific topics used for Redaktör across all completed Iterations
REDAKTOR_TOPICS_ALL = [
    "Biets Livscykel", # Iteration 1 (5)
    "Drottningbiet", # Iteration 1 (5)
    "Arbetsbinas Många Uppgifter", # Iteration 1 (5)
    "Drönarnas Roll i Bikupan", # Iteration 1 (5)
    "Biets Kommunikation (Vaggdansen)", # Iteration 1 (5)
    "Hot mot Bin (Pesticider, Varroa, Förlust av habitat)", # Iteration 2 (5)
    "Olika Bi-arter i Sverige (Honungsbin, Humlor, Solitärbin)", # Iteration 2 (5)
    "Biodling som Hobby", # Iteration 2 (5)
    "Bins Roll i Ekosystemet (med fokus på pollineringens bredare impakt)", # Iteration 2 (5)
    "Bin i Staden (Urban Biodling)", # Iteration 2 (5)
    "Honungsskörd och Hantering", # Iteration 3 (5)
    "Bin och Blommor: Ett Symbiotiskt Förhållande", # Iteration 3 (5)
    "Bisamhällets Organisation och Superorganismen", # Iteration 3 (5)
    "Olika Typer av Honung och Deras Egenskaper", # Iteration 3 (5)
    "Bin i Historien, Myter och Kulturen", # Iteration 3 (5)
    "Bin och Väder: Hur Påverkas Binas Aktivitet?", # Iteration 4 (5)
    "Drottningens Livsfarliga Parningsflykt", # Iteration 4 (5)
    "Binas Naturliga Fiender (förutom kvalster/sjukdom)", # Iteration 4 (5)
    "Binas Sinnen: Syn, Lukt och Smak", # Iteration 4 (5)
    "Propolis: Binas Kåda och Dess Användning", # Iteration 4 (5)
    "Binas Anatomi: Vingar, Ben och Kroppsdelar", # Iteration 5 (10)
    "Biodlingens Historia Genom Tiderna", # Iteration 5 (10)
    "Olika Typer av Vildbibon", # Iteration 5 (10)
    "Andra Parasiter och Sjukdomar hos Bin (än Varroa)", # Iteration 5 (10)
    "Hur Bin Ser Världen: Färgseende och UV-ljus", # Iteration 5 (10)
    "Bins Behov av Vatten", # Iteration 5 (10)
    "Pollen och Bibröd: Binas Proteinrika Föda", # Iteration 5 (10)
    "Honungsdagg: En Ovanlig Honungskälla", # Iteration 5 (10)
    "Processen att Skapa Bivax", # Iteration 5 (10)
    "Binas Immunförsvar och Hälsa", # Iteration 5 (10)
    "Lagar och Regler Kring Biodling i Sverige", # Iteration 6 (10)
    "Hur Bin Orienterar Sig: Sol, Magnetfält och Landmärken", # Iteration 6 (10)
    "Runddansen och Vaggdansen: Olika Budskap", # Iteration 6 (10)
    "Bin som Pollinatörer av Fruktträd och Bärodlingar", # Iteration 6 (10)
    "Ekologisk Biodling: Principer och Praxis", # Iteration 6 (10)
    "Binas Övervintring: Klotet och Foder", # Iteration 6 (10)
    "Vinterfoder och Vårstimulering i Bikupan", # Iteration 6 (10)
    "Grunderna i Drottningodling", # Iteration 6 (10)
    "Svärmkontroll och Hur Man Hanterar Svärmar", # Iteration 6 (10)
    "Binas Avgörande Roll för Vilda Växters Fortplantning" # Iteration 6 (10)
]
# Note: The Redaktör used the template prompt for each topic to generate content.
# The actual generated content for all 40 articles is stored below.


# Prompt used for the Kvalitetsansvarig role to review articles and find terms (Iteration 1 with 5 articles)
KVALITETSANSVARIG_PROMPT_ITER1 = """
Granska följande 5 artiklar om bin (textinnehåll bifogas). Kontrollera att varje artikel uppfyller längdkravet på minst 1500 tecken (idealt 1750 ± 250). Bedöm om de verkar unika och fokuserade på sina ämnen. Identifiera alla viktiga facktermer som används i artiklarna som bör inkluderas i en ordlista.
"""
# Prompt used for the Kvalitetsansvarig role to review NEW articles and find NEW terms (Iterations 2, 3, 4 with 5 articles per batch)
KVALITETSANSVARIG_PROMPT_NEW_BATCH_5 = """
Granska följande 5 *nya* artiklar om bin (textinnehåll bifogas). Kontrollera att varje artikel uppfyller längdkravet på minst 1500 tecken (idealt 1750 ± 250). Bedöm om de verkar unika, fokuserade på sina ämnen och skiljer sig tillräckligt från de tidigare {num_previous_articles} artiklarna. Identifiera alla nya viktiga facktermer som används i dessa artiklar och som bör läggas till i ordlistan.
"""
# Prompt used for the Kvalitetsansvarig role to review NEW articles and find NEW terms (Iterations 5, 6 with 10 articles per batch)
KVALITETSANSVARIG_PROMPT_NEW_BATCH_10 = """
Granska följande 10 *nya* artiklar om bin (textinnehåll bifogas). Kontrollera att varje artikel uppfyller längdkravet på minst 1500 tecken (idealt 1750 ± 250). Bedöm om de verkar unika, fokuserade på sina ämnen och skiljer sig tillräckligt från de tidigare {num_previous_articles} artiklarna. Identifiera alla nya viktiga facktermer som används i dessa artiklar och som bör läggas till i ordlistan.
"""

# All terms identified by Kvalitetsansvarig across all completed Iterations
KVALITETSANSVARIG_TERMS_ALL = sorted(list(set([
    "Livscykel", "Ägg", "Larv", "Pupa", "Drottning", "Arbetarbi",
    "Drönare", "Bikupa", "Feromon", "Pollen", "Nektar", "Honung",
    "Vax", "Vaggdans", "Svärmning", # Iteration 1 terms
    "Varroakvalster", "Solitärbin", "Humlor", "Habitatförlust", "Pesticider", "Urban biodling", # Iteration 2 terms
    "Honungsskörd", "Slunga", "Ram", "Symbios", "Superorganism", "Nektarkälla", "Pollenkälla", "Propolis", "Bivax", # Iteration 3 terms
    "Parningsflykt", "Predator", "Bifigurer", "Ocelli", "Antenner", "Gadd", # Iteration 4 terms
    "Anatomi", "Facettögon", "Punktögon", "Pollenkorgar", "Bivall", "Cell", "Vaxkörtlar", "Bibröd", "Honungsdagg", "Immunförsvar", "Hemolymfa", "Patogen", # Iteration 5 terms
    "Lagstiftning", "Orientering", "Runddans", "Vårstimulering", "Drottningodling", "Svärmkontroll", "Pollinatör" # Iteration 6 terms
]))) # Use set to get unique terms, then sort

# Note: Added some definitions to the glossary content below based on new terms.

# Prompt used for the Testledare role to create an initial test plan (Iteration 1)
TESTLEDARE_PROMPT_ITER1 = """
Utforma ett första utkast till en testplan för att verifiera den genererade webbplatsen och GitHub Actions workflow. Hur kan vi testa att Python-scriptet körs utan fel, att alla nödvändiga filer skapas korrekt, att 'mkdocs.yml' är giltig, att GitHub Actions workflow triggas vid push till 'main', och att den framgångsrikt bygger och (simulerat) driftsätter webbplatsen?
"""
# Prompt used for the Testledare role to review test plan (Subsequent Iterations)
TESTLEDARE_PROMPT_REVIEW = """
Granska testplanen från tidigare iterationer. Är den fortfarande relevant och tillräcklig för att testa en webbplats med {num_articles} artiklar? Behöver några steg justeras eller läggas till?
"""


# --- Generated Content (Iterations 1-6) ---

# Simulated article content for all 40 articles.
# This dictionary now includes content for all 40 articles.
ARTICLE_CONTENT_ALL = {
    "biets_livscykel.md": """
# Biets Livscykel

Biets livscykel är en fascinerande process som börjar med ett litet ägg och slutar med ett fullvuxet bi, redo att bidra till kupans överlevnad. Livscykeln skiljer sig något mellan drottningar, arbetsbin och drönare, men grundstegen är desamma: ägg, larv, puppa och vuxet bi. Allt börjar när drottningen lägger ett ägg i en av bikupans vaxceller. Dessa celler har i förväg rengjorts och polerats av arbetsbin, vilket säkerställer en hygienisk miljö för den spirande larven.

Ägget är pyttelitet, bara cirka 1,5 millimeter långt, och liknar ett riskorn. Efter ungefär tre dagar kläcks ägget, och en larv kommer fram. Larvstadiet är en period av intensiv tillväxt. Larven matas omväxlande med bidrottninggelé (för drottningar), pollen och nektar av skötarbin. Larven ömsar skinn flera gånger under sin utveckling och växer exponentiellt i storlek. Den tillbringar större delen av sin tid innesluten i cellen, enbart fokuserad på att äta och växa. Efter cirka sex dagar (varierar med typ av bi) är larven fullvuxen och slutar äta.

Därefter påbörjas puppstadiet. Arbetsbin täcker cellen med ett lock av vax och pollen, vilket förseglar larven inuti. Inne i den förseglade cellen spinner larven en kokong runt sig. Nu genomgår den en fullständig omvandling, känd som metamorfos, där larvens kropp omformas till ett vuxet bi med vingar, ben och antenner. Detta stadium varar olika länge beroende på biets kast; en arbetsbi-puppa utvecklas på cirka 12 dagar, en drönarpuppa på 14 dagar, och en drottningpuppa på endast 7 dagar. Den kortare utvecklingstiden för drottningen säkerställer att en ny drottning snabbt kan ta över om den gamla dör.

När omvandlingen är klar, gnager det fullt utvecklade biet sig ut ur sin cell. Det nykläckta biet är mjukt och luddigt, och dess första uppgift är att rengöra sig själv och sin cell. Inom några timmar börjar det utföra sina första sysslor i kupan, vilket markerar början på dess liv som ett vuxet bi. Livslängden för ett vuxet bi varierar kraftigt. Arbetsbin som kläcks på våren eller sommaren lever bara några veckor, utslitna av intensivt arbete med att samla mat och sköta kupan. Bin som kläcks på hösten lever däremot över vintern, då aktiviteten är låg, och deras huvuduppgift är att hjälpa till att hålla kupan varm och ta hand om drottningen tills våren kommer och livscykeln börjar om igen. Drönare lever endast under sommaren och dör efter parning, medan drottningar kan leva i flera år och är bikupans enda fertila individ, ständigt upptagen med att lägga ägg för att säkerställa samhällets fortlevnad. Hela denna cykel är avgörande för bisamhällets överlevnad och framgång.
""",
    "drottningbiet.md": """
# Drottningbiet: Bikupans Hjärta

Drottningbiet är utan tvekan den viktigaste individen i ett bisamhälle. Hon är inte bara kupans moder – hon är den enda fullt utvecklade honan kapabel att lägga ägg, och därmed samhällets reproduktiva kärna. Hennes närvaro och hälsa är avgörande för kupans styrka och överlevnad. Utan en drottning kommer samhället gradvis att förtvina, eftersom inga nya bin kläcks för att ersätta de gamla.

En drottning skiljer sig markant från arbetsbin och drönare, både i utseende och beteende. Hon är större än arbetsbin, med en längre, mer strömlinjeformad kropp. Hennes vingar är proportionellt kortare i förhållande till kroppen jämfört med arbetsbin. Det som verkligen särskiljer henne är hennes reproduktiva organ; medan arbetsbin är sterila, har drottningen fullt utvecklade äggstockar. Hon utvecklas också från ett ägg som matats uteslutande med bidrottninggelé under hela larvstadiet, en näringsrik kost som möjliggör hennes fulla utveckling.

Drottningens primära uppgift är att lägga ägg. En frisk, produktiv drottning kan lägga upp till 1500-2000 ägg per dag under högsäsongen, vilket överstiger hennes egen kroppsvikt. Hon rör sig över vaxkakorna, undersöker tomma celler med sina antenner och lägger snabbt ett ägg i varje lämplig cell. Hon bestämmer också om ägget ska befruktas eller inte; obefruktade ägg blir till drönare (hanbin), medan befruktade ägg blir till arbetsbin (sterila honor) eller nya drottningar. Denna kontroll över könsfördelningen är en annan kritiskt funktion.

Utöver äggläggning kontrollerar drottningen bisamhället genom feromoner – kemiska signaler hon utsöndrar. "Drottningferomonet" sprids i kupan via arbetsbin som sköter om henne. Detta feromon har flera funktioner: det hämmar utvecklingen av äggstockar hos arbetsbin, förhindrar dem från att lägga egna ägg, det signalerar drottningens närvaro och välbefinnande till samhället, och det spelar en roll vid svärmning. När drottningens feromonproduktion minskar (på grund av ålder eller sjukdom) eller när samhället blir för stort, kan arbetsbin uppfatta detta som en signal att samhället behöver en ny drottning eller är redo att svärma.

Livslängden för en drottning är betydligt längre än för arbetsbin och drönare; hon kan leva i upp till 3-5 år, även om hennes produktivitet oftast minskar efter 2-3 år. När drottningen åldras, minskar hennes äggläggningstakt och feromonproduktion. Samhället kommer då att uppfatta behovet av en ersättare och påbörja processen att föda upp en ny drottning genom att mata lämpliga larver med bidrottninggelé. När den nya drottningen är redo, kommer hon att döda den gamla drottningen (om hon inte redan är död) eller, oftare, den gamla drottningen svärmar ut med en del av arbetsbina för att bilda ett nytt samhälle. Drottningens roll är central för bikupans struktur, reproduktion och sociala sammanhållning.
""",
    "arbetsbin.md": """
# Arbetsbinas Många Uppgifter

Arbetsbin utgör den absoluta majoriteten av individerna i ett bisamhälle och är bokstavligen ryggraden i kupans funktion. De är sterila honor vars hela liv, som under sommaren oftast bara varar några veckor, ägnas åt att utföra alla de nödvändiga sysslor som krävs för samhällets överlevnad och blomstring. Deras arbete är noggrant uppdelat baserat på ålder, en fascinerande form av arbetsfördelning som kallas polyetism baserad på ålder. Ett arbetsbi byter gradvis uppgift allteftersom det blir äldre.

De första dagarna efter att ett arbetsbi kläckts ur sin cell är det främst sysselsatt med uppgifter inomhus. Dess första jobb är att rengöra cellen det föddes ur, samt andra celler, för att förbereda dem för nya ägg, pollen eller nektar. De fungerar också som "sköterskebin", vilka har utvecklade körtlar som producerar bidrottninggelé och larvföda. Dessa unga bin matar larverna och drottningen. De hjälper också till med att hålla kupan varm genom att klumpa ihop sig, särskilt viktigt under kallare perioder. Vidare deltar de i att ventilera kupan genom att vifta med vingarna vid ingången för att reglera temperatur och fuktighet.

När arbetsbiet blir lite äldre, vanligtvis efter den första veckan, övergår dess uppgifter till andra sysslor inom kupan. De kan börja producera vax från vaxkörtlar på undersidan av sina bakkroppar. Detta vax används för att bygga och reparera vaxkakorna, där honung och pollen lagras och där ägg läggs. Vid denna ålder kan de också ta emot nektar och pollen från de äldre fältbina, bearbeta nektarn till honung genom att tillsätta enzymer och ventilera bort fukt, samt lagra pollen i celler för att användas som "bibröd". De fungerar även som vakter vid kupans ingång för att skydda mot inkräktare som getingar eller andra bin.

De äldsta arbetsbina, ofta de sista 1-2 veckorna av sitt liv under högsäsong, blir "fältbin". Deras uppgift är att lämna kupan för att samla nektar och pollen från blommor. Detta är det mest krävande och riskfyllda jobbet, då de utsätts för rovdjur, väder och navigeringssvårigheter. Nektar samlas i honungsblåsan för att transporteras tillbaka till kupan, medan pollen samlas i "pollenkorgar" på bakbenen. Fältbin spelar en avgörande roll i pollineringen av växter när de flyger från blomma till blomma. Deras liv är kort men oerhört intensivt, präglat av konstant arbete tills vingarna är för slitna för att flyga, varefter de dör utanför kupan. Arbetsbinas kollektiva och organiserade arbete är en imponerande demonstration av socialt beteende och är fundamental för bisamhällets existens.
""",
    "dronare.md": """
# Drönarnas Roll i Bikupan

Drönarna, hanbina i ett bisamhälle, har en roll som ofta missförstås och underskattas. Till skillnad från de ständigt arbetande honorna (drottningen och arbetsbina), är drönarnas existens till synes mer avslappnad. De har ingen gadd (vilket innebär att de inte kan stickas), samlar varken nektar eller pollen, producerar inte vax, och deltar inte i kupans rengöring eller omvårdnad av larver. Deras enda egentliga uppgift är att para sig med en ung, obefruktad drottning.

Drönare utvecklas från obefruktade ägg. Detta innebär att de endast har kromosomer från drottningen, deras mor. De är alltså haploida. Deras livscykel är något längre än arbetsbinas, och de tar längre tid på sig att utvecklas från ägg till vuxet bi. Drönarcellerna i vaxkakan är också större än arbetsbienes celler, vilket resulterar i att drönarna är större och kraftigare byggda än arbetsbina. De har också mycket stora ögon, vilket tros hjälpa dem att lokalisera drottningar under parningsflykten.

Större delen av tiden tillbringar drönarna med att bara äta den honung som arbetsbina har samlat, och att vänta. De kan ses vandra runt i kupan, äta direkt från honungsceller, och emellanåt putsa sig. Deras passivitet i kupans dagliga sysslor gör att de ibland ses som en "börda" på samhällets resurser, särskilt under perioder med låg nektartillgång.

Drönarnas viktiga ögonblick kommer under de så kallade "drönarsamlingsplatserna". Detta är specifika geografiska områden, ofta på hög höjd, dit drönare från många olika bikupor i området samlas. Unga, obefruktade drottningar flyger också till dessa platser för att para sig. Parningen sker i luften. En drottning parar sig vanligtvis med flera drönare under en enda eller några få parningsflygningar. För drönaren är parningen en slutpunkt – dess endofallus (parningsorgan) fastnar i drottningen och slits loss från drönarens kropp, vilket leder till att drönaren dör strax därefter.

Efter parningssäsongen på sensommaren eller hösten, när behovet av parning upphör, har drönarna spelat ut sin roll. Arbetsbina tolererar inte längre drönarnas närvaro som konsumenter av kupans matförråd inför vintern. De slutar mata drönarna och kan till och med driva ut dem ur kupan för att svälta eller frysa ihjäl. Denna till synes brutala utvisning är en nödvändig del av bisamhällets överlevnadsstrategi inför knappare tider. Trots sin korta och till synes begränsade roll är drönarna helt avgörande för binas fortplantning och för att säkra den genetiska mångfalden inom arten, då drottningar parar sig med drönare från många olika samhällen.
""",
    "vaggdansen.md": """
# Biets Kommunikation: Vaggdansen

Binas förmåga att kommunicera effektivt är en av de mest imponerande aspekterna av deras komplexa sociala liv. Ett av de mest kända exemplen på denna kommunikation är den så kallade vaggdansen, en ritualiserad rörelsesekvens som utförs av fältbin som återvänder till kupan efter att ha funnit en bra källa till nektar, pollen eller vatten. Genom denna dans kan biet förmedla information till sina kamrater om var resursen finns, hur långt bort den är, och vilken kvalitet den har.

Vaggdansen utförs inne i den mörka bikupan, vanligtvis på en vertikal vaxkaka. Andra bin samlas runt dansaren och följer dess rörelser med sina antenner, kännande av vibrationerna och luftströmmarna. Dansen består av två huvudfaser: en "vaggningsfas" och en "återgångsfas". Under vaggningsfasen rör sig biet rakt fram medan det vibrerar kraftigt med sin bakkropp – därav namnet "vaggdans". Efter denna raka rörelse går biet i en båge tillbaka till startpunkten, utför en ny rak vaggningsfas, och går sedan i en båge åt andra hållet tillbaka till startpunkten. Mönstret blir alltså en serie raka linjer avbrutna av alternerande cirkelbågar, bildande en figur som liknar en "åtta".

Riktningen på resursen i förhållande till bikupan kommuniceras av vinkeln på den raka vaggningsfasen i relation till gravitationen (vertikalt nedåt på den vertikala kakan). Om den raka dansen går rakt upp, betyder det att resursen finns rakt mot solen. Om den går rakt ner, är resursen i motsatt riktning från solen. Om den raka dansen har en vinkel på 30 grader till vänster om vertikalt uppåt, betyder det att resursen finns 30 grader till vänster om solen. Bin har en förmåga att kompensera för solens rörelse över himlen, vilket gör att de kan ge korrekt riktningsinformation även om solen rört sig under tiden biet var ute och flög.

Avståndet till resursen kommuniceras av längden på den raka vaggningsfasen och hastigheten på dansen. En längre och långsammare vaggningsfas indikerar ett längre avstånd, medan en kortare och snabbare dans signalerar att källan är närmare. Biet kan också förmedla information om resursens kvalitet; ju mer intensiv och långvarig dansen är, desto bättre är källan. Dessutom, genom att ge bort små smakprov av den insamlade nektarn eller pollen till de bin som följer dansen, kan biet också förmedla information om doften av blommorna.

Vaggdansen är ett anmärkningsvärt exempel på hur djur kan använda symboliska kommunikation för att förmedla komplex information om omvärlden. Forskning har visat att bin som "läser" vaggdansen sedan framgångsrikt kan hitta de resurser som dansaren har signalerat, vilket bevisar dansens effektivitet som ett kommunikationsmedel inom bisamhället. Denna komplexa form av kommunikation är avgörande för samhällets förmåga att effektivt utnyttja tillgängliga födoresurser i omgivningen.
""",
    "hot_mot_bin.md": """
# Hot mot Bin

Bin, både honungsbin och vilda pollinatörer som humlor och solitärbin, står inför en rad allvarliga hot världen över. Dessa hot bidrar till en oroväckande nedgång i bi-populationer, vilket inte bara påverkar den biologiska mångfalden utan även vår livsmedelsproduktion, eftersom bin pollinerar en stor del av de grödor vi är beroende av. Förståelse för dessa hot är det första steget mot att skydda dessa ovärderliga insekter.

Ett av de mest betydande hoten är användningen av pesticider, särskilt neonikotinoider, inom jordbruket. Dessa bekämpningsmedel är utformade för att döda skadeinsekter, men de kan också vara extremt giftiga för bin, även i låga doser. Exponering kan leda till förvirring, nedsatt navigeringsförmåga, försvagat immunsystem och i värsta fall död. Även subletala doser kan påverka bisamhällets hälsa och produktivitet negativt. Vissa länder och regioner har infört restriktioner eller förbud mot vissa typer av neonikotinoider, men utmaningen kvarstår.

Förlust och fragmentering av livsmiljöer är ett annat stort problem. Urbanisering, intensivt jordbruk och avskogning minskar tillgången på de blommor som bin behöver för nektar och pollen, samt platser för att bygga bon. Monokulturer inom jordbruket, där stora områden odlas med en enda gröda, minskar också den biologiska mångfalden av föda för bin under stora delar av året. Bin behöver en varierad kost från olika blommor under hela säsongen för att vara friska. När deras naturliga habitat försvinner, minskar deras överlevnadschanser dramatiskt.

Sjukdomar och parasiter utgör också allvarliga hot. Varroakvalstret (Varroa destructor) är en parasit som angriper honungsbin och sprider virus som försvagar både individuella bin och hela bisamhällen. Kvalstret är en global plåga för biodlare. Andra sjukdomar, som amerikansk yngelröta och europeisk yngelröta, kan snabbt sprida sig i en kupa och kräva drastiska åtgärder som att bränna infekterade samhällen för att förhindra spridning. Dessutom påverkas bin av virus och svampar som kan försvaga dem.

Klimatförändringar bidrar också till bins svårigheter. Ändrade temperaturer och nederbördsmönster kan påverka när blommor blommar, vilket kan leda till att binas livscykel blir osynkroniserad med tillgången på föda. Extremväder, som långvarig torka eller kraftiga regn, kan direkt skada bin eller minska blomningen. Introduktion av invasiva arter, både växter som konkurrerar med inhemska blommor och insekter som attackerar bin (t.ex. asiatisk geting), är ytterligare hot. Att tackla dessa komplexa hot kräver samordnade insatser från regeringar, jordbrukare, biodlare och allmänheten för att skapa en mer bi-vänlig miljö.
""",
    "olika_biarter_sverige.md": """
# Olika Bi-arter i Sverige

När man talar om bin tänker många först på honungsbiet (Apis mellifera), det sociala bi som hålls av biodlare för produktion av honung och pollinering av grödor. Men Sverige hyser en mycket större och mer diversifierad grupp av bin än så. Utöver honungsbiet finns det hundratals olika arter av vildbin, inklusive de välkända humlorna och en stor variation av solitärbin. Dessa vildbin är otroligt viktiga pollinatörer och spelar en avgörande roll i våra naturliga ekosystem och för vilda växters fortplantning.

Honungsbiet, även om det är det mest kända, är inte ursprungligt i Sverige utan introducerades av människan. De lever i stora, permanenta samhällen, oftast i konstgjorda bikupor, och deras sociala struktur är högt utvecklad med en drottning, tusentals arbetsbin och drönare. De är generalister när det gäller föda och pollinerar en mängd olika blommor, men de har också specifika krav på sina levnadsmiljöer och är beroende av biodlares skötsel för att överleva, särskilt under vintern.

Humlor (Bombus spp.) är kanske de mest älskade av våra vildbin. De är större, luddigare och ofta mer tåliga mot kyla än honungsbin. Detta gör dem till effektiva pollinatörer även under kyligare väder och tidigt på våren eller sent på hösten när honungsbina är mindre aktiva. Humlor lever i mindre samhällen än honungsbin, oftast under ettåriga cykler där bara den befruktade drottningen övervintrar och grundar ett nytt bo på våren. Det finns många olika humlearter i Sverige, varav vissa är specialiserade på att pollinera specifika växter. Tyvärr är flera humlearter hotade.

Solitärbin utgör den absolut största gruppen av bin i Sverige, med flera hundra olika arter. Till skillnad från honungsbin och humlor lever solitärbin inte i samhällen. Varje hona är fertil och bygger sitt eget bo, där hon samlar föda och lägger ägg. Bona kan byggas på en mängd olika platser: i håligheter i trä, i marken, i ihåliga stjälkar eller under stenar. Solitärbin är ofta mer specialiserade än honungsbin och humlor, vilket innebär att vissa arter enbart pollinerar en specifik typ av blomma. Denna specialisering gör dem särskilt sårbara om deras specifika värdväxt försvinner. Exempel på solitärbin är murarbin, sandbin och tapetserarbin.

Skyddet av vildbin är avgörande för att bevara vår biologiska mångfald. De bidrar till pollineringen av vilda växter, vilket i sin tur stödjer hela ekosystem. Genom att skapa blommande miljöer, undvika pesticider och erbjuda boplatser kan vi hjälpa dessa viktiga pollinatörer att överleva och frodas.
""",
    "biodling_hobby.md": """
# Biodling som Hobby

Biodling har blivit en alltmer populär hobby, driven av en önskan att bidra till pollineringen, producera egen honung eller helt enkelt fascinationen för bisamhällets komplexa liv. Att börja med biodling kräver engagemang, kunskap och en vilja att lära sig, men belöningarna i form av naturupplevelse och den söta honungen kan vara stora. Det är dock viktigt att närma sig biodling med respekt för bina och en förståelse för ansvaret det innebär.

Det första steget för en blivande biodlare är att skaffa sig kunskap. Kurser arrangeras av biodlareföreningar över hela landet och ger en grundläggande förståelse för binas biologi, skötsel under olika årstider, sjukdomar och skadedjur samt lagar och regler kring biodling. Att läsa böcker och besöka erfarna biodlare är också ovärderligt. Man behöver lära sig om bisamhällets dynamik, hur man hanterar bin säkert, och hur man upptäcker tecken på problem i kupan.

Utrustning är en annan viktig investering. Man behöver minst en bikupa (ofta börjar man med två eller tre för att ha reservdelar och möjligheten att jämföra samhällen), skyddsutrustning som bidräkt, slöja och handskar, verktyg som kupkniv och rökpust, samt utrustning för honungshantering som en honungsslunga (kan ofta lånas eller hyras initialt) och kärl för lagring. Placeringen av kupan är också viktig; en solig, vindskyddad plats med tillgång till dragväxter (blommor som ger nektar och pollen) och vatten är idealisk.

Att skaffa bin kan göras på flera sätt. Man kan köpa en avläggare (en liten grupp bin med en drottning från en befintlig kupa), en svärm (om man har tur och hittar en), eller paketbin (bin utan kupa som levereras i en låda med en parad drottning). Det är viktigt att köpa bin från en pålitlig källa för att minimera risken att introducera sjukdomar.

Under säsongen, från vår till höst, kräver biodling regelbunden tillsyn. Man behöver kontrollera samhällets hälsa, se att drottningen lägger ägg, bedöma foderläget, utöka kupan vid behov för att förhindra svärmning, och behandla mot varroakvalster. Honung skördas vanligtvis på sommaren när bin har samlat ett överskott. På hösten förbereds samhället för vintern genom att säkerställa att de har tillräckligt med vinterfoder (ofta sockerlösning) och att kupan är skyddad mot kyla och fukt.

Biodling är en givande men ansvarsfull hobby. Den ger en djupare koppling till naturen och insikt i ett fantastiskt insekts liv. Genom att sprida kunskap och uppmuntra fler att starta biodling kan vi tillsammans bidra till att stärka bi-populationerna och öka pollineringen i våra landskap.
""",
    "bins_roll_ekosystemet.md": """
# Bins Roll i Ekosystemet

Bin är fundamentalt viktiga för jordens ekosystem. Deras mest kända och kritiska funktion är pollinering – processen där pollen överförs från en blomma till en annan, vilket möjliggör befruktning och frösättning hos växter. Utan bin och andra pollinatörer skulle många av de vilda växter som utgör grunden för ekosystemens näringsvävar inte kunna fortplanta sig. Detta skulle leda till en kaskadeffekt med minskad växtlighet, färre frön och bär som föda för djur, och i förlängningen en minskad biologisk mångfald.

Pollinering är inte bara avgörande för vilda växter, utan även för en mycket stor del av mänsklighetens livsmedelsproduktion. Uppskattningsvis pollinerar bin (både honungsbin och vildbin) omkring en tredjedel av all mat vi äter. Detta inkluderar en mängd frukter, grönsaker, nötter, frön och foderväxter för boskap. Exempel på grödor som är starkt beroende av pollinering inkluderar äpplen, blåbär, mandlar, kaffe, kakao och många oljeväxter. Utan bin skulle skördarna av dessa grödor minska dramatiskt, vilket skulle påverka livsmedelssäkerheten och ekonomin globalt.

Bin fungerar som en viktig länk mellan växter och andra djur i ekosystemet. Genom att pollinerar växter säkerställer de produktionen av frukter och frön, som i sin tur utgör föda för fåglar, däggdjur och insekter. Binas egna insamlade resurser – nektar och pollen – är också föda för andra insekter och spindeldjur. Deras bon och larver kan utgöra föda för rovdjur som fåglar. Binas närvaro och aktivitet kan därmed vara en indikator på ekosystemets hälsa.

Dessutom bidrar bin till den genetiska mångfalden hos växter genom att flytta pollen mellan olika plantor. Detta är viktigt för växternas förmåga att anpassa sig till förändrade miljöförhållanden och motstå sjukdomar. Olika biarter har ofta specialiserade relationer med specifika växter, vilket innebär att förlusten av en specifik biart kan leda till att en eller flera växtarter också försvinner om de är beroende av just det biet för pollinering.

Den ekologiska tjänst som bin utför genom pollinering är ovärderlig och svår att ersätta i stor skala. Robotar och manuell pollinering har testats, men ingen metod är lika effektiv, skalbar och kostnadseffektiv som binas naturliga arbete. Att skydda bin och deras livsmiljöer är därför inte bara viktigt för bina själva, utan en fundamental förutsättning för att upprätthålla friska ekosystem och säkerställa vår egen framtida livsmedelsförsörjning. Insatser för att bevara bin är insatser för att bevara den biologiska mångfalden och naturens funktion.
""",
    "bin_i_staden.md": """
# Bin i Staden: Urban Biodling och Vilda Bin

Staden, med sina parker, trädgårdar, balkonger och grönområden, erbjuder ofta oväntade möjligheter för bin, både tama honungsbin och vilda solitärbin och humlor. I många urbana miljöer kan bin till och med hitta en mer varierad och mindre pesticidbelastad föda än på landsbygden där monokulturer dominerar. Urban biodling har blivit en växande trend, samtidigt som insatser för att gynna vilda bin i staden ökar.

Urban biodling innebär att man håller bikupor i stadsmiljö, ofta på tak, i parker eller på koloniområden. Städer kan erbjuda en lång och varierad blomningssäsong tack vare mångfalden av trädgårdsväxter, parkplanteringar och blommande träd och buskar. Detta kan ge goda förutsättningar för bisamhällenas tillväxt och honungsproduktion. Honungen från stadsmiljöer kan ofta ha en unik smakprofil beroende på de dominerande växterna i området. Att ha bin nära ger också en konkret koppling till naturen för stadsbor och ökar medvetenheten om pollinatörernas betydelse.

Utöver honungsbin hittar även vilda bin en plats i staden. Humlor kan bygga bon i gamla mus- eller fågelbon, i komposter eller under skjul. Solitärbin kan utnyttja håligheter i tegelväggar, gammalt trä, eller bygga bon i sandig jord. Stadens grönområden, även små sådana som rabatter och krukor på balkonger, kan erbjuda nödvändig föda i form av nektar och pollen.

För att gynna bin i staden kan flera åtgärder vidtas. Enskilda medborgare kan välja att plantera bivänliga växter i sina trädgårdar, på balkonger och fönsterbrädor. Växter som lavendel, timjan, ringblommor, gurkört och solrosor är populära bland bin. Att låta gräsmattor blomma ut istället för att ständigt klippa dem skapar också viktiga födokällor. Att minska eller helt undvika användning av pesticider i stadsmiljö är avgörande.

Kommuner och fastighetsägare kan bidra genom att anlägga bivänliga planteringar i parker och längs gator, skapa ängsmarker i stället för kortklippta gräsmattor, och sätta upp insektshotell eller sandbäddar för solitärbin. Vattenspeglar eller grunda vattenkällor är också viktiga, eftersom bin behöver dricka. Utbildningsinsatser kan öka allmänhetens förståelse för binas behov och minska rädsla för stick.

Bin i staden visar att naturen kan blomstra även i tätbebyggda områden om vi ger den utrymme och rätt förutsättningar. Urban biodling och insatser för vilda bin bidrar inte bara till pollinering av stadens växtliv och ökade skördar i urbana odlingar, utan också till att öka den biologiska mångfalden och skapa grönare, mer levande stadsmiljöer för alla.
""",
    "honungsskord_hantering.md": """
# Honungsskörd och Hantering

Att skörda honung är en av biodlarens mest givande sysslor, resultatet av binas outtröttliga arbete att samla nektar och omvandla den till detta gyllene, söta livsmedel. Processen kräver noggrannhet och hygien för att säkerställa att honungen blir av hög kvalitet och fri från föroreningar. Honung skördas vanligtvis när vaxkakorna är fyllda med honung och bin har förseglat cellerna med ett tunt lager vaxlock, vilket indikerar att honungen har rätt fuktighetshalt.

Först behöver biodlaren öppna bikupan försiktigt. Detta görs bäst under lugna förhållanden när de flesta bin är ute och samlar, ofta mitt på dagen. En rökpust används för att lugna bina; röken maskerar binas alarmsignaler och gör dem mindre benägna att stickas. Biodlaren tar sedan ut de ramar som är fyllda med honung. Man använder en mjuk borste eller bi-blås för att avlägsna bin från ramarna innan de tas bort från kupan. Det är viktigt att endast skörda överskottshonung som bina inte behöver för eget bruk, särskilt inför vintern då de är helt beroende av sina lagrade reserver.

Nästa steg är att "avliva" ramarna, vilket innebär att ta bort de vaxlock som bin har satt över honungscellerna. Detta görs med en speciell avlivningsgaffel eller en uppvärmd kniv. Vaxlocket är rent bivax och kan sparas och användas till vaxprodukter. När vaxlocken är borta är honungen exponerad i cellerna och redo att extraheras.

Extraktionen sker oftast med hjälp av en honungsslunga. En slunga är en centrifugalmaskin där ramarna placeras. Genom att snurra ramarna tvingas honungen ut ur cellerna av centrifugalkraften och samlas längs slungans sidor, varifrån den rinner ner till botten och ut genom en tappkran. Detta är en skonsam metod som gör att vaxkakorna förblir intakta och kan återanvändas av bina. Mindre mängder honung kan också skördas genom att krossa vaxkakorna och låta honungen rinna av, men detta förstör kakorna.

Efter att honungen har slungats, behöver den silas för att avlägsna vaxrester, bi-delar och andra orenheter. Detta görs med silar av olika finhetsgrad. Den silade honungen hälls sedan i kärl för sedimentering, där eventuella kvarvarande partiklar och luftbubblor stiger till ytan. Efter några dagar kan honungen tappas på burkar. Honung bör förvaras mörkt och svalt. Med tiden kan honung kristalliseras, vilket är en naturlig process och ett tecken på att honungen är naturlig och av god kvalitet. Den kan enkelt återställas till flytande form genom försiktig uppvärmning i ett vattenbad. Korrekt skörd och hantering säkerställer en ren och smakrik honung redo att avnjutas.
""",
    "bin_blommor_symbios.md": """
# Bin och Blommor: Ett Symbiotiskt Förhållande

Relationen mellan bin och blommor är ett klassiskt exempel på symbios – ett ömsesidigt fördelaktigt förhållande där båda parter drar nytta. För blomman är biet en oumbärlig budbärare som överför pollen, vilket är nödvändigt för dess fortplantning. För biet är blomman en livsviktig källa till föda i form av nektar och pollen. Detta samspel har utvecklats över miljontals år och har format både binas och blommornas egenskaper.

Blommor har utvecklat en mängd olika strategier för att attrahera bin och andra pollinatörer. De producerar lockande dofter, har färgglada kronblad som fungerar som visuella signaler (ofta med mönster synliga i ultraviolett ljus som bin kan se men inte människor), och erbjuder belöningar i form av nektar och pollen. Nektar är en sockerrik vätska som ger bin energi (kolhydrater), medan pollen är rikt på protein, fett, vitaminer och mineraler – avgörande för larvernas tillväxt och bins hälsa. Vissa blommor har även särskilda strukturer eller mekanismer som säkerställer att pollen fastnar på biet när det besöker blomman.

Bin har i sin tur anpassat sig för att vara effektiva pollinatörer och födosamlare. De har specialiserade kroppsdelar för att samla och transportera pollen, som till exempel pollenkorgarna på bakbenen hos honungsbin och humlor, eller täta hår på kroppen där pollen fastnar hos solitärbin. Deras munpartier är anpassade för att suga upp nektar. Binas beteende, som deras trohet till en specifik blomart under en födosamlingstur (så kallad "blomtrohet"), ökar effektiviteten i pollineringen genom att pollen från en art förs till en annan blomma av samma art.

Vissa bi- och blomarter har utvecklat mycket specifika och exklusiva relationer. Vissa solitärbin kan till exempel enbart samla pollen från en enda växtart, eller en liten grupp av närbesläktade arter. Dessa specialiserade bin är extremt effektiva pollinatörer för just dessa växter, men är också mycket sårbara om deras specifika värdväxt försvinner från landskapet. Detta understryker vikten av biologisk mångfald – en variation av både biarter och blomarter säkerställer ett robustare ekosystem.

Förändringar i klimat och markanvändning som påverkar blomningstider eller tillgången på specifika blommor kan störa denna känsliga symbios och negativt påverka både bi-populationer och de växter de pollinerar. Att förstå och skydda den komplexa relationen mellan bin och blommor är därför centralt för att bevara biologisk mångfald och säkerställa de ekosystemtjänster som vi är beroende av. Att plantera en mångfald av inhemska, bivänliga växter är ett av de bästa sätten att stödja denna livsviktiga relation.
""",
    "bisamhallets_organisation.md": """
# Bisamhällets Organisation och Superorganismen

Ett bisamhälle är mycket mer än bara en samling individer; det är ett av de mest studerade och fascinerande exemplen på en superorganism. Inom vetenskapen används begreppet superorganism för att beskriva en social enhet, som ett bisamhälle eller en myrstack, där de enskilda individerna (bina) fungerar mer som celler i en större kropp. Samhället som helhet uppvisar egenskaper och beteenden som går långt utöver vad en enskild bi kan göra, och det agerar kollektivt för samhällets överlevnad och fortplantning snarare än för individuella bins reproduktion (med undantag för drottningen och tillfälligt drönarna).

Kärnan i superorganismen är den strikta sociala hierarkin och arbetsfördelningen. Samhället består av tre kaster: en drottning, tusentals arbetsbin och säsongsvis drönare. Drottningens roll är nästan uteslutande reproduktion; hon är samhällets enda äggläggare. Arbetsbin, som alla är sterila honor, utför i princip allt annat arbete: sköter om drottningen, matar larver, bygger vaxkakor, rengör kupan, vaktar ingången, och samlar föda (nektar, pollen, vatten, propolis). Deras uppgifter skiftar vanligtvis med ålder, från inre sysslor som sköterskor till yttre som fältbin. Drönarnas enda uppgift är att para sig med en ny drottning under parningsflykten.

Kommunikation är central för superorganismens funktion. Bin använder komplexa system av kemiska signaler (feromoner), fysiska interaktioner och rörelser (som vaggdansen) för att koordinera aktiviteter. Drottningens feromon är särskilt viktigt för att upprätthålla samhällets sammanhållning och hämma arbetsbinas fortplantningsförmåga. Feromoner signalerar också samhällets tillstånd och behov, t.ex. när det är dags att föda upp en ny drottning eller svärma.

Beslutsfattande i bisamhället är ofta en kollektiv process. När det är dags att svärma och hitta ett nytt hem, skickar arbetsbin ut spanare för att söka efter lämpliga boplatser. Spanarbin som hittar en bra plats återvänder till svärmen och utför en vaggdans på svärmens yta för att kommunicera platsens kvalitet och riktning. Ju bättre plats, desto mer intensiv dans. Andra bin inspekterar platserna och kan börja "rösta" på sin favoritplats genom att också dansa för den. När tillräckligt många bin "röstar" på samma plats, nås en konsensus och hela svärmen flyger dit. Detta är ett elegant exempel på distribuerat, kollektivt beslutsfattande.

Som superorganism reglerar samhället kollektivt sin inre miljö, som temperatur och fuktighet i kupan, och fattar beslut om när och var föda ska samlas eller när en ny drottning ska födas upp. Den enskilda bies liv och död är mindre viktigt än superorganismens fortlevnad och reproduktion (svärmning). Att studera bisamhället som en superorganism ger djupa insikter i hur komplexa system kan organisera sig och fatta beslut utan centraliserad kontroll, ett koncept med relevans även inom andra områden som robotik och datavetenskap.
""",
    "olika_typer_honung.md": """
# Olika Typer av Honung och Deras Egenskaper

Honung är inte bara honung. Smak, färg, arom och konsistens varierar stort beroende på vilka blommor bin har samlat nektar från. Biodlare och honungskännare pratar om "sortshonung" när majoriteten av nektaren kommer från en specifik växtart, vilket ger honungen dess karakteristiska egenskaper. Att lära sig känna igen olika honungstyper är en del av upplevelsen med denna naturliga produkt.

Färgen på honung kan variera från nästan helt genomskinlig till mörkt bärnstensfärgad eller till och med nästan svart. Generellt sett tenderar ljus honung att ha en mildare smak, medan mörkare honung ofta är mer robust och smakrik. Färgen påverkas av de mineraler och pigment som finns i nektarn från olika växter. Exempelvis ger akacianektar en mycket ljus honung, medan ljungnektar ger en mörkare, mer bärnstensfärgad honung.

Smaken är den mest framträdande egenskapen som skiljer olika honungstyper åt. Smakprofilen kan vara söt, syrlig, bitter, nötig, fruktig, blommig, kryddig eller maltig, beroende på nektarkällan. Vissa honungar har en ren, söt smak (t.ex. klöverhonung), medan andra har komplexa smaknyanser (t.ex. bovetehonung med en robust, maltig smak). Ljunghonung är känd för sin kraftiga, lite bittra och aromatiska smak, och den har en geléaktig konsistens som kräver speciell hantering vid slungning. Raps- och klöverhonung kristalliseras sig snabbt och blir vita och krämiga, medan akacia- och maskroshonung tenderar att förbli flytande längre.

Aromen är också en viktig egenskap. Honungens doft reflekterar de flyktiga ämnena i nektarn. En honung kan dofta subtilt av blommor, intensivt av örter, eller ha en distinkt, nästan medicinsk doft som ljunghonung. Att dofta på honungen innan man smakar ger ofta en god indikation på dess karaktär.

Konsistensen kan vara flytande, trögflytande, krämig eller hård kristalliserad. Alla honungar kristalliserar sig med tiden, men hastigheten och kornigheten varierar beroende på förhållandet mellan fruktsocker (fruktos) och druvsocker (glukos) i nektarn. Honung med hög frukoshalt kristalliserar långsammare än honung med hög glukoshalt. Kontrollerad kristallisation genom ympning (tillsätta en liten mängd finkristallin honung) och omrörning kan ge en mjuk, krämig konsistens som är populär.

Att uppskatta olika typer av honung är som att utforska vinets eller kaffets värld – varje sort berättar en historia om landskapet och blommorna bina har besökt. Att provsmaka och jämföra honung från olika källor ger en djupare förståelse för biets arbete och naturens mångfald.
""",
    "bin_historia_kultur.md": """
# Bin i Historien, Myter och Kulturen

Bin har fascinerat människan i tusentals år och har en rik historia och djupgående betydelse i kulturer världen över. Långt innan modern biodling utvecklades har människor samlat honung och bivax från vilda bisamhällen. Bevis på detta finns i grottmålningar som är upp till 15 000 år gamla, vilka avbildar människor som skördar honung. De gamla egyptierna var tidiga mästare på biodling, och bin och honung hade en viktig roll i deras religion, medicin och som sötningsmedel. Honung användes även som betalningsmedel och i balsamering.

I antikens Grekland och Rom fortsatte biodlingen att utvecklas. Grekerna använde olika typer av kupor, inklusive liggande krukor och flätade korgar, och hade en god förståelse för bisamhällets organisation (även om de inte helt förstod drottningens roll, som de ibland trodde var en kung). Romarna beskrev biodling i detalj i jordbrukslitteratur. Både grekerna och romarna värderade högt honung och vax.

Under medeltiden i Europa blev biodling, särskilt vaxproduktionen, mycket viktig. Bivax var nödvändigt för kyrkliga ljus, som användes i stor utsträckning. Kloster var ofta centrum för biodlingskunskap. Bönder höll bin i enkla halmkupor (skepor) eller ihåliga trästockar. Skörden innebar ofta att hela samhället fick offras.

En revolution inom biodlingen skedde på 1800-talet med uppfinningen av den flyttbara ramen. Amerikanen L.L. Langstroth patenterade den första praktiskt användbara bikupan med flyttbara ramar 1852. Denna uppfinning bygger på upptäckten av det "birummet" – ett specifikt avstånd (ca 6-9 mm) som bin varken bygger igen med vax eller propolis. Genom att konstruera ramar med detta avstånd kunde biodlare inspektera samhället, skörda honung och hantera sjukdomar utan att förstöra vaxkakorna eller stressa bina i onödan. Detta möjliggjorde modern, storskalig biodling och ledde till snabb utveckling av teknik och kunskap.

Sedan Langstroths tid har biodlingstekniken fortsatt att förfinas, med nya kupmodeller, metoder för drottningodling, sjukdomsbekämpning och utrustning för honungshantering. Idag är biodling en global verksamhet, från småskaliga hobbybiodlare till stora kommersiella företag, som spelar en avgörande roll för både honungsproduktion och, allt viktigare, för pollineringen av jordbruksgrödor världen över. Biodlingens historia är en spegel av mänsklighetens långa och nära relation till naturen och dessa fantastiska insekter.
""",
    "bin_vader_aktivitet.md": """
# Bin och Väder: Hur Påverkas Binas Aktivitet?

Väderförhållanden har en direkt och betydande inverkan på bins aktivitet, särskilt på fältbinas förmåga att samla föda. Temperatur, nederbörd, vind och solljus spelar alla roller i hur, när och om bin kan lämna kupan för att pollinera och samla nektar och pollen. För biodlare är det viktigt att förstå dessa samband för att kunna bedöma samhällets tillstånd och behov.

Temperatur är en av de mest kritiska faktorerna. Honungsbin blir vanligtvis aktiva när temperaturen överstiger cirka 10-12 grader Celsius. Under denna tröskel är de mer benägna att stanna i kupan för att spara energi och upprätthålla värmen. Vissa vildbin, som humlor, är mer köldtåliga och kan vara aktiva vid lägre temperaturer. För höga temperaturer kan också vara problematiskt; vid extrem hetta kan bin ägna mer tid åt att hämta vatten för att kyla kupan genom avdunstning istället för att samla nektar, och överhettning kan vara farligt för dem.

Nederbörd, särskilt kraftigt regn, hindrar bin från att flyga. Regndroppar kan vara för stora och tunga för bin att navigera i, och de kan skada deras vingar. Lätt duggregn eller fuktig luft kan dock tolereras i viss utsträckning. Långvariga regnperioder kan leda till att bin blir instängda i kupan, vilket kan orsaka brist på färsk föda och stress i samhället. Efter regn kan blommorna också ha sköljts rena från nektar och pollen.

Vind påverkar också bins flygförmåga och navigeringsprecision. Kraftig vind gör det svårt för bin att flyga rakt, kan blåsa bort dem från sin kurs och ökar energiförbrukningen. Bin föredrar att flyga i relativt lugna förhållanden. Vind kan också påverka blommors nektarproduktion och pollenutsläpp.

Solljus är viktigt för bins orientering. Honungsbin använder solens position, även när den är dold bakom moln, som en del av sitt navigeringssystem (kompassriktning). Molnigt väder kan därför göra navigeringen svårare. Solljus påverkar också blommorna och deras produktion av nektar, vilken ofta är högre under soliga förhållanden.

Klimatförändringar med mer extrema väderhändelser och oförutsägbara säsonger utgör ett växande hot för bin, eftersom de kan störa den känsliga synkroniseringen mellan biets livscykel och tillgången på blommor. En mild vinter följd av en plötslig köldknäpp på våren kan vara förödande om bina redan har börjat föda upp yngel och det inte finns tillräckligt med föda ute. Förståelsen för hur väder påverkar bin är avgörande för biodlare och för att kunna skapa strategier för att mildra klimatförändringarnas effekter på pollinatörer.
""",
    "drottningens_parningsflykt.md": """
# Drottningens Livsfarliga Parningsflykt

Drottningens parningsflykt är en kritisk och farlig fas i hennes liv, helt avgörande för bisamhällets framtid. Det är den enda gången i sitt liv, bortsett från eventuell svärmning, som en ung drottning lämnar bikupan för att para sig. Denna flygning sker vanligtvis några dagar till en vecka efter att hon kläckts. Syftet är att möta drönare från andra samhällen och samla tillräckligt med spermier för att kunna befrukta ägg under resten av sitt liv.

Parningsflykten sker under gynnsamma väderförhållanden – oftast soligt, varmt och vindstilla. Drottningen navigerar till specifika områden som kallas drönarsamlingsplatser. Dessa platser är ofta lokaliserade på samma platser år efter år och fungerar som mötesplatser för drönare från många olika bikupor i ett stort område. Exakt hur drönarsamlingsplatserna etableras och hur bin navigerar till dem är fortfarande föremål för forskning, men det tros involvera visuella landmärken och feromonspår.

När drottningen anländer till drönarsamlingsplatsen, lockar hon till sig drönare med hjälp av ett kraftfullt sexualferomon. Hundratals eller till och med tusentals drönare kan samlas runt henne i luften. Parningen sker i hög hastighet under flykt. Drottningen parar sig inte bara med en enda drönare, utan med mellan 10 och 20 olika drönare under en eller flera parningsflygningar. Denna multi-parning (polyandri) är evolutionärt viktig; den säkerställer att drottningen får en stor och genetiskt diversifierad uppsättning spermier att lagra i sin spermathek (sädesbehållare). Genetisk variation inom bisamhället gör det mer motståndskraftigt mot sjukdomar och bättre anpassat till olika födokällor och miljöförhållanden.

För drönaren är parningen en dödsdom. Efter att ha överfört spermier till drottningen fastnar drönarens endofallus i drottningens könsorgan och slits loss från drönarens kropp när de separeras. Drönaren faller då till marken och dör. Trots detta offer är drönarens instinkt att para sig överväldigande, driven av fortplantningsbehovet på samhällsnivå.

Parningsflykten är riskfylld för drottningen. Hon är utsatt för rovdjur som fåglar och sländor under flykten. Om vädret plötsligt försämras kan hon ha svårt att hitta tillbaka till kupan. Om hon inte lyckas para sig med tillräckligt många drönare, eller om spermierna inte är livskraftiga, kommer hon inte att kunna lägga befruktade ägg, och bisamhället kommer att dö ut eller tvingas föda upp en ny drottning. Efter framgångsrik parning återvänder drottningen till kupan, nu full av spermier för resten av sitt liv, och påbörjar sin livslånga karriär som äggläggare. Hennes lyckade parningsflykt är ett ögonblick av yttersta vikt för samhällets fortbestånd.
""",
    "binas_naturliga_fiender.md": """
# Binas Naturliga Fiender

Utöver sjukdomar och parasiter som varroakvalstret, har bin en rad naturliga fiender i form av rovdjur (predatorer) och andra insekter. Dessa fiender kan utgöra hot mot både enskilda bin och hela bisamhällen, även om friska och starka samhällen oftast kan försvara sig effektivt mot många hot.

Fåglar är en vanlig fiende för bin. Biätare (Merops apiaster) är en fågelart som specialiserat sig på att fånga flygande insekter, inklusive bin. De kan orsaka betydande förluster för biodlare i områden där de förekommer rikligt. Andra fåglar, som svalor och flugsnappare, kan också fånga bin i luften. Enskilda fåglar är sällan ett existentiellt hot mot ett stort bisamhälle, men lokala problem kan uppstå.

Insekter utgör en varierad grupp av fiender. Getingar, särskilt bålgetingar, kan vara aggressiva rovdjur som attackerar bikupor för att stjäla honung eller fånga bin som föda till sina egna larver. Den invasiva asiatiska bålgetingen (Vespa velutina) är ett särskilt allvarligt hot i Europa, känd för att kunna decimera bisamhällen snabbt. Tjuvmjölkarbin (t.ex. vissa arter av släktet Psithyrus, numera inkluderade i Bombus) är en typ av humlor som är parasiter på andra humlearters bon; de tar över boet och tvingar värdhumlorna att föda upp deras egna avkomma. Rovsteklar är andra insekter som kan fånga bin.

Spindlar, särskilt hjulnätspindlar som bygger stora nät nära blommor eller bikupor, kan fånga bin. Större spindlar som krabbspindlar kan ligga i bakhåll på blommor och fånga besökande bin.

Vissa däggdjur kan också utgöra ett hot. Björnar är kända för att bryta sig in i bikupor för att komma åt honungen och larverna. I Sverige är detta ett lokalt problem i områden med björnpopulationer. Möss kan ta sig in i kupan under vintern när bina är i klot, äta honung och störa bina. Myror kan ibland också vara ett problem, särskilt om kupan är placerad direkt på marken.

Förutom direkta rovdjur finns det också konkurrenter och kleptoparasiter. Vissa insekter eller till och med andra biarter kan försöka stjäla nektar eller pollen från bins insamlingsplatser eller till och med från kupan.

Binas försvar mot fiender inkluderar vaktbin vid kupans ingång, förmågan att stickas (för arbetsbin och drottningen, även om drottningen sällan lämnar kupan eller sticker annat än rivaliserande drottningar), och i fallet med större hot som bålgetingar, kollektiva försvar som att bilda en het boll runt inkräktaren för att överhetta och döda den. Biodlare kan också vidta åtgärder för att skydda sina samhällen, som att använda mindre ingångar, nät eller elektriska stängsel. Att förstå och hantera binas fiender är en viktig del av biodling och bi-bevarande.
""",
    "binas_sinnen.md": """
# Binas Sinnen: Syn, Lukt och Smak

Binas framgång som pollinatörer och sociala insekter är starkt beroende av deras välutvecklade sinnen. Syn, lukt och smak är särskilt viktiga för att hitta föda, navigera, känna igen släktingar och kommunicera inom samhället. Deras sinnesvärld skiljer sig på många sätt från vår egen, vilket gör dem till fascinerande studieobjekt.

Binas syn är anmärkningsvärd. De har fem ögon: två stora fasettögon på sidorna av huvudet och tre mindre punktögon (ocelli) ovanpå huvudet. Fasettögonen består av tusentals små linser (ommatidier) som ger bin ett brett synfält och utmärkt förmåga att upptäcka rörelse. Deras färgseende skiljer sig från vårt; bin kan se färger som gult, blått och ultraviolett ljus, men de kan inte se rött. Många blommor har mönster som är synliga i ultraviolett ljus, fungerande som "nektarguider" som leder biet till födan. Punktögonen tros främst hjälpa till med stabilisering av flykten och orientering i rymden, kanske genom att känna av horisonten.

Luktsinnet är extremt viktigt för bin och är beläget på antennerna. Bin kan detektera och skilja på en mängd olika dofter, inklusive blomdofter, feromoner från drottningen och andra bin, samt dofter som markerar kupans ingång eller födokällor. Luktsinnet spelar en avgörande roll i att lokalisera blommor, särskilt på avstånd. Bin kan också känna igen specifika blomarter baserat på deras unika doftsignatur. Inom kupan är luktsinnet avgörande för att känna igen medlemmar av det egna samhället och för att upptäcka främmande bin eller inkräktare. Feromoner, som är en typ av luktsignaler, används för att kommunicera komplex information om drottningens status, larvernas behov och faror.

Smaksinnet sitter dels i munpartierna, men också i antennerna och på benen, särskilt på fötterna. Detta gör att bin kan "smaka" på en yta genom att bara landa på den. Smaksinnet är viktigt för att bedöma kvaliteten på nektar och pollen. Bin kan skilja på olika sockerarter och koncentrationer, och de föredrar sötare nektar som ger mer energi. De kan också detektera bittra ämnen som kan indikera att födan är olämplig.

Tillsammans ger binas sinnen dem en rik och detaljerad bild av sin omgivning, anpassad för deras specifika behov som pollinatörer och sociala insekter. Deras förmåga att integrera information från syn, lukt och smak möjliggör effektiv födosamling, exakt navigering och upprätthållande av den komplexa sociala strukturen inom bisamhället. Att förstå binas sinnesvärld ger en djupare uppskattning för deras imponerande biologiska kapacitet.
""",
    "propolis_binas_kada.md": """
# Propolis: Binas Kåda och Dess Användning

Propolis, ofta kallat bikitt, är ett fascinerande material som bin producerar från kåda och harts som de samlar från träd, knoppar och andra växter. Bin bearbetar kådan genom att blanda den med vax och enzymer från sina egna körtlar. Resultatet är ett klibbigt, gummiliknande ämne med en karakteristisk doft och varierande färg, från gulaktig till mörkbrun eller grönaktig, beroende på vilka växter kådan kommer ifrån. Propolis har flera viktiga funktioner i bikupan.

En av propolisens huvudfunktioner är att fungera som ett byggmaterial för att täta springor och oönskade öppningar i bikupan. Detta hjälper till att isolera kupan mot kyla, drag och fukt, vilket är avgörande för att upprätthålla rätt temperatur och mikroklimat, särskilt under vintern. Genom att täta springor minskar bin också inträdet för rovdjur och parasiter som inte kan nagga sig igenom det sega materialet.

Propolis används också för att minska storleken på kupans ingång om den är för stor, vilket gör det lättare att försvara kupan mot inkräktare. Bin kan också använda propolis för att "balsamera" eller täcka över större inkräktare, som möss eller stora insekter, som de dödat men inte kan transportera ut ur kupan. Genom att täcka in kroppen i propolis förhindras förruttnelse och spridning av sjukdomar i kupan.

Kanske mest anmärkningsvärt är propolisens antimikrobiella egenskaper. Materialet innehåller en mängd bioaktiva föreningar, inklusive flavonoider, fenolsyror och eteriska oljor, som har visat sig ha antibakteriella, antivirala, svampdödande och antiinflammatoriska effekter. Bin utnyttjar dessa egenskaper för att hålla kupan hygienisk och minska risken för sjukdomsutbrott i det tätt packade samhället. De klär insidan av cellerna med ett tunt lager propolis innan drottningen lägger ägg, vilket skapar en steril miljö för larvernas utveckling.

Människan har länge känt till och utnyttjat propolisens egenskaper. I gamla civilisationer som Egypten, Grekland och Rom användes propolis traditionellt inom medicinen för sårvård, munhygien och som behandling mot olika åkommor. Idag används propolis fortfarande i folkmedicin och som ingrediens i vissa hälsoprodukter, kosttillskott, salvor och munvårdsprodukter, även om vetenskaplig forskning kring dess medicinska effekter på människor pågår.

Sammanfattningsvis är propolis ett mångsidigt och viktigt material för bisamhället, som fungerar som byggmaterial, försvarsverktyg och desinfektionsmedel. Dess rika biologiska sammansättning och historiska användning understryker dess värde, både för bin och, potentiellt, för människor.
""",
    "binas_anatomi.md": """
# Binas Anatomi: Vingar, Ben och Kroppsdelar

Ett bis kropp är en mästerlig konstruktion, perfekt anpassad för dess uppgifter att flyga, samla föda, bygga, försvara sig och leva i ett komplext socialt samhälle. Binas anatomi är liksom andra insekters uppdelad i tre huvudsegment: huvud, mellankropp (thorax) och bakkropp (abdomen). Varje segment har specialiserade strukturer som är avgörande för biets funktion.

Huvudet är centrum för binas sinnen och födointag. Här finns de fem ögonen – två stora fasettögon på sidorna av huvudet för att upptäcka rörelse och form, och tre mindre punktögon (ocelli) ovanpå för orientering. Antennerna, som sitter på huvudet, är binas primära organ för lukt, smak och beröring, avgörande för att känna av omvärlden och kommunicera inom kupan. Munpartierna är komplexa och anpassade för att slicka upp nektar med tungan (proboscis) och för att tugga och forma vax och pollen med käkarna (mandibler).

Mellankroppen (thorax) är flygets och rörelsens centrum. Här sitter de sex benen och de fyra vingarna. Binas ben är inte bara till för att gå; de är högt specialiserade för olika uppgifter. På frambenen finns en "antennputsare" för att rengöra antennerna. Mellanbenen har en sporre som används för att lossa pollen från pollenkorgarna på bakbenen. Bakbenen hos arbetsbin är särskilt anmärkningsvärda med sina "pollenkorgar" (corbiculae) – släta, konkava områden omgivna av styva hår där biet packar pollen eller propolis för transport tillbaka till kupan. Vingarna är tunna, membranösa och sammankopplade under flykt med små krokar (hamuli) för att fungera som en enda stor yta, vilket möjliggör effektiv flygning.

Bakkroppen (abdomen) innehåller de flesta av biets inre organ, inklusive matsmältningssystemet, reproduktionsorganen (fullt utvecklade endast hos drottningen), hjärtat (ryggrör), och andningssystemet (trakéer). Hos arbetsbin finns vaxkörtlarna på undersidan av bakkroppen, som producerar de små vaxfjällen som används för att bygga vaxkakor. Gadden, som finns hos arbetsbin och drottningen, sitter i slutet av bakkroppen. Hos arbetsbin är gadden hullingförsedd och fastnar i huden på däggdjur, vilket leder till att gadden slits loss och biet dör – ett extremt försvar för samhället. Drottningens gadd saknar stora hullingar och används främst för att döda rivaliserande drottningar. Bakkroppen är också flexibel och kan användas för att packa pollen i celler och för att utföra vaggdansen. Binas anatomi är ett fantastiskt exempel på evolutionär anpassning för överlevnad och socialt liv.
""",
    "biodlingens_historia.md": """
# Biodlingens Historia Genom Tiderna

Relationen mellan människan och bin sträcker sig tusentals år tillbaka i tiden, långt innan modern biodling uppstod. Ursprungligen var relationen baserad på honungsjakt – att lokalisera och plundra vilda bisamhällen för att komma åt den eftertraktade honungen och bivaxet. De äldsta bevisen för detta är grottmålningar i Spanien daterade till cirka 15 000 f.Kr. som visar människor som klättrar i träd för att skörda honung.

De första stegen mot egentlig biodling, där människan började skydda och hantera bisamhällen snarare än att bara plundra dem, skedde i forntida civilisationer. I det gamla Egypten, omkring 2500 f.Kr., fanns en utvecklad biodling där bisamhällen hölls i horisontella lerkrukor eller cylindrar. Dessa transporterades längs Nilen för att dra nytta av olika blomningstider, en tidig form av vandrande biodling. Honung och vax hade stor ekonomisk, medicinsk och religiös betydelse.

I antikens Grekland och Rom fortsatte biodlingen att utvecklas. Grekerna använde olika typer av kupor, inklusive liggande krukor och flätade korgar, och hade en god förståelse för bisamhällets organisation (även om de inte helt förstod drottningens roll, som de ibland trodde var en kung). Romarna beskrev biodling i detalj i jordbrukslitteratur. Både grekerna och romarna värderade högt honung och vax.

Under medeltiden i Europa blev biodling, särskilt vaxproduktionen, mycket viktig. Bivax var nödvändigt för kyrkliga ljus, som användes i stor utsträckning. Kloster var ofta centrum för biodlingskunskap. Bönder höll bin i enkla halmkupor (skepor) eller ihåliga trästockar. Skörden innebar ofta att hela samhället fick offras.

En revolution inom biodlingen skedde på 1800-talet med uppfinningen av den flyttbara ramen. Amerikanen L.L. Langstroth patenterade den första praktiskt användbara bikupan med flyttbara ramar 1852. Denna uppfinning bygger på upptäckten av det "birummet" – ett specifikt avstånd (ca 6-9 mm) som bin varken bygger igen med vax eller propolis. Genom att konstruera ramar med detta avstånd kunde biodlare inspektera samhället, skörda honung och hantera sjukdomar utan att förstöra vaxkakorna eller stressa bina i onödan. Detta möjliggjorde modern, storskalig biodling och ledde till snabb utveckling av teknik och kunskap.

Sedan Langstroths tid har biodlingstekniken fortsatt att förfinas, med nya kupmodeller, metoder för drottningodling, sjukdomsbekämpning och utrustning för honungshantering. Idag är biodling en global verksamhet, från småskaliga hobbybiodlare till stora kommersiella företag, som spelar en avgörande roll för både honungsproduktion och, allt viktigare, för pollineringen av jordbruksgrödor världen över. Biodlingens historia är en spegel av mänsklighetens långa och nära relation till naturen och dessa fantastiska insekter.
""",
    "olika_typer_vildbibon.md": """
# Olika Typer av Vildbibon

Medan honungsbin lever i stora, permanenta samhällen i bikupor, uppvisar de hundratals arter av vildbin i Sverige en förbluffande variation i hur och var de bygger sina bon. De flesta vildbin är solitärbin, vilket innebär att varje hona bygger och försörjer sitt eget bo. Bara humlor, som också räknas till vildbina, lever i samhällen, men dessa är vanligtvis små och ettåriga.

Solitärbin väljer boplatser utifrån artens specifika preferenser. En mycket stor andel av solitärbina är marklevande. De gräver gångar och bon i sandig eller lerig jord, ofta på soliga, ogärna vegetationstäckta platser som sandtag, slänter eller stigar. Varje hona gräver sin egen gång, skapar sidoceller längs gången, samlar pollen och nektar som föda i cellerna, lägger ett ägg i varje cell och förseglar den. Exempel på marklevande solitärbin är sandbin, jordbin och en del vägbin.

En annan stor grupp solitärbin är hålrumslevande. De utnyttjar befintliga håligheter för sina bon. Detta kan vara borrade gångar i dött trä (t.ex. staketstolpar, stockar, eller "bi-hotell"), ihåliga växtstjälkar (som rörflen eller bambu), sprickor i murar eller berg, eller till och med gamla skalbaggegångar i trä. Murarbin och tapetserarbin är vanliga exempel på hålrumslevande solitärbin. Murarbin använder lera eller sand blandat med saliv för att bygga och försegla sina celler, medan tapetserarbin klipper ut cirkulära bitar av blad för att fodra sina bon, därav namnet.

Humlor (vildbin i släktet Bombus) bygger sina bon på andra sätt. Humlesamhällen är ettåriga och grundas på våren av en övervintrad drottning. Boplatserna kan variera men är ofta underjordiska, till exempel i övergivna musbon, i komposter, under stenar eller i täta grästuvor. Vissa humlearter, som t.ex. trädgårdshumlan, kan också bygga bon ovan jord i fågelholkar eller isoleringsmaterial. Humlebon är mindre strukturerade än honungsbinas bon; de bygger vaxkrukor för att lagra nektar och pollen och celler för ägg och larver, men utan de regelbundna, vertikala vaxkakorna.

Att skapa och bevara en mångfald av boplatser är avgörande för att stödja vildbi-populationerna. Att lämna obrukad, sandig mark, behålla dött trä och ihåliga stjälkar, samt sätta upp bi-hotell kan göra stor skillnad för dessa viktiga pollinatörer. Variationen i vildbibon är ett tydligt tecken på den ekologiska mångfald som finns bland bin utöver det välkända honungsbiet.
""",
    "andra_parasiter_sjukdomar.md": """
# Andra Parasiter och Sjukdomar hos Bin

Utöver det ökända varroakvalstret (Varroa destructor), som är det mest destruktiva hotet mot honungsbin globalt, kan bin drabbas av en rad andra parasiter, sjukdomar orsakade av virus, bakterier och svampar, samt skadedjur. Dessa kan försvaga bisamhällen och i värsta fall leda till deras kollaps.

En annan allvarlig parasit är trakékvalstret (Acarapis woodi), som lever i binas luftrör (trakéer) i mellankroppen. Infektion kan försvåra andningen och förkorta binas livslängd, särskilt under vintern. Symtom kan vara svåra att upptäcka utan mikroskopisk undersökning.

Nosema är en svampsjukdom som påverkar binas matsmältningssystem. Den orsakas av encelliga svampar (Microsporidia), främst Nosema apis och Nosema ceranae. Infektion skadar binas tarmar, vilket minskar deras förmåga att ta upp näring från födan. Detta leder till försvagade bin, kortare livslängd och minskad honungsproduktion. Sjukdomen är särskilt problematisk under perioder då bina är instängda i kupan, som på vintern.

Yngelröta är en bakteriell sjukdom som angriper bilarver. De två vanligaste formerna är amerikansk yngelröta (Paenibacillus larvae) och europeisk yngelröta (Melissococcus plutonius). Amerikansk yngelröta är den mest allvarliga, en mycket smittsam sjukdom som snabbt kan utplåna ett samhälle. Bakterien bildar mycket motståndskraftiga sporer som kan överleva i kupmaterial i årtionden. Drabbade larver dör och torkar ihop till mörka fjäll. Europeisk yngelröta är ofta mindre dödlig, men kan också försvaga samhällen avsevärt. Båda kräver strikta hygienåtgärder och i fallet med amerikansk yngelröta ofta destruktion av samhället och utrustningen.

Virus är vanliga hos bin och sprids ofta av varroakvalstret. Exempel inkluderar Deformed Wing Virus (DWV), som orsakar missbildade vingar, och Chronic Bee Paralysis Virus (CBPV), som orsakar skakningar och förlamning. Ett starkt bisamhälle med låg kvalsterinfektion kan ofta hantera virusbelastningen, men i kombination med kvalster kan virus vara mycket skadligt.

Andra skadedjur inkluderar vaxmott, en fjäril vars larver äter vaxkakor och kan förstöra lagrat material, och myror, som kan stjäla honung och störa samhället.

Vildbin kan drabbas av liknande parasiter och sjukdomar, men ofta har de ett mer spritt levnadssätt som kan minska smittspridningen jämfört med de tättboende honungsbina. Att upprätthålla god hygien i biodlingen, välja motståndskraftiga bi-raser och stödja bi-hälsa genom att säkerställa tillgång till varierad föda är viktiga strategier för att hantera dessa hot.

""",
    "hur_bin_ser_varlden.md": """
# Hur Bin Ser Världen: Färgseende och UV-ljus

Binas syn är en av deras mest fascinerande anpassningar, särskilt hur de uppfattar färger. Deras syn är avgörande för att hitta blommor, navigera och känna igen varandra. Medan vi människor har tre typer av färgkänsliga receptorer (för rött, grönt och blått ljus), har bin också tre, men deras spektrum är förskjutet. Bin ser inte rött ljus på samma sätt som vi gör. Istället ser de gult, blått och ultraviolett (UV) ljus.

Det faktum att bin kan se ultraviolett ljus är särskilt viktigt för deras interaktion med blommor. Många blommor som för oss kan se enfärgade ut, har i själva verket komplexa mönster på sina kronblad som bara reflekterar UV-ljus. Dessa UV-mönster, ofta kallade "nektarguider" eller "bi-guider", fungerar som landningsbanor som visuellt leder biet direkt till blommans centrum där nektar och pollen finns. Detta gör bins födosök mycket effektivare. Att se världen i UV-ljus ger bin tillgång till en helt annan uppsättning visuell information som är dold för det mänskliga ögat.

Binas färgseende är inte lika skarpt som vårt, men det är optimerat för att snabbt känna igen mönster och färger associerade med nektar- och pollenrika blommor. De kan skilja mellan olika nyanser av gult, blått och UV, samt blandfärger som skapas när dessa våglängder kombineras. Vitt uppfattas ofta som en blandning av alla färger, inklusive UV, vilket gör vita blommor mycket synliga för bin. Rött ljus, som bin inte ser bra, kan för dem se ut som svart eller en nyans av grått, vilket förklarar varför röda blommor som inte reflekterar UV (t.ex. många rosor) främst pollineras av fåglar eller andra djur som ser rött, snarare än av bin.

Förutom färgseendet ger binas stora fasettögon dem ett mycket brett synfält, nästan 360 grader runt huvudet. Även om de inte har hög upplösning som vårt centrala seende, är fasettögonen extremt bra på att upptäcka rörelse. Detta är avgörande för att undvika rovdjur och navigera i snabb flykt. De tre punktögonen (ocelli) på hjässan tros inte bidra till bildseende, men de hjälper biet att stabilisera sin flykt genom att känna av ljusnivåer och orientera sig mot horisonten.

Sammantaget ger binas specialiserade syn dem en unik uppfattning om sin omvärld, anpassad för deras specifika behov som pollinatörer och sociala insekter. Deras förmåga att integrera information från syn, lukt och smak möjliggör effektiv födosamling, exakt navigering och upprätthållande av den komplexa sociala strukturen inom bisamhället. Att förstå binas sinnesvärld ger en djupare uppskattning för deras imponerande biologiska kapacitet.
""",
    "bins_behov_vatten.md": """
# Bins Behov av Vatten

Vi tänker ofta på bin som samlare av nektar och pollen, men vatten är en lika vital resurs för bisamhällets överlevnad och välbefinnande. Arbetsbin har uppgiften att samla vatten och transportera det tillbaka till kupan, särskilt under varmt väder eller när samhället växer snabbt och behöver reglera temperaturen och fuktigheten inne i kupan.

Vatten används av bin av flera anledningar. För det första är det avgörande för att späda ut den tjocka honungen till en mer lättsmält konsistens, särskilt under perioder när bin föder upp larver. Larverna matas med en blandning av pollen, nektar (eller honung) och körtelsekret från arbetsbin, och vatten behövs för att justera konsistensen på denna föda.

För det andra används vatten för att reglera temperaturen inne i kupan. Bin håller en anmärkningsvärt konstant temperatur i yngelområdet, vanligtvis runt 32-35 grader Celsius, oavsett yttertemperaturen. Under varma dagar hämtar fältbin vatten och sprider ut det i tunna skikt på vaxkakorna. Andra bin i kupan fläktar sedan med vingarna för att skapa luftcirkulation. När vattnet avdunstar sänks temperaturen i kupan, liknande hur svett kyler däggdjur. Denna "luftkonditionering" är avgörande för att förhindra överhettning som kan skada både vuxna bin och yngel.

För det tredje bidrar vatten till att upprätthålla rätt fuktighetsnivå i kupan. Viss fuktighet behövs för att förhindra att larverna torkar ut och för att underlätta hanteringen av den lagrade honungen.

Bin samlar vatten från en mängd olika källor. De föredrar ofta platser med grunt vatten där de lätt kan landa utan att drunkna, som kanter av pölar, fågelbad med stenar i, fuktig jord eller blad med dagg. De lockas ofta till platser som kan tyckas orena för oss, som vatten från gödselstackar eller diken, eftersom dessa källor kan innehålla mineraler eller salter som bin behöver.

En brist på tillgängligt vatten kan stressa ett bisamhälle allvarligt och påverka dess förmåga att föda upp yngel och reglera kupans temperatur. Biodlare är medvetna om detta behov och tillhandahåller ofta en vattenkälla nära sina bikupor, särskilt under torra perioder eller när det finns ont om naturliga vattenkällor i närheten. Att se till att bin har tillgång till rent vatten är en enkel men viktig åtgärd för att stödja deras hälsa och bidra till ett välmående bisamhälle.
""",
    "pollen_bibrod.md": """
# Pollen och Bibröd: Binas Proteinrika Föda

Nektar ger bin energi i form av kolhydrater, men för att växa, utvecklas och upprätthålla samhällets hälsa behöver bin också en rik källa till protein, vitaminer, mineraler och fetter. Denna källa är pollen. Pollen, som samlas från blommande växter, är avgörande för larvernas tillväxt, unga bins utveckling av körtlar (som producerar bidrottninggelé och vax), och för drottningens äggläggning.

Fältbin samlar pollen medvetet när de besöker blommor för att samla nektar. När biet besöker en blomma fastnar pollenkorn på dess håriga kropp. Med hjälp av sina ben borstar biet av pollen och packar det i de specialiserade "pollenkorgarna" (corbiculae) som finns på utsidan av bakbenen hos honungsbin och humlor. Innan biet packar pollen i korgen, fuktar det det ofta med en liten mängd nektar eller honung från sin honungsblåsa, vilket hjälper till att forma pollen till en kompakt boll. Dessa pollenbollar, som ofta har lysande färger beroende på vilken blomma de kommer ifrån (gul, orange, brun, lila etc.), transporteras sedan tillbaka till kupan.

Väl i kupan levererar fältbiet pollenbollarna till arbetsbin som lagrar dem i tomma celler runt yngelområdet. När pollen har lagrats i cellerna, bearbetas det av andra arbetsbin. De packar pollen hårt i cellerna och blandar det med en liten mängd honung och enzymer. Denna jäsningsprocess, som liknar fermentering, omvandlar pollen till "bibröd" (bee bread). Bibröd är mer näringsrikt, lättare att smälta och längre hållbart än obehandlat pollen. Jäsningsprocessen bryter ner de hårda cellväggarna i pollenkornen och frigör näringsämnen, samtidigt som den producerar mjölksyra som bevarar bibrödet.

Bibröd är den primära proteinkällan för larverna och de unga arbetsbin som producerar larvföda och bidrottninggelé. Drottningen behöver också bibröd för att kunna producera ett stort antal ägg. Utan tillräckligt med pollen och bibröd kan bisamhällets tillväxt stanna av, och binas hälsa kan försämras. Variationen av pollen från olika blommor är viktig för att säkerställa att bin får en balanserad kost med alla nödvändiga aminosyror, vitaminer och mineraler.

Att säkerställa att bin har tillgång till en mångfald av pollenkällor under hela säsongen är en kritisk aspekt av bi-hälsa och bevarande. Genom att plantera eller bevara blommande växter som producerar rikligt med pollen bidrar vi direkt till bisamhällenas styrka och deras förmåga att utföra sin avgörande roll som pollinatörer.
""",
    "honungsdagg.md": """
# Honungsdagg: En Ovanlig Honungskälla

När vi tänker på honung, föreställer vi oss oftast bin som samlar nektar från blommor. Men bin kan också producera honung från en annan, mindre känd sockerrik källa: honungsdagg. Honungsdagg är en sockerhaltig vätska som utsöndras av vissa växtsugande insekter, framför allt bladlöss (aphider), när de livnär sig på sav från växter. Bin kan samla denna honungsdagg istället för eller som komplement till blomnektar.

Processen börjar när bladlöss suger upp stora mängder sav från blad eller stjälkar för att få tillgång till de proteiner de behöver. Sav är mycket rik på socker men relativt fattig på protein. Bladlössen måste därför konsumera stora volymer sav och utsöndrar överskottssockret som en klibbig, söt vätska – honungsdagg. Denna honungsdagg kan sedan droppa ner på blad och grenar under de angripna växterna.

När blomnektar är knapp, eller om det finns en riklig källa till honungsdagg i närheten, kan fältbin börja samla denna honungsdagg istället. Bin behandlar honungsdaggen på samma sätt som nektar; de samlar in den i sin honungsblåsa och transporterar den tillbaka till kupan. Där bearbetas den av andra bin genom att tillsätta enzymer och ventilera bort fukt, precis som vid honungsproduktion från nektar. Resultatet blir honungsdagghonung.

Honungsdagghonung skiljer sig ofta från blomhonung. Den är vanligtvis mörkare i färgen och har en mer robust, mindre söt, ibland lite syrlig eller maltig smak. Den har ofta en högre halt av mineraler, antioxidanter och vissa sockerarter som inte finns i nektar. Honungsdagghonung kristalliserar sig generellt sett mycket långsammare än blomhonung på grund av en annan sockerbalans.

Produktion av honungsdagghonung är helt beroende av förekomsten av de växtsugande insekterna och de rätta växtarterna. Vanliga källor inkluderar träd som gran, tall, ek, lönn och lind som har bladlöss eller andra sköldlöss. Vissa år, om förhållandena är de rätta för bladlössens förökning och väderförhållandena är gynnsamma för binas insamling (inte för regnigt som sköljer bort daggen), kan honungsdagg utgöra en betydande del av bins honungsproduktion.

Ur ett biodlingsperspektiv kan honungsdagghonung vara en värdefull skörd, men den har också sina utmaningar. Vissa typer av honungsdagghonung har en sockerprofil som kan vara svår för bin att smälta under vintern, vilket kan leda till problem som dysenteri. Därför brukar biodlare se till att bin får tillräckligt med vinterfoder baserat på sockerlösning istället för enbart honungsdagghonung. Trots detta är honungsdagg en fascinerande och viktig alternativ födokälla som visar på binas anpassningsförmåga.
""",
    "processen_skapa_bivax.md": """
# Processen att Skapa Bivax

Bivax är en anmärkningsvärd substans som bin producerar och använder för att bygga den struktur som hela bisamhället är beroende av: vaxkakorna. Dessa hexagonala celler fungerar som bikupans skafferi för honung och pollen, och som barnkammare där drottningen lägger sina ägg och larverna växer upp. Processen att skapa bivax är energikrävande och utförs av unga arbetsbin.

Bivax produceras av speciella vaxkörtlar som sitter på undersidan av bakkroppen hos arbetsbin i en viss ålder, vanligtvis mellan 12 och 20 dagar gamla. För att kunna producera vax måste bin konsumera stora mängder honung. Det krävs ungefär 6-8 kg honung för att producera 1 kg vax. Detta understryker vaxets värde för bisamhället – det är en investering av lagrad energi.

När bina är redo att producera vax, samlar de sig i täta klungor inne i kupan och bildar en "bivall". I denna bivall är temperaturen hög (cirka 33-36°C), vilket är nödvändigt för att vaxkörtlarna ska fungera optimalt. Små, tunna vaxfjäll, ungefär 2-3 millimeter stora, utsöndras från körtlarna och stelnar när de kommer i kontakt med luften.

Biet använder sedan speciella borstar och kammar på sina ben för att lossa vaxfjällen från sin bakkropp. De för vaxfjällen till munnen där de tuggas och bearbetas med käkarna (mandibler) och en liten mängd saliv. Denna process omvandlar de spröda fjällen till ett formbart, mjukt material.

Med det bearbetade vaxet börjar bina bygga vaxkakor. De formar vaxet till sexkantiga celler i ett tätt, regelbundet mönster. Formen på cellerna är mycket effektiv; sexhörningar använder minst mängd byggmaterial för att skapa maximal volym och är strukturellt starka. Bina bygger vaxkakorna vertikalt, hängande ner från taket eller ramarnas överlister i en bikupa. Celler byggs på båda sidor av en gemensam mittvägg. Arbetet är ett kollektivt projekt där många bin bidrar till att bygga ut och forma kakorna.

När cellerna är färdiga används de omedelbart av samhället för att lagra honung och pollen, samt för att föda upp yngel. När honung har lagrats i en cell och fuktigheten är den rätta, förseglar bina cellen med ett tunt vaxlock för att skydda honungen. Dessa vaxlock tas sedan bort av biodlaren vid honungsskörd (avlivas) och är det renaste bivaxet.

Bivax är inte bara funktionellt; det har också använts av människan i årtusenden för en mängd olika syften, inklusive ljustillverkning, kosmetika, läkemedel och konst. Processen som bin använder för att skapa detta mångsidiga material är ett av många exempel på den imponerande ingenjörskonst som finns i bisamhället.
""",
    "binas_immunforsvar_halsa.md": """
# Binas Immunförsvar och Hälsa

Trots att bin är små insekter har de ett komplext immunförsvar som hjälper dem att bekämpa patogener som bakterier, virus och svampar. Deras hälsa är avgörande för bisamhällets överlevnad, och förståelsen för bi-immunitet är ett viktigt område inom forskningen, särskilt med tanke på de ökande hoten mot bi-populationer.

Binas immunförsvar skiljer sig från däggdjurens. De har inte antikroppar eller specialiserade celler som T-celler, men de har ett effektivt medfött immunförsvar. Detta system bygger på både cellulära och humorala (vätskebaserade) svar. Det cellulära svaret involverar specialiserade celler (hemocyter) som cirkulerar i binas "blod" (hemolymfa). Dessa celler kan känna igen främmande partiklar som bakterier eller parasiter och antingen fagocytera (äta upp) dem eller kapsla in större inkräktare.

Det humorala svaret innebär produktion av antimikrobiella peptider och enzymer som cirkulerar i hemolymfan. Dessa ämnen kan direkt attackera och neutralisera patogener. Vissa av dessa peptider produceras som svar på en infektion, medan andra finns ständigt närvarande som ett första försvar.

Utöver sitt individuella immunförsvar har bisamhället också en unik form av "social immunitet" eller kollektiv hälsa. Detta inkluderar flera beteenden och mekanismer som minskar spridningen av sjukdomar inom den tätt packade kupan. Ett exempel är putsbeteendet (grooming), där bin rengör sig själva och varandra för att avlägsna parasiter som varroakvalster. Ett annat är hygientbeteende, där arbetsbin känner igen och avlägsnar sjuka larver eller puppor från cellerna innan infektionen sprider sig vidare.

Drottningen spelar en roll i samhällets immunitet genom att överföra vissa immunitetsfaktorer, som t.ex. vitellogenin, till äggen. Detta ger larverna en viss nivå av passiv immunitet.

Trots dessa försvarssystem är bin sårbara för en rad patogener, och deras immunförsvar kan bli överbelastat, särskilt när de är stressade av andra faktorer som dålig näring, pesticider eller hög parasitbelastning (t.ex. varroa). Forskning på binas immunförsvar syftar till att bättre förstå dessa mekanismer för att utveckla strategier för att stärka bisamhällenas motståndskraft mot sjukdomar och därmed bidra till att minska bi-dödligheten. En frisk bi-population är avgörande för både biodling och ekosystemens hälsa.
""",
    "lagar_regler_biodling.md": """
# Lagar och Regler Kring Biodling i Sverige

Att bedriva biodling i Sverige, vare sig det är i liten skala som hobby eller i större kommersiell skala, innebär att man som biodlare måste känna till och följa vissa lagar och regler. Dessa syftar till att skydda både binas hälsa, förhindra spridning av bisjukdomar och säkerställa kvaliteten på biprodukter.

En central del av regelverket rör bisjukdomar. Jordbruksverket har ansvar för bekämpning av allvarliga bisjukdomar som amerikansk yngelröta och europeisk yngelröta. Det finns anmälningsplikt för dessa sjukdomar; om en biodlare misstänker eller konstaterar smitta måste detta omedelbart rapporteras till Länsstyrelsen. Länsstyrelsen fattar sedan beslut om eventuella restriktioner, avspärrningar av drabbade bigårdar eller destruktion av smittade samhällen och material för att hindra vidare spridning. Det är också förbjudet att flytta bisamhällen, drottningar eller begagnad utrustning från en bigård till en annan utan tillstånd eller kontroll. Att köpa bin eller drottningar från källor med okänd hälsostatus är en risk.

För att underlätta smittspårning rekommenderas starkt att alla biodlare registrerar sina bigårdar hos Jordbruksverket. Detta är inte obligatoriskt för hobbybiodlare med färre än 15 samhällen, men det underlättar informationsspridning och insatser vid sjukdomsutbrott i närområdet.

Vid produktion och försäljning av honung finns det regler kring märkning och hygien. Honung som säljs måste uppfylla vissa kvalitetskrav. Märkningen på honungsburken ska bland annat ange produktens namn (Honung), nettovikt, namn och adress på biodlaren/förpackaren, ursprungsland (Sverige), och eventuella tillsatser (vilket vanligtvis inte förekommer i ren honung). För honung som säljs direkt från biodlaren till konsumenten är reglerna något enklare än för honung som säljs via butiker.

Regler kring placering av bikupor kan också finnas, särskilt i tätbebyggda områden eller nära allmänna platser. Även om det sällan finns specifika lagar som förbjuder biodling i stadsmiljö, kan lokala ordningsföreskrifter eller hänsynsregler gälla. Det handlar ofta om att placera kupor så att de inte utgör en direkt fara eller olägenhet för grannar eller allmänheten, till exempel genom att rikta flustret (ingången) bort från gångvägar eller inhägna bigården.

Utöver nationella regler kan EU-gemensamma regler gälla för biodling och biprodukter. Som biodlare är det ens eget ansvar att hålla sig informerad om gällande lagar och regler, ofta via Jordbruksverket och relevanta biodlareorganisationer, för att bedriva en ansvarsfull och hållbar biodling.
""",
    "hur_bin_orienterar_sig.md": """
# Hur Bin Orienterar Sig: Sol, Magnetfält och Landmärken

Binas förmåga att navigera är häpnadsväckande. Ett fältbi kan flyga flera kilometer från kupan för att hitta en nektar- eller pollenkälla och sedan hitta tillbaka till sin egen specifika kupa, även bland tusentals andra i en stor bigård. Denna precisa orienteringsförmåga bygger på ett komplext system där bin använder flera olika navigeringsverktyg.

En av de viktigaste navigeringsmetoderna är att använda solen som en kompass. Bin kan uppfatta polariserat ljus, vilket gör att de kan bestämma solens position även när den är dold bakom moln. Genom att känna av mönstret i det polariserade himmelsljuset kan biet beräkna var solen befinner sig. De kompenserar även för solens rörelse över himlen under dagen, med hjälp av en inre biologisk klocka. Vaggdansen använder solens position i relation till kupans vertikala yta för att kommunicera riktningen till en födokälla.

Förutom solen använder bin landmärken i landskapet. När ett ungt bi gör sina första orienteringsflygningar runt kupan, lär det sig att känna igen visuella särdrag i omgivningen – träd, byggnader, kullar, floder etc. Dessa landmärken fungerar som visuella referenspunkter under senare födosök. När ett bi återvänder till kupan efter en flygning, gör det ofta en "återkomstspiral" runt kupans ingång, som om det bekräftar sin position och uppdaterar sin minneskarta över området.

Forskning tyder också på att bin kan använda jordens magnetfält för orientering, även om denna mekanism är mindre välförstådd än solkompassen och landmärkena. Det finns bevis för att bin har förmåga att detektera magnetfält och att detta kan spela en roll, särskilt under molnigt väder eller i kombination med andra signaler.

Bins navigering är flexibel. Om en av navigeringssystemen störs, kan de förlita sig mer på de andra. Till exempel, om solen inte är synlig och de befinner sig i ett område utan tydliga landmärken, kan magnetfältsorientering bli viktigare.

Dofter spelar också en roll i navigeringen, särskilt på kortare avstånd. Bin kan följa doftspår från blommor, andra bin, eller doften av sin egen kupa.

Denna kombination av en "solkompass" (som kompenserar för tid på dagen), en "minneskarta" baserad på visuella landmärken, potentiell användning av magnetfält, och doftsignaler, gör bin till exceptionella navigatörer. Deras förmåga att effektivt hitta föda och återvända till kupan är fundamental för bisamhällets överlevnad och visar på en imponerande kognitiv kapacitet hos dessa små insekter.
""",
    "runddansen_vaggdansen.md": """
# Runddansen och Vaggdansen: Olika Budskap

Binas danser är ett av naturens mest kända exempel på symbolisk kommunikation. Det mest berömda är vaggdansen, som används för att kommunicera platsen för födokällor som är relativt långt bort. Men för närmare källor använder bin en annan typ av dans: runddansen. Dessa två danser, tillsammans med övergångsformer, utgör bisamhällets komplexa "språk" för att förmedla information om föda.

Runddansen används när en nektar- eller pollenkälla finns **nära** bikupan, vanligtvis inom cirka 50-100 meter. När ett fältbi hittar en rik källa på nära håll och återvänder till kupan, utför det en runddans på vaxkakan. Dansen består helt enkelt av att biet rör sig i snäva cirklar, omväxlande medurs och moturs. Biet stannar ibland upp och ger smakprov av nektar till andra bin som följer dansen. Runddansen förmedlar information om att det finns en bra födokälla **nära kupan** och ger information om **doften** av blommorna (via smakprovet), men den ger **ingen information om riktning eller exakt avstånd**. Andra bin i kupan, som känner doften och vet att källan är nära, lämnar sedan kupan och söker efter blommor med den specifika doften i närområdet.

När födokällan är **längre bort**, över cirka 50-100 meter, övergår biet till att utföra **vaggdansen**. Som beskrivits tidigare, består vaggdansen av en rak "vaggningsfas" följd av en båge tillbaka till startpunkten, en ny rak vaggningsfas och en båge åt andra hållet, bildande en "åtta". Vaggdansen förmedlar betydligt mer detaljerad information:
* **Riktning:** Vinkeln på den raka vaggningsfasen i förhållande till vertikalt uppåt (gravitationen) korrelerar med vinkeln till födokällan i förhållande till solen.
* **Avstånd:** Längden och intensiteten på den raka vaggningsfasen (antal vibrationer) indikerar avståndet. En längre och mer intensiv dans betyder längre avstånd.
* **Kvalitet:** Hur länge och intensivt biet dansar totalt indikerar födokällans kvalitet.

Övergångsformer mellan runddans och vaggdans kan observeras för källor på medelavstånd, vilket ytterligare understryker kontinuiteten i detta kommunikationssystem.

Skillnaden i budskap mellan runddansen och vaggdansen är logisk ur binas perspektiv. För nära källor är den exakta riktningen mindre viktig; det räcker att veta att det finns något bra i närheten och vad det luktar. För längre avstånd blir däremot effektivitet avgörande, och precis riktning och avståndsinformation hjälper andra bin att snabbt hitta den specifika källan utan att slösa energi på slumpmässigt sökande. Binas dansspråk är ett anmärkningsvärt bevis på deras kognitiva förmåga och deras komplexa sociala organisation.
""",
    "bin_pollinatorer_frukt_bar.md": """
# Bin som Pollinatörer av Fruktträd och Bärodlingar

Bins roll som pollinatörer är avgörande för en stor del av vår livsmedelsproduktion, inte minst för odlingen av fruktträd och bärbuskar. Många av de populäraste frukterna och bären vi äter är beroende av eller gynnas kraftigt av pollinering av bin, främst honungsbin och humlor. Utan dessa flitiga insekter skulle skördarna minska dramatiskt eller helt utebli.

Fruktträd som äpplen, päron, plommon, körsbär och mandlar är i hög grad beroende av korspollinering, vilket innebär att pollen måste överföras från blommor på en sort av trädet till en annan sort för att fruktsättning ska ske. Bin är de mest effektiva transportörerna av detta pollen. När ett bi besöker en blomma för att samla nektar eller pollen, fastnar pollenkorn på dess kropp. När biet sedan flyger till nästa blomma på ett annat träd av en kompatibel sort, överförs pollen, och befruktning kan ske. En intensiv bi-aktivitet under blomningen säkerställer en god pollinering, vilket resulterar i fler frukter, större frukter och frukter med bättre form.

Bär som blåbär, lingon, jordgubbar, hallon och vinbär gynnas också av bi-pollinering, även om graden av beroende varierar mellan arter. Vissa bär, som jordgubbar, kan ge viss fruktsättning utan bi-pollinering, men bin förbättrar avsevärt både mängden bär och bärets kvalitet (storlek, form). Blåbär är särskilt beroende av humlor och vissa solitärbin med en specifik teknik för att "buzz-pollinera" blommorna, vilket innebär att de vibrerar med sina flygmuskler för att skaka loss pollen.

Biodlare transporterar ofta bisamhällen till fruktodlingar och bärodlingar under blomningsperioden. Detta kallas hyrespollinering och är en viktig inkomstkälla för biodlare, samtidigt som det säkerställer högsta möjliga skörd för odlaren. Placeringen av kupor i odlingarna måste ske strategiskt för att maximera binas besök på grödorna.

Nedgången i bi-populationer globalt utgör ett allvarligt hot mot dessa grödor. Förlust av vildbin på grund av habitatförlust och pesticidanvändning minskar den naturliga pollinering som sker utöver honungsbinas insats. Därför är insatser för att skydda och främja både honungsbin och vildbin direkt kopplade till vår förmåga att fortsätta odla frukter och bär i de mängder och den kvalitet vi är vana vid. Att stödja bin är att stödja en hållbar livsmedelsproduktion.
""",
    "ekologisk_biodling.md": """
# Ekologisk Biodling: Principer och Praxis

Ekologisk biodling är en form av biodling som följer ekologiska principer, med fokus på bisamhällets naturliga beteenden, hälsa och välfärd, samt en hållbar förvaltning av både bin och den omgivande miljön. Målet är att producera honung och andra biprodukter på ett sätt som minimerar negativ påverkan på binas hälsa, den biologiska mångfalden och ekosystemet.

Centralt för ekologisk biodling är valet av plats för bigården. Platser bör väljas där bin har tillgång till nektar- och pollenkällor som huvudsakligen kommer från ekologiskt odlade växter eller vilda områden som inte har behandlats med förbjudna bekämpningsmedel eller syntetiska gödningsmedel inom en viss radie. Detta minskar risken att bin samlar in kontaminerad föda.

Behandling av bisjukdomar och parasiter skiljer sig också inom ekologisk biodling. Förebyggande åtgärder som att välja motståndskraftiga bi-raser, upprätthålla god hygien i bigården och regelbunden kontroll av samhällets hälsa är avgörande. Vid behov av behandling tillåts endast vissa naturliga substanser, som t.ex. myrsyra, oxalsyra eller mjölksyra, för bekämpning av varroakvalster. Användning av syntetiska kemiska bekämpningsmedel eller antibiotika är förbjudet. Sjukdomar som inte kan behandlas med tillåtna metoder, som amerikansk yngelröta, hanteras genom destruktion av samhället och materialet enligt gällande lagar, precis som i konventionell biodling.

Foderhanteringen är en annan viktig aspekt. Bina ska i första hand leva av sin egen honung och pollen. För vinterfoder är det tillåtet att ge ekologiskt socker eller ekologisk honung från den egna bigården. Det är inte tillåtet att ge sockerlösning gjord på konventionellt socker eller honung från icke-ekologisk produktion.

Val av bi-ras är också relevant; ekologisk biodling gynnar lokala bi-raser som är anpassade till den lokala miljön och dess klimat, och som har god naturlig motståndskraft mot sjukdomar. Metoder för drottningodling ska följa ekologiska principer.

Användningen av material i bikupan styrs också. Kuporna ska huvudsakligen vara tillverkade av naturliga material. Vid behov av behandling av kupmaterial tillåts endast vissa substanser. Plastramar och plastmellanväggar är generellt inte tillåtna, även om undantag kan finnas under en övergångsperiod.

Certifiering av ekologisk biodling kräver att biodlaren följer de specifika regler som sätts upp av kontrollorgan och att bigården inspekteras regelbundet. Honung och andra biprodukter från ekologisk biodling kan märkas med ekologiska märkningar, som t.ex. KRAV eller EUs ekologiska logotyp. Ekologisk biodling är inte bara en metod för att producera honung, utan en helhetssyn på biodling som en del av ett större, hållbart ekosystem.
""",
    "binas_overvintring.md": """
# Binas Övervintring: Klotet och Foder

För honungsbin i tempererade klimat, som Sverige, är övervintringen en kritisk period. Till skillnad från många andra insekter som dör på hösten eller går i dvala individuellt, övervintrar ett bisamhälle kollektivt som en enhet i kupan. De går inte i dvala i egentlig mening, utan är aktiva inuti ett vinterklot för att hålla sig varma. En framgångsrik övervintring kräver rätt förberedelser inför vintern.

När temperaturen sjunker på hösten, slutar bina att flyga ut för att samla föda. De samlas istället i ett tätt klot inne i kupan, oftast centrerat runt yngelområdet (om det fortfarande finns något sent yngel) och foderförråden. Detta kallas vinterklotet. Genom att vibrera med sina flygmuskler (utan att vingarna rör sig) genererar bina värme. Bina i klotets yttre lager sitter tätt packade för att isolera och minimera värmeförlust. Inne i klotet är temperaturen betydligt högre än yttertemperaturen, runt 20-30°C i den yttre delen och 30-35°C i kärnan när yngel ska värmas. Bina roterar långsamt mellan klotets yttre och inre delar så att inget bi blir för kallt.

För att generera värme och överleva vintern behöver bina energi, vilken de får från sina lagrade foderförråd – honung och bibröd. Honung är den primära energikällan (kolhydrater), medan bibröd ger protein och andra näringsämnen, särskilt viktigt om yngel föds upp tidigt på våren. Ett starkt bisamhälle behöver lagra en betydande mängd foder inför vintern, ofta mellan 15-25 kg honung eller motsvarande i sockerlösning. Om foderförrådet är otillräckligt riskerar samhället att svälta.

En annan kritisk faktor under övervintringen är ventilationen i kupan. Bin producerar vattenånga när de förbränner sitt foder. Om fukten inte kan ventileras ut, kan den kondensera på kupans insida, vilket skapar en fuktig och kall miljö som gynnar mögel och sjukdomar. För hög fuktighet kan vara dödligt för bisamhället. Biodlare säkerställer därför att kuporna har tillräcklig ventilation, ofta via flusteröppningen och eventuella ventilationshål högre upp.

Under vintern är binas aktivitet minimal. De lämnar inte kupan för att tömma tarmen; avföring sparas tills en lämplig "rengöringsflykt" kan göras under en varmare vinterdag. Långa perioder av instängdhet utan möjlighet till tömningsflykt kan leda till dysenteri, en allvarlig tarmsjukdom.

På senvintern eller tidig vår börjar drottningen ofta lägga ägg igen, och bina måste öka temperaturen i yngelområdet. Detta kräver mer energi och stressar samhället. En lyckad övervintring beror på ett starkt samhälle, tillräckligt med foder, god ventilation och minimala störningar. Att hjälpa bina att övervintra framgångsrikt är en av biodlarens viktigaste uppgifter.
""",
    "vinterfoder_varstimulering.md": """
# Vinterfoder och Vårstimulering i Bikupan

Inför den långa svenska vintern är det avgörande för biodlaren att säkerställa att bisamhällena har tillräckligt med foder för att överleva. Bin lever på sina lagrade reserver av honung och bibröd under den period de inte kan flyga ut och samla föda. Om dessa reserver är otillräckliga måste biodlaren tillföra extra vinterfoder.

Det primära vinterfodret som bin lagrar är honung. Ett starkt samhälle behöver upp till 20-25 kg honung för att klara en normal vinter. Om biodlaren har skördat honung under sommaren, behöver det utrymme som honungen tog upp ersättas med annat foder. Det vanligaste extrafodret är en sockerlösning, oftast gjord på strösocker och vatten i proportionerna 2:1 (två delar socker till en del vatten) eller 3:2. Denna sockerlösning lagras av bina i cellerna och omvandlas till ett "vinterfoder" som de kan leva på. Sockerlösningen är energirik och lätt för bin att hantera. Viss honungsdagghonung kan vara svårsmält för bin under vintern och bör undvikas som enda vinterfoder.

Utöver energi från socker/honung behöver bin också tillgång till bibröd (lagrat pollen) som proteinkälla, särskilt på senvintern när drottningen börjar lägga ägg igen och larverna behöver protein för att växa. Ett samhälle bör ha flera ramar med bibröd lagrat nära vinterklotet.

På vårvintern, när dagarna blir längre men utomhustemperaturen fortfarande är låg, kan biodlaren ge så kallad "vårstimulering". Detta syftar till att uppmuntra drottningen att börja lägga ägg och därmed starta uppfödningen av nya bin inför den kommande säsongen. Vårstimulering kan göras genom att ge en mindre mängd tunn sockerlösning (t.ex. 1:1 socker/vatten), en pollenersättning (proteinfoder), eller genom att flytta ramar med lagrat foder närmare vinterklotet. Detta lurar bina att tro att flödet av föda utifrån har börjat, vilket stimulerar äggläggningen. För tidig och för kraftig vårstimulering kan dock vara riskabelt om vädret snabbt slår om till kyla och det inte finns tillräckligt med bin att värma det ökande yngelområdet.

Korrekt foderhantering – att säkerställa tillräckligt med foder inför vintern och vid behov ge lämplig vårstimulering – är kritiskt för att bisamhällena ska överleva vintern starka och redo för säsongens utmaningar. Det är en av de viktigaste färdigheterna för en framgångsrik biodlare.
""",
    "grunderna_drottningodling.md": """
# Grunderna i Drottningodling

Drottningen är bisamhällets hjärta, och hennes kvalitet är avgörande för samhällets styrka, produktivitet och motståndskraft. Att kunna odla egna drottningar (drottningodling) är en central färdighet för seriösa biodlare, oavsett om målet är att ersätta gamla eller dåliga drottningar, öka antalet bisamhällen, eller avla på önskvärda egenskaper som mildhet, svärmtröghet och motståndskraft mot sjukdomar.

Drottningodling utnyttjar bisamhällets naturliga förmåga att föda upp en ny drottning när den gamla drottningen försvinner, dör eller är dålig. Processen bygger på att man presenterar mycket unga larver (1-2 dagar gamla) för arbetsbin som saknar en drottning eller vars drottning har spärrats bort. Dessa arbetsbin, som då blir "nöddrottningbin", kan omvandla larverna till drottningar genom att mata dem rikligt och uteslutande med bidrottninggelé under hela larvstadiet. De bygger också speciella, större drottningceller runt larverna.

Den vanligaste metoden för drottningodling involverar att man tar en ram med unga larver från ett bisamhälle med goda egenskaper (moder samhälle). Dessa larver överförs sedan försiktigt till speciella odlingsramar eller "ympas" över till plastkoppar som sätts in i ett samhälle som förberetts för att föda upp drottningar (odlingssamhälle). Odlingssamhället är antingen drottninglöst eller har sin drottning bortspärrad, vilket gör att arbetsbina är motiverade att genast börja dra upp nya drottningar från de presenterade larverna.

Efter cirka 10-11 dagar är drottningcellerna färdiga att kläckas. De kan då flyttas till små parningskupor (parningssamhällen eller nucs) som består av en liten mängd bin och foder. Varje parningskupa får en färdig drottningcell. Några dagar senare kläcks den unga drottningen i parningskupan. Hon kommer sedan att göra en eller flera parningsflygningar till drönarsamlingsplatser för att para sig med drönare. Efter framgångsrik parning återvänder hon till parningskupan och börjar lägga ägg.

När den unga, parades drottningen har börjat lägga ägg i parningskupan, är hon redo att introduceras i ett produktionssamhälle. Detta kan vara ett samhälle som har blivit drottninglöst (antingen naturligt eller av biodlaren), eller ett samhälle där den gamla drottningen avsiktligt byts ut. Introduktionen måste göras försiktigt, ofta genom att placera den nya drottningen i en liten bur med några arbetsbin från det mottagande samhället. Detta ger bina tid att vänja sig vid hennes feromon innan hon släpps ut, vilket minskar risken att hon dödas.

Drottningodling är en tidsödande och kunskapskrävande process som kräver noggrann planering och hantering. Men möjligheten att producera egna, högkvalitativa drottningar är en ovärderlig tillgång för varje seriös biodlare som vill bygga starka och friska bisamhällen.
""",
    "svarmkontroll_hantering.md": """
# Svärmkontroll och Hur Man Hanterar Svärmar

Svärmning är binas naturliga sätt att föröka sig som samhälle. När ett bisamhälle blir stort, starkt och trångbott under senvåren eller försommaren, kan det bestämma sig för att dela sig. Den gamla drottningen lämnar då kupan med ungefär hälften av arbetsbina för att hitta ett nytt hem. Kvar i den ursprungliga kupan finns yngel, foder och nylagda drottningceller, ur vilka en ny drottning kommer att kläckas. För biodlaren innebär svärmning en förlust av bin och honungsproduktion i den svärmande kupan, samt risken att svärmen försvinner eller bosätter sig på ett oönskat ställe (t.ex. i en skorsten). Svärmkontroll är därför en viktig del av biodlingen.

Svärmlust är en naturlig instinkt, men den kan hanteras genom olika metoder för svärmkontroll. Målet är att minska binas motivation att svärma genom att ge dem mer utrymme, avbryta drottningens äggläggningstillgång till alla ramar, eller simulera svärmningsprocessen på ett kontrollerat sätt.

En grundläggande svärmkontrollsåtgärd är att i god tid utöka kupan genom att lägga till nya lådor med ramar, vilket ger bina mer plats för yngeluppfödning och foderlagring. Detta minskar trängseln. Att se till att bina har möjlighet att bygga nya vaxkakor kan också minska svärmlusten.

Mer direkta metoder involverar att bryta svärmningscykeln. En vanlig metod är att regelbundet inspektera samhällen under svärmningsperioden (typiskt från slutet av maj till juli) och leta efter svärmceller – speciella, större celler där bina föder upp nya drottningar inför en svärmning. Om svärmceller hittas, kan de brytas bort för att hindra svärmningen. Detta måste göras regelbundet, ofta varje 7-10 dag, då bina snabbt kan dra upp nya svärmceller.

En annan metod är att göra en konstgjord svärm eller avläggare. Detta innebär att man tar bort den gamla drottningen och några ramar med bin och yngel och placerar dem i en ny kupa på en ny plats – i princip en kontrollerad svärm. I den ursprungliga kupan lämnas några svärmceller kvar, ur vilka en ny drottning kläcks, eller så introducerar man en parad drottning. Detta uppfyller samhällets behov av att dela sig på ett sätt som gynnar biodlaren.

Trots försök till svärmkontroll kan ett samhälle svärma. Om en svärm upptäcks, kan biodlaren försöka fånga in den. En nyligen utsvärmad klot med bin och drottningen sitter ofta i ett träd eller en buske. Genom att placera en tom kupa eller låda under svärmen och försiktigt skaka ner bina, kan svärmen fångas in och flyttas till en ny kupa. Att fånga en svärm är ofta relativt enkelt eftersom svärmande bin är fokuserade på att hitta ett nytt hem och är mindre benägna att stickas.

Svärmkontroll är en balansgång mellan att respektera binas naturliga beteende och att förvalta samhällena för honungsproduktion och bi-hälsa. Framgångsrik svärmkontroll kräver att biodlaren är uppmärksam, förstår bisamhällets signaler och agerar i tid.
""",
    "binas_avgorande_roll_vilda_vaxter.md": """
# Binas Avgörande Roll för Vilda Växters Fortplantning

Bin, både honungsbin och de otaliga arterna av vildbin som finns i våra landskap, spelar en fundamentalt viktig roll för fortplantningen av en överväldigande majoritet av vilda växter. Medan vindpollinering fungerar för vissa växter (som gräs och barrträd), är pollinering utförd av insekter, och bland dem bin, den dominerande mekanismen för fortplantning hos blommande växter. Utan denna ekosystemtjänst skulle vilda växter inte kunna producera frön och frukter i den utsträckning som krävs för att upprätthålla den biologiska mångfalden.

Vilda växter är anpassade för att attrahera pollinatörer, och bin är bland de mest effektiva. De besöker blommor regelbundet för att samla nektar och pollen, de resurser som är nödvändiga för deras egen överlevnad. När biet besöker en blomma, fastnar pollenkorn på dess håriga kropp. När biet sedan flyger till nästa blomma av samma art, överförs pollen, och befruktning kan ske. Detta säkerställer korspollinering, vilket är viktigt för många växtarters genetiska variation och förmåga att anpassa sig till förändrade miljöer.

Många vilda växtarter har utvecklat specifika relationer med vissa biarter. Vissa blommor har en form eller struktur som bara kan pollineras effektivt av bin med en viss storlek eller tunglängd. Vissa solitärbin är "oligolektiska", vilket betyder att de enbart samlar pollen från en enda växtart eller en liten grupp närbesläktade arter. Dessa specialiserade pollinatörer är avgörande för just dessa växters överlevnad. Exempelvis är vissa klockblommor beroende av specifika klockbiarter för pollinering. Humlor är viktiga pollinatörer för många vilda blommor, särskilt de med djupa blomkalkar som bara humlor med sina långa tungor kan nå nektarn i.

Förlusten av bi-populationer, vare sig det gäller honungsbin eller vildbin, har direkta konsekvenser för vilda växtsamhällen. När pollinatörer minskar, minskar frösättningen hos de växter de pollinerar. Detta kan leda till att växtpopulationer krymper eller försvinner lokalt. Eftersom många djur är beroende av vilda växter för föda (frön, bär, löv) och skydd, kan en nedgång i växtligheten få kaskadeffekter genom hela ekosystemet, vilket påverkar fåglar, däggdjur, insekter och andra organismer.

Att skydda vilda bins livsmiljöer – genom att bevara eller återställa blommande ängar, dikeskanter, skogsbryn och andra blommrika områden – är avgörande för att upprätthålla en frisk vildbi-population. Att minska användningen av pesticider och undvika att slå gräs och vegetation under blomningsperioden bidrar också. Genom att säkerställa vilda bins fortlevnad skyddar vi inte bara insekterna själva, utan bevarar också den biologiska mångfald av vilda växter som är så fundamental för friska och motståndskraftiga ekosystem. Binas arbete för vilda växter är en tyst, men ovärderlig, tjänst.
"""
}


# Expanded glossary content with definitions for all terms
GLOSSARY_CONTENT_ALL = """
# Ordlista

* **Anatomi:** Läran om organismers kroppsliga uppbyggnad; syftar här på biets kroppsdelar.
* **Antenner:** Binas känselorgan på huvudet, viktiga för lukt, smak och beröring.
* **Arbetarbi:** Steril honbi som utför alla uppgifter i bikupan utom äggläggning.
* **Bifigurer:** Ett informellt samlingsnamn för olika djur (insekter, fåglar, däggdjur etc.) som utgör fiender för bin.
* **Bikupa:** Den bostad som bin lever i, antingen naturlig eller konstgjord (biodlares kupa).
* **Bisamhället:** Den sociala enheten som består av drottning, arbetsbin och drönare, fungerar som en superorganism.
* **Bivall:** En tät klunga av bin i kupan, bildad för att generera värme vid vaxproduktion eller under vintern (vinterklot).
* **Bivax:** Vax som produceras av arbetsbin från särskilda körtlar på bakkroppen, används för att bygga vaxkakor och täcka honungsceller.
* **Bibröd:** Pollen som packats i vaxceller och fermenterats med honung och enzymer, används som proteinrik föda.
* **Cell (Vaxcell):** De sexkantiga strukturer som bygger upp vaxkakorna, används för lagring av honung/pollen och uppfödning av yngel.
* **Drönare:** Hanbi vars enda uppgift är att para sig med drottningen. Utvecklas från obefruktat ägg.
* **Drottning:** Det enda fertila honbiet i samhället, ansvarig för all äggläggning.
* **Drottningodling:** Processen att avsiktligt föda upp nya bidrottningar.
* **Ekologisk biodling:** Biodling som följer ekologiska principer för att gynna bi-hälsa och miljö.
* **Facettögon:** Binas två stora sammansatta ögon på sidorna av huvudet, utmärkta på att upptäcka rörelse och UV-ljus.
* **Feromon:** Kemisk signal som bin använder för kommunikation, t.ex. drottningferomonet.
* **Gadd:** Biets (arbetsbi/drottning) försvarspiggar, kopplad till giftkörtel.
* **Habitatförlust:** När ett djurs eller en växts naturliga livsmiljö förstörs eller fragmenteras, ofta p.g.a. mänsklig aktivitet.
* **Hemolymfa:** Binas "blod", vätskan som cirkulerar i deras öppna cirkulationssystem och transporterar näringsämnen och immunceller.
* **Honung:** Binäring som produceras av bin från nektar, lagras som föda.
* **Honungsdagg:** Sockerhaltig vätska som utsöndras av växtsugande insekter och som bin ibland samlar och omvandlar till honung.
* **Honungsskörd:** Processen att samla in överskottshonung från bikupan.
* **Humlor:** En grupp av vildbin (släktet Bombus) som lever i mindre, ettåriga samhällen och är effektiva pollinatörer, särskilt i kyligare väder.
* **Immunförsvar:** Organismens system för att skydda sig mot sjukdomar och främmande inkräktare.
* **Lagstiftning (Biodling):** Lagar och regler som styr biodling, t.ex. rörande bisjukdomar och honungshantering.
* **Larv:** Biets stadium mellan ägg och puppa, en period av snabb tillväxt.
* **Livscykel:** Biets utveckling från ägg till vuxet bi (ägg, larv, puppa, vuxen).
* **Nektar:** Sockerrik vätska producerad av blommor, bins huvudsakliga källa till kolhydrater (energi).
* **Nektarkälla:** Växter eller blommor som producerar nektar som bin samlar.
* **Ocelli:** Binas tre små punktögon ovanpå huvudet, tros hjälpa till med flygorientering och stabilisering.
* **Orientering (Bin):** Binas förmåga att navigera och hitta sin väg med hjälp av bl.a. solen, magnetfält och landmärken.
* **Parningsflykt:** Den flygning då en ung drottning parar sig med drönare.
* **Patogen:** En mikroorganism (bakterie, virus, svamp etc.) som kan orsaka sjukdom.
* **Pesticider:** Kemikalier som används för att döda skadeorganismer, t.ex. insekter (insekticider) eller ogräs (herbicider). Kan vara skadliga för bin.
* **Pollen:** Blommas hanliga fortplantningsmaterial, bins huvudsakliga källa till protein, vitaminer och mineraler (bibröd).
* **Pollenkälla:** Växter eller blommor som producerar pollen som bin samlar.
* **Pollenkorgar:** Specialiserade strukturer på bakbenen hos honungsbin och humlor, används för att transportera pollen och propolis.
* **Pollinatör:** Ett djur (främst insekter som bin) som överför pollen mellan blommor och därmed möjliggör befruktning.
* **Pollinering:** Överföring av pollen från en blomma till en annan, ofta utfört av bin. Viktigt för många växters fortplantning.
* **Predator:** Ett djur som jagar och äter andra djur; i bins fall inkluderar det t.ex. fåglar, getingar och spindlar.
* **Propolis:** Kåda eller harts som bin samlar från träd och växter och använder för att täta springor i kupan och som skydd mot mikroorganismer.
* **Pupa:** Biets stadium mellan larv och vuxet bi, då omvandlingen (metamorfosen) sker inuti en kokong.
* **Ram:** Träram som innehåller vaxkakor i en modern bikupa, kan enkelt lyftas ur kupan av biodlaren.
* **Runddans:** Binas kommunikationsdans för att ange att en födokälla finns nära kupan.
* **Slunga:** En centrifugalmaskin som används för att extrahera honung ur vaxkakor.
* **Solitärbin:** En stor grupp av vildbin som lever ensamma, där varje hona bygger och försörjer sitt eget bo.
* **Superorganism:** En social enhet (som ett bisamhälle) där individerna fungerar som delar av en större, integrerad enhet.
* **Svärming:** Bisamhällets naturliga fortplantningsmetod där en del av samhället, inklusive den gamla drottningen, lämnar kupan för att bilda ett nytt samhälle.
* **Svärmkontroll:** Metoder biodlare använder för att hantera eller förhindra svärmning.
* **Symbios:** Ett förhållande mellan två olika organismer där båda drar nytta, t.ex. mellan bin och blommor.
* **Urban biodling:** Att hålla bikupor och bedriva biodling i stadsmiljö.
* **Vaggdans:** Binas kommunikationsdans för att ange riktning, avstånd och kvalitet på en födokälla som är längre bort från kupan.
* **Vandrande biodling:** Att flytta bisamhällen mellan olika platser för att dra nytta av olika blomningstider.
* **Varroakvalster:** En parasit (Varroa destructor) som angriper honungsbin och är ett stort hot mot bisamhällens hälsa världen över.
* **Vax:** Se Bivax.
* **Vaxkörtlar:** Specialiserade körtlar på undersidan av arbetsbinas bakkropp som producerar bivax.
* **Vårstimulering:** Åtgärder biodlare vidtar på vårvintern för att stimulera drottningens äggläggning.
* **Ägg:** Biets första livsstadium, lagt av drottningen i en vaxcell.
"""

# MkDocs configuration file content (Updated navigation for 40 articles)
MKDOCS_YML_CONTENT_ITERATION6 = """
site_name: Världen av Bin
nav:
    - Hem: index.md
    - Artiklar:
        - Biets Livscykel: biets_livscykel.md
        - Drottningbiet: drottningbiet.md
        - Arbetsbinas Många Uppgifter: arbetsbin.md
        - Drönarnas Roll i Bikupan: dronare.md
        - Biets Kommunikation: vaggdansen.md
        - Hot mot Bin: hot_mot_bin.md
        - Olika Bi-arter i Sverige: olika_biarter_sverige.md
        - Biodling som Hobby: biodling_hobby.md
        - Bins Roll i Ekosystemet: bins_roll_ekosystemet.md
        - Bin i Staden: bin_i_staden.md
        - Honungsskörd och Hantering: honungsskord_hantering.md
        - Bin och Blommor: Ett Symbiotiskt Förhållande: bin_blommor_symbios.md
        - Bisamhällets Organisation och Superorganismen: bisamhallets_organisation.md
        - Olika Typer av Honung och Deras Egenskaper: olika_typer_honung.md
        - Bin i Historien, Myter och Kulturen: bin_historia_kultur.md
        - Bin och Väder: Hur Påverkas Binas Aktivitet?: bin_vader_aktivitet.md
        - Drottningens Livsfarliga Parningsflykt: drottningens_parningsflykt.md
        - Binas Naturliga Fiender: binas_naturliga_fiender.md
        - Binas Sinnen: Syn, Lukt och Smak: binas_sinnen.md
        - Propolis: Binas Kåda och Dess Användning: propolis_binas_kada.md
        - Binas Anatomi: Vingar, Ben och Kroppsdelar: binas_anatomi.md
        - Biodlingens Historia Genom Tiderna: biodlingens_historia.md
        - Olika Typer av Vildbibon: olika_typer_vildbibon.md
        - Andra Parasiter och Sjukdomar hos Bin: andra_parasiter_sjukdomar.md
        - Hur Bin Ser Världen: Färgseende och UV-ljus: hur_bin_ser_varlden.md
        - Bins Behov av Vatten: bins_behov_vatten.md
        - Pollen och Bibröd: Binas Proteinrika Föda: pollen_bibrod.md
        - Honungsdagg: En Ovanlig Honungskälla: honungsdagg.md
        - Processen att Skapa Bivax: processen_skapa_bivax.md
        - Binas Immunförsvar och Hälsa: binas_immunforsvar_halsa.md
        - Lagar och Regler Kring Biodling i Sverige: lagar_regler_biodling.md
        - Hur Bin Orienterar Sig: Sol, Magnetfält och Landmärken: hur_bin_orienterar_sig.md
        - Runddansen och Vaggdansen: Olika Budskap: runddansen_vaggdansen.md
        - Bin som Pollinatörer av Fruktträd och Bärodlingar: bin_pollinatorer_frukt_bar.md
        - Ekologisk Biodling: Principer och Praxis: ekologisk_biodling.md
        - Binas Övervintring: Klotet och Foder: binas_overvintring.md
        - Vinterfoder och Vårstimulering i Bikupan: vinterfoder_varstimulering.md
        - Grunderna i Drottningodling: grunderna_drottningodling.md
        - Svärmkontroll och Hur Man Hanterar Svärmar: svarmkontroll_hantering.md
        - Binas Avgörande Roll för Vilda Växters Fortplantning: binas_avgorande_roll_vilda_vaxter.md
    - Ordlista: ordlista.md
theme:
    name: material
plugins:
    - search
"""

# GitHub Actions workflow file content (Unchanged)
GITHUB_ACTIONS_YML_CONTENT_ITERATION6 = """
name: Deploy MkDocs Site

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: 3.x

      - name: Install dependencies
        run: |
          pip install mkdocs mkdocs-material
          # Add any validation steps here if needed, e.g., mkdocs validate

      - name: Deploy site
        run: mkdocs gh-deploy --force
        # The --force flag is often used with gh-deploy on the main branch
        # to overwrite the gh-pages branch history. Adjust if your
        # deployment strategy requires appending or different handling.

"""

# --- Script Generation Logic ---

def create_site_structure(articles_dict, glossary_content, mkdocs_yml, github_actions_yml):
    """Creates the necessary directories and files for the MkDocs site."""
    print("Creating site directories...")
    os.makedirs("docs", exist_ok=True)
    os.makedirs(".github/workflow", exist_ok=True)

    print("Creating index.md...")
    with open("docs/index.md", "w", encoding="utf-8") as f:
        f.write("# Välkommen till Världen av Bin\n\nDetta är en sida om bin, skapad med kärlek av AI-bin för människor. Utforska artiklarna för att lära dig mer om dessa fascinerande varelser.")

    print("Creating article files...")
    for filename, content in articles_dict.items():
        filepath = os.path.join("docs", filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f" - Created {filepath}")

    print("Creating ordlista.md...")
    with open("docs/ordlista.md", "w", encoding="utf-8") as f:
        f.write(glossary_content)
    print(" - Created docs/ordlista.md")

    print("Creating mkdocs.yml...")
    with open("mkdocs.yml", "w", encoding="utf-8") as f:
        f.write(mkdocs_yml)
    print(" - Created mkdocs.yml")

    print("Creating GitHub Actions workflow file...")
    workflow_path = os.path.join(".github", "workflows", "mkdocs.yml")
    with open(workflow_path, "w", encoding="utf-8") as f:
        f.write(github_actions_yml)
    print(f" - Created {workflow_path}")

    print("\nSite files generated successfully.")

def print_prompts_used():
    """Prints all the prompts used across all completed iterations."""
    num_articles = len(REDAKTOR_TOPICS_ALL)
    # Number of previous articles when the NEW_BATCH_10 prompt was used (Iterations 5, 6)
    num_previous_articles_iter5 = 20
    num_previous_articles_iter6 = 30
    # Number of previous articles when the NEW_BATCH_5 prompt was used (Iterations 2, 3, 4)
    num_previous_articles_iter2_4 = [5, 10, 15]

    print("\n--- Prompts Used Across Iterations 1, 2, 3, 4, 5 & 6 ---")

    print("\n--- Arkitekt Prompts ---")
    print("Iteration 1 Design Prompt:")
    print(ARKITEKT_PROMPT_ITER1)
    print(f"\nIteration 2, 3, 4, 5 & 6 Review Prompt Template (used with num_articles=10, 15, 20, 30 and {num_articles}):")
    print(ARKITEKT_PROMPT_REVIEW.format(num_articles='{num_articles}')) # Show template placeholder


    print("\n--- Tekniker Prompts ---")
    print("Iteration 1 Outline Prompt:")
    print(TEKNIKER_PROMPT_OUTLINE_ITER1)
    print("(Note: Tekniker's main task in subsequent Iterations was implementation based on team's results, not new outline prompts)")


    print("\n--- Redaktör Prompt Template and Topics ---")
    print("Template Used for Each Article:")
    print(REDAKTOR_PROMPT_TEMPLATE)
    print(f"\nAll Topics Used Across Iterations 1-{len(REDAKTOR_TOPICS_ALL)//5 if len(REDAKTOR_TOPICS_ALL)%5==0 else '?'}:") # Dynamic iteration count
    for i, topic in enumerate(REDAKTOR_TOPICS_ALL):
        print(f"{i+1}. {topic}")
    print("(Note: The template was used for each topic to generate the article content stored above)")


    print("\n--- Kvalitetsansvarig Prompts ---")
    print("Iteration 1 Review Prompt (5 articles):")
    print(KVALITETSANSVARIG_PROMPT_ITER1)
    print(f"\nIteration 2, 3 & 4 Review Prompt Template (5 new articles per batch, used with num_previous_articles={num_previous_articles_iter2_4}):")
    print(KVALITETSANSVARIG_PROMPT_NEW_BATCH_5.format(num_previous_articles='{num_previous_articles}')) # Show template placeholder
    print(f"\nIteration 5 & 6 Review Prompt Template (10 new articles per batch, used with num_previous_articles={num_previous_articles_iter5} and {num_previous_articles_iter6}):")
    print(KVALITETSANSVARIG_PROMPT_NEW_BATCH_10.format(num_previous_articles='{num_previous_articles}')) # Show template placeholder

    print(f"\nAll Terms Identified Across Iterations 1-{len(REDAKTOR_TOPICS_ALL)//5 if len(REDAKTOR_TOPICS_ALL)%5==0 else '?'}:")
    print(", ".join(KVALITETSANSVARIG_TERMS_ALL))


    print("\n--- Testledare Prompts ---")
    print("Iteration 1 Initial Plan Prompt:")
    print(TESTLEDARE_PROMPT_ITER1)
    print(f"\nIteration 2, 3, 4, 5 & 6 Review Prompt Template (used with num_articles=10, 15, 20, 30 and {num_articles}):")
    print(TESTLEDARE_PROMPT_REVIEW.format(num_articles='{num_articles}')) # Show template placeholder


    print("\n--- End of Prompts Used ---")


# --- Main Execution ---
if __name__ == "__main__":
    print("Executing script to generate site files and display prompts for Iteration 6...")

    # 1. Create the site structure with generated content and config
    create_site_structure(
        ARTICLE_CONTENT_ALL,
        GLOSSARY_CONTENT_ALL,
        MKDOCS_YML_CONTENT_ITERATION6, # Use updated YML
        GITHUB_ACTIONS_YML_CONTENT_ITERATION6 # Use potentially updated GH Action (unchanged this iter)
    )

    # 2. Display the prompts that were used to generate this iteration's result
    print_prompts_used()

    print("\nIteration 6 complete. Please review the generated files and prompts.")
    print(f"This script generates all {len(ARTICLE_CONTENT_ALL)} articles and the updated ordlista/navigation.")
    print("To demo, replace the previous files with these new ones and commit to your GitHub repository's 'main' branch.")
    print("The GitHub Action should then automatically build and deploy the updated site.")

