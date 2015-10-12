#!/usr/bin/env python
# -*- coding: utf-8 -*-

def insert_country():
    """Here is for that user enter a country for after save a list or dictionary"""
    country = raw_input("Insert a country, please: ")
    print country
    verific_country(country)

def verific_country (country):
    if country.isalpha():
        return True
    else:
        return False




#def user_answer():
    """here is for check te answer number for the option its her/he
    for example option one option two option three"""



if __name__ == '__main__':
    insert_country()