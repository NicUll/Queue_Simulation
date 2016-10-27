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
postkontoret kl 14:00. Han startar programmet och skriver in värdena, utdatan blir just vilken tid han kan vänta sig att lämna.

Fru Franco undrar hur länge hon kan räkna med att få jobba över en dag då många kunder har flera ärenden, 
hon startar programmet och höjer antal ärenden per kund. Sedan startar hon simuleringen och ser när den sista kunden lämnar.

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
    
    
    
class Model(object):
  def __init__(self):
    pass

class Controller(object):
  def __init__(self):
    pass
    
class View(object):
  def __init__(self, model):
    pass


```

##Programflöde och dataflöde

1. Programmet startas
  * En main-funktion startas och;
  * Skapar en tk-inter ruta
  * Hämtar senaste controller-värdena från fil och skapar 
    * Model-objekt med hämtade värden, skapar ett office-objekt
    * View-objekt som får en referens till model
    * Simulation-objekt med referens till view och model, startas pausad
    * Controller med referens till simulering och model (som även håller i simuleringsvärden)
  * View och controller ritas upp i tk-inter rutan
2. Användaren kan välja att ändra parametrarna först eller starta simuleringen
3. Simulering startas och simuleringsobjektet kallar på model och view för att
   ändra parametrar, updatera kunder och skriva ut text. Controllern körs parallellt 
   och kallar vid behov på model och simulation
4. Text matas ut med information om kunder, användaren kan när som pausa simuleringen
5. Simuleringen har kört färdigt och alla händelser finns kvar i rutan.
6. Användaren avslutar programmmet.
  
