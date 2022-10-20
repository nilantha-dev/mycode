#!/usr/bin/env python3

"""Asks for a country of choice, guess the capital of that country, check the accuracy of that answer"""

from countryinfo import CountryInfo

def main():
    #country
    country = input('Choose a country: ')
    #get the input for capital
    capital_input = input('What is the capital of' + country)
    capital = CountryInfo(country).capital()

    #print
    print(capital)
main()
