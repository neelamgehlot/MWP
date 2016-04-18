# Mathematical Word Problem Solver
Hindi mathematical word problem solver

# Translator:

1. Uses Google's Translate API.
2. Manually here: http://www.lexilogos.com/keyboard/devanagari.htm

# POS Tagging:

http://www.coli.uni-saarland.de/~thorsten/tnt/

# Creating Containers:

Containers will have :
Entity, Attribute, Verb, Quantity(Equation)

We have following Python files(Each representing a different object):    
1. Question.py    
2. Containers.py    
3. Equation.py    
4. makeVerbDict.py    
5. MWP.py 

# Example:

राम के पास १० सेब है। उसने श्याम को ५ सेब दिये। अब राम के पास ७ सेब है। तो श्याम के पास पेह्ले कितने सेब थे।


Container1  
Name : राम    
Entity : सेब    
Attr :    
Quantity:10    

Name : राम    
Entity : सेब    
Attr :    
Quantity:10 - 5    

Name : राम    
Entity : सेब    
Attr :    
Quantity:7    

Container2    
Name :    
Entity :    
Attr :    
Quantity:    

Name : श्याम    
Entity :     
Attr :     
Quantity:J + 5    

Name : श्याम    
Entity :    
Attr :    
Quantity:7    

Equation is :    
J + 5  =  7    
The final result is:  2.0    
