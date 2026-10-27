"""
Created on Sat Oct 24 18:27:13 2026

@Author: Ellen Johanne Eidem, elljoh-e@online.no

"""
print('')

#%% Oppgave 1
print('Oppgave 1')

# Inndata
alder = int(input('Hvilket år er du født? ') )


#Beregninger
år_2024 = 2024 - alder  # Oppgaven ber om antall år i 2024
år_2026 = 2026 - alder  # Oppgaven ber om antall år i 2024, men her antas det inneværende år som er 2026
år_2027 = 2027 - alder  # Oppgaven ber om antall år i 2024, men her antas det neste år som er 2027


# Utdata
print(f'I løpet av 2024 ble du {år_2024:0.0f} år.')
print(f'I løpet av 2026 ble/blir du {år_2026:0.0f} år.')
print(f'I løpet av 2027 blir du {år_2027:0.0f} år.')




#%% Oppgave 2
print('Oppgave 2')

# Import av pakker
import numpy as np


# Inndata
antall_elever = int(input('Skriv inn antall elever: ' ))


# Antakelse
pizza_per_elev = 1/4  # Hver elev spiser 1/4 pizza


# Beregninger
antall = np.ceil(antall_elever * pizza_per_elev)  # Forhøyer oppover til nærmeste hele tall


# Utdata
print(f'Det må handles inn {antall :0.0f} pizzaer.')




#%% Oppgave 3
print('Oppgave 3')

# Import av pakker
import numpy as np


# Inndata
v_grad = float(input('Dette programmet konverterer fra grader til radianer. Skriv inn gradtallet: '))


# Funksjon
def grad2rad(grader):
    
    v_rad = v_grad*np.pi/180  # Konvertering fra grader til radianer
    
    return v_rad


#Beregninger
v_radianer = grad2rad(v_grad)  # Kaller opp funksjonen som konverterer


# Utdata
print(f'{v_grad} grader er lik {v_radianer :0.2f} radianer.')




#%% Oppgave 4
print('Oppgave 4')

# Oppgave 4a)

# Inndata

data = {
        'Norge': ['Oslo', 0.634],  # Navn på hovedstaden i landet og antall milllioner innbyggere i hovedstaden 
        'England': ['London', 8.982],
        'Frankrike': ['Paris', 2.16],
        'Italia' : ['Roma', 2.873]
        }

land = str(input('Skriv inn et land (Norge, England, Frankrike, Italia): ').capitalize())

hovedstad, innbyggere = data[land]  # Tilordner verdier til variablene hovedstad og innbyggere basert på valgt land


# Utdata

print(f'{hovedstad} er hovedstaden i {land} og det er {innbyggere} mill. innbyggere i {hovedstad}.')



# Oppgave 4b)

# Nye inndata

land5 = str(input('Skriv inn et nytt land: ').capitalize())  # Innhenter informasjon om et nytt land
hovedstad5 = str(input('Skriv inn hovedstaden i landet: ').capitalize())
innbyggere5 = float(input('Skriv inn antall innbyggere i hovedstaden (mill.): '))

data.update({land5: [hovedstad5, innbyggere5]})  # Oppdaterer dictionaryen data


# Utdata

print('Dictionaryen data:')
print(data)  # Skriver dictionaryen data til skjerm




#%% Oppgave 5
print('Oppgave 5')

# Import av pakker
import numpy as np


# Inndata
a = float(input('Skriv inn lengden på a: '))  # a er lik diameter i sirkelen = 2r
b = float(input('Skriv inn lengden på b: '))  # b er lik store katet til en rettvinklet trekant


# Funkjson
def areal_omkrets(a ,b):
    A_halvsirkel = (np.pi*(a/2)**2)/2  # Arealet av halve sirkelen = pi r^2 / 2, der r = a/2
    A_trekant = a*b/2  # Arealet av trekanten a = lille katet, b = store katet
    
    A_figur = A_halvsirkel + A_trekant  # Totalt areal av figuren
    
    
    O_trekant = b + np.sqrt(a**2 + b**2)  # Lengden av store katet + hypotenusen (lille katet skal ikke medregnes)
    
    O_halvsirkel = np.pi*(a/2)  # Lengden av halve sirkelen = pi r
    O_figur = O_trekant + O_halvsirkel  # Total ytre omkrets av figuren
    
    return A_figur, O_figur

# Beregninger
areal, omkrets = areal_omkrets(a, b)  # Tuppel

# Utdata    
print(f'Arealet av figuren i oppgaven er {areal :0.1f} og ytre omkrets er {omkrets :0.1f}.')




#%% Oppgave 6
print('Oppgave 6')

# Import av pakker
import numpy as np
import matplotlib.pyplot as plt


# Inndata
x = np.linspace(-10, 10, 200)  # Oppretter en array med 200 punkter jevnt fordelt mellom -10 og 10, stoppverdien er inkludert


# Funksjon
def f(x):
    dummy = -x**2 -5
    return dummy


# Plotting
plt.close(1)  # Lukker alle figurer
plt.figure(1, figsize = (8,4))  # Oppretter Figure 1
plt.rcParams.update({'font.size': 14})  # Setter fontstørrelse i hele plottet
plt.plot(x, f(x),'r-',label='f(x)')  # Plotter f(x) som funksjon av x
plt.title('Oppgave 6')
plt.legend()  # Oppretter en tegnforklaring
plt.xlabel('x')
plt.ylabel('Verdi')
plt.xlim(-10,10)
plt.ylim(-100,0)
plt.grid()
plt.tight_layout()  # Gjør plass til plottet og aksetitler
plt.show()

