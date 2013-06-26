#!/usr/bin/env python

#(c) GPLv3 2013 Daniel Bauer (headlessD@gmail.com) 
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys

# definition of amino acid weight by acronym
a=89.10
r=174.2
n=132.12
d=133.1
c=121.16
q=146.15
e=147.13
g=75.07
h=155.16
i=131.17
l=131.18
k=146.19
m=149.21
f=165.19
p=115.13
s=105.09
t=119.12
w=204.23
y=181.19
v=117.15

h2o=18.01

# returns the molar mass of an amino acid
def get_molar_mass(code):
        if code is 'A':
                return a
        if code is 'R':
                return r
        if code is 'N':
                return n
        if code is 'D':
                return d
        if code is 'C':
                return c
        if code is 'Q':
                return q
        if code is 'E':
                return e
        if code is 'G':
                return g
        if code is 'H':
                return h
        if code is 'I':
                return i
        if code is 'L':
                return l
        if code is 'K':
                return k
        if code is "M":
                return m
        if code is "F":
                return f
        if code is "P":
                return p
        if code is "S":
                return s
        if code is "T":
                return t
        if code is "W":
                return w
        if code is "Y":
                return y
        if code is "V":
                return v

# calculates molar mass of a sequence given as a string
def calculate_molar_mass(string):
	number_of_acids = 0
	molar_mass = 0
	for aa in string:
		molar_mass = molar_mass + get_molar_mass(aa)
		number_of_acids += 1
		
	molar_mass = molar_mass - (number_of_acids-1)*h2o
	return molar_mass

# asks for user input
def ask_for_acid():
	user_input = raw_input("Please enter your aminoacid sequence:")
	if user_input is "":
		print "No sequence entered!"
		print ""
		print_help()
		return ask_for_acid()
	else:
		return user_input

# shows header
def show_interface():
	print "###################################"
	print "###### Amino acid calculator ######"
	print "###################################"
	print ""
	print ""
	
# prints a short help
def print_help():
	print "Help:"
	print "To calculate the mass for an aminoacidsequence, simply put the sequence (codeform) in the input box using capital letters and press enter"
	print "example: The sequence Alanine-Cysteine-Tyrosine would be ACY"
	print ""
	print "You can also use this programm by running it with the aminoacid sequence as an argument"
	print ""
	
	
if __name__ == '__main__':
	if len(sys.argv) > 1:
		acid_string = sys.argv[1]
	else:
		show_interface()
		acid_string = ask_for_acid()
		
	molar_mass = calculate_molar_mass(acid_string)
	print "molar mass for " + acid_string + " is " + str(molar_mass) + " g/mole."
		
	