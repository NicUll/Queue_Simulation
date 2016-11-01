##DD1316 – Kösimulering
####Nic Ullman

###Specifikation

##Inledning
Jag ska göra ett program som simulerar kundhanteringen på ett postkontor. Programmet ska startas från en terminal 
och sedan öppnas i ett eget fönster med ett grafiskt användargränssnitt. I gränssnittet ska möjligheten finnas att 
ändra simuleringsparametrar (hastighet, kundfrekvens, antal ärenden, öppettider), pausa, starta och starta om simuleringen. 
Möjligheten ska även finnas att enbart skriva in antal ärenden och klockslag som en person anländer och få data 
på när personen kan förväntas lämna postkontoret.

En utmaning blir att presentera datan på ett tydligt sätt och att skriva algoritmer som hanterar de 
simuleringsparametrar som finns på ett smart sätt.

##Användarscenarier
Kalle är nyfiken på hur lång tid han kan förvänta sig att få vänta att få 3st ärenden klara om han anländer vid 
postkontoret kl 14:00. Han startar programmet och möts av ett fönster med en stor textruta för utdata till vänster, sliders för att ändra simuleringsparametrar samt start- och pausknappar under dessa, till höger. Han väljer att låta simuleringsparametrarna ha kvar sina standardvärden. Kalle är nu enbart intresserad av att veta hur lång tid det skulle ta för honom, och fyller därför i en textruta med sitt antal ärenden och vilket klockslag han tänkte anlända. Därefter klickar han på, "simulera enstaka kund" och får då i textrutan till vänster ut informationen:
*"Kund som anländer kl 14:00 med 3 ärenden kan förväntas lämna postkontoret kl 14:07"*
Kalle har nu fått sin uppskattade tid och väljer att klicka på "avsluta", programmet stängs då ner.

Fru Franco undrar hur lång aktiv arbetstid hon kan förvänta sig samt hur länge hon kan räkna med att få jobba över en dag då många kunder har fler ärenden än vanligt. 
Hon startar programmet och höjer antal ärenden i genomsnitt per kund genom att dra i en slider till höger. Sedan startar hon simuleringen genom att klicka på knappen "simulera heldag". I rutan till vänster matas alla ärenden ut och allra sist står när sista kunden lämnar följt av; 
* antal kunder 
* total kötid
* väntetid (enbart kö) per kund 
* total arbetstid
* arbetstid per kund
Hon avslutar sedan programmet genom att klicka på "avsluta".

##Programskelett
```python

class Office(object):
  def __init__(self, times, time_per_customer):
    """Create a post-office object with parameters for 
    business-hours and the time it takes per customer.
    A list is also initiated that will hold the customer queue,
    together with an index keeping track of current customer."""
    pass
    
  def add_customer(self, customer):
    """Add a customer to the queue.
    Return their place in the queue"""
    pass
    
  def customer_done(self, out_time):
    """Increase the customer queue index 
    i.e. go to next customer."""
    pass


class Customer(object):
  def __init__(self, in_time, errands):
    """Create a new customer and store the amount of errands they have
    and the time they entered the post-office."""
    pass
    
    
class Simulation(object):
  def __init__(self, view, model):
    """Runs the simulation with the current simulation
    parameters."""
    pass
    
  def start_simulation(self):
    pass
    
  def pause_simulation(self):
    pass
    
  def update_parameters(self):
    """Change the values used to simulate"""
     pass
    
    
class Model(object):
  def __init__(self, values):
    """Model object that holds the simulation parameters."""
    pass
    
class SaveFile(object):
  def __init(self, filename):
    """An object responsible for handling the savefile"""
    pass

class Controller(object):
  def __init__(self):
    """The controller that changes simulation parameters."""
    pass
    
class View(object):
  def __init__(self, model):
    """The view that displays the GUI and outputs the simulation data."""
    pass


```

##Programflöde och dataflöde

1. Programmet startas
  * En main-funktion startas och;
  * Skapar en tk-inter ruta
  * Hämtar senaste controller-värdena från fil genom att
    skapa ett savefile objekt med referens till sparfilen 
    (om den finns, annars skapas filen) och skapar sedan:
    * Model-objekt med hämtade värden -> skapar ett office-objekt
    * View-objekt som får en referens till model
    * Simulation-objekt med referens till view och model, startas pausad
    * Controller med referens till simulering och model (som även håller i start-simuleringsvärden åt controller)
  * View och controller ritas upp i tk-inter rutan
2. Användaren kan välja att ändra parametrarna först eller starta simuleringen
3. Simulering startas och körs i en main-loop där simuleringsobjektet kallar på model och view för att
   ändra parametrar, updatera kunder och skriva ut text. Controllern körs om lott 
   och kallar vid behov på model och simulation
4. Text matas ut med information om kunder, användaren kan när som pausa simuleringen (main-loopen)
5. Simuleringen har kört färdigt och alla händelser finns kvar i rutan.
6. Användaren avslutar programmmet. 

  
