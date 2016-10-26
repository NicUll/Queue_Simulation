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
    the last customer from the queue"""
    pass


class Customer(object):
  def __init__(self, in_time, errands):
    """Create a new customer and store the amount of errands they have
    and the time they entered the post-office."""
    pass
    
    
class Simulation(object):
  def __init__(self, Controller):
    """Runs the simulation with the current simulation
    parameters taken from the controller)"""
    
class Controller(object):
  def __init__(self):


```

##Programflöde och dataflöde
