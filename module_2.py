# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 00:00:46 2018

@author: Nishna

Task 2 Module
a. View by countries
b. View by continents

"""

class task2a :
    """Class to process task2 a """
    def __init__(self, document_id, datafile) :
        self.__document_id = document_id
        self.__datafile = datafile


    
    def dict_view_by_country(self):
        """ a.Dictionary for View by country"""
        import module_common as cf
        import pandas as pd
        
        """Generate data"""
        view_count = pd.value_counts(cf.common_functions.get_values(self.__datafile,
                                                                    'visitor_country',
                                                                    'subject_doc_id',
                                                                    self.__document_id)).to_frame()['visitor_country']
        """Dictionary which has the data for views by country of the document"""
        country_dict = {view_count.index[i] : view_count[i] for i in range(0,len(view_count))}
        print(country_dict)
        return country_dict
    
    def view_by_country(self, gui = None): 
        """ a. Plot View by country"""
        import plot_functions as pf
        country_dict = self.dict_view_by_country()
        
        """Plot histogram"""
        if(gui is None) :
            pf.plot_functions.plot_hist(country_dict,
                          xlab = "Country",
                          ylab = "Views",
                          title = "Views By Country") 
        else :
            return pf.plot_functions.plot_hist_gui(country_dict,
                          xlab = "Country",
                          ylab = "Views",
                          title = "Views By Country") 
            
        
class task2b :
    """Class to process task2 b """
    __continents = { # dictionary with continent code as key and full name as value
            'AF' : 'Africa',
            'AS' : 'Asia',
            'EU' : 'Europe',
            'NA' : 'North America',
            'SA' : 'South America',
            'OC' : 'Oceania',
            'AN' : 'Antarctica'
            }
    
    __country_to_continent = { # dictionary having the continent mapping for each country
        'AF' : 'AS',
        'AX' : 'EU',
        'AL' : 'EU',
        'DZ' : 'AF',
        'AS' : 'OC',
        'AD' : 'EU',
        'AO' : 'AF',
        'AI' : 'NA',
        'AQ' : 'AN',
        'AG' : 'NA',
        'AR' : 'SA',
        'AM' : 'AS',
        'AW' : 'NA',
        'AU' : 'OC',
        'AT' : 'EU',
        'AZ' : 'AS',
        'BS' : 'NA',
        'BH' : 'AS',
        'BD' : 'AS',
        'BB' : 'NA',
        'BY' : 'EU',
        'BE' : 'EU',
        'BZ' : 'NA',
        'BJ' : 'AF',
        'BM' : 'NA',
        'BT' : 'AS',
        'BO' : 'SA',
        'BQ' : 'NA',
        'BA' : 'EU',
        'BW' : 'AF',
        'BV' : 'AN',
        'BR' : 'SA',
        'IO' : 'AS',
        'VG' : 'NA',
        'BN' : 'AS',
        'BG' : 'EU',
        'BF' : 'AF',
        'BI' : 'AF',
        'KH' : 'AS',
        'CM' : 'AF',
        'CA' : 'NA',
        'CV' : 'AF',
        'KY' : 'NA',
        'CF' : 'AF',
        'TD' : 'AF',
        'CL' : 'SA',
        'CN' : 'AS',
        'CX' : 'AS',
        'CC' : 'AS',
        'CO' : 'SA',
        'KM' : 'AF',
        'CD' : 'AF',
        'CG' : 'AF',
        'CK' : 'OC',
        'CR' : 'NA',
        'CI' : 'AF',
        'HR' : 'EU',
        'CU' : 'NA',
        'CW' : 'NA',
        'CY' : 'AS',
        'CZ' : 'EU',
        'DK' : 'EU',
        'DJ' : 'AF',
        'DM' : 'NA',
        'DO' : 'NA',
        'EC' : 'SA',
        'EG' : 'AF',
        'SV' : 'NA',
        'GQ' : 'AF',
        'ER' : 'AF',
        'EE' : 'EU',
        'ET' : 'AF',
        'FO' : 'EU',
        'FK' : 'SA',
        'FJ' : 'OC',
        'FI' : 'EU',
        'FR' : 'EU',
        'GF' : 'SA',
        'PF' : 'OC',
        'TF' : 'AN',
        'GA' : 'AF',
        'GM' : 'AF',
        'GE' : 'AS',
        'DE' : 'EU',
        'GH' : 'AF',
        'GI' : 'EU',
        'GR' : 'EU',
        'GL' : 'NA',
        'GD' : 'NA',
        'GP' : 'NA',
        'GU' : 'OC',
        'GT' : 'NA',
        'GG' : 'EU',
        'GN' : 'AF',
        'GW' : 'AF',
        'GY' : 'SA',
        'HT' : 'NA',
        'HM' : 'AN',
        'VA' : 'EU',
        'HN' : 'NA',
        'HK' : 'AS',
        'HU' : 'EU',
        'IS' : 'EU',
        'IN' : 'AS',
        'ID' : 'AS',
        'IR' : 'AS',
        'IQ' : 'AS',
        'IE' : 'EU',
        'IM' : 'EU',
        'IL' : 'AS',
        'IT' : 'EU',
        'JM' : 'NA',
        'JP' : 'AS',
        'JE' : 'EU',
        'JO' : 'AS',
        'KZ' : 'AS',
        'KE' : 'AF',
        'KI' : 'OC',
        'KP' : 'AS',
        'KR' : 'AS',
        'KW' : 'AS',
        'KG' : 'AS',
        'LA' : 'AS',
        'LV' : 'EU',
        'LB' : 'AS',
        'LS' : 'AF',
        'LR' : 'AF',
        'LY' : 'AF',
        'LI' : 'EU',
        'LT' : 'EU',
        'LU' : 'EU',
        'MO' : 'AS',
        'MK' : 'EU',
        'MG' : 'AF',
        'MW' : 'AF',
        'MY' : 'AS',
        'MV' : 'AS',
        'ML' : 'AF',
        'MT' : 'EU',
        'MH' : 'OC',
        'MQ' : 'NA',
        'MR' : 'AF',
        'MU' : 'AF',
        'YT' : 'AF',
        'MX' : 'NA',
        'FM' : 'OC',
        'MD' : 'EU',
        'MC' : 'EU',
        'MN' : 'AS',
        'ME' : 'EU',
        'MS' : 'NA',
        'MA' : 'AF',
        'MZ' : 'AF',
        'MM' : 'AS',
        'NA' : 'AF',
        'NR' : 'OC',
        'NP' : 'AS',
        'NL' : 'EU',
        'NC' : 'OC',
        'NZ' : 'OC',
        'NI' : 'NA',
        'NE' : 'AF',
        'NG' : 'AF',
        'NU' : 'OC',
        'NF' : 'OC',
        'MP' : 'OC',
        'NO' : 'EU',
        'OM' : 'AS',
        'PK' : 'AS',
        'PW' : 'OC',
        'PS' : 'AS',
        'PA' : 'NA',
        'PG' : 'OC',
        'PY' : 'SA',
        'PE' : 'SA',
        'PH' : 'AS',
        'PN' : 'OC',
        'PL' : 'EU',
        'PT' : 'EU',
        'PR' : 'NA',
        'QA' : 'AS',
        'RE' : 'AF',
        'RO' : 'EU',
        'RU' : 'EU',
        'RW' : 'AF',
        'BL' : 'NA',
        'SH' : 'AF',
        'KN' : 'NA',
        'LC' : 'NA',
        'MF' : 'NA',
        'PM' : 'NA',
        'VC' : 'NA',
        'WS' : 'OC',
        'SM' : 'EU',
        'ST' : 'AF',
        'SA' : 'AS',
        'SN' : 'AF',
        'RS' : 'EU',
        'SC' : 'AF',
        'SL' : 'AF',
        'SG' : 'AS',
        'SX' : 'NA',
        'SK' : 'EU',
        'SI' : 'EU',
        'SB' : 'OC',
        'SO' : 'AF',
        'ZA' : 'AF',
        'GS' : 'AN',
        'SS' : 'AF',
        'ES' : 'EU',
        'LK' : 'AS',
        'SD' : 'AF',
        'SR' : 'SA',
        'SJ' : 'EU',
        'SZ' : 'AF',
        'SE' : 'EU',
        'CH' : 'EU',
        'SY' : 'AS',
        'TW' : 'AS',
        'TJ' : 'AS',
        'TZ' : 'AF',
        'TH' : 'AS',
        'TL' : 'AS',
        'TG' : 'AF',
        'TK' : 'OC',
        'TO' : 'OC',
        'TT' : 'NA',
        'TN' : 'AF',
        'TR' : 'AS',
        'TM' : 'AS',
        'TC' : 'NA',
        'TV' : 'OC',
        'UG' : 'AF',
        'UA' : 'EU',
        'AE' : 'AS',
        'GB' : 'EU',
        'US' : 'NA',
        'UM' : 'OC',
        'VI' : 'NA',
        'UY' : 'SA',
        'UZ' : 'AS',
        'VU' : 'OC',
        'VE' : 'SA',
        'VN' : 'AS',
        'WF' : 'OC',
        'EH' : 'AF',
        'YE' : 'AS',
        'ZM' : 'AF',
        'ZW' : 'AF'
        }

    
    def __init__(self, document_id, datafile) :
        self.__document_id = document_id
        self.__datafile = datafile

    
    def view_by_continent(self, gui = None):
        """ a. View by continent"""
        import common_functions as cf
        import plot_functions as pf
                
        """Generate data"""
        records = cf.common_functions.get_values(self.__datafile,
                                                 'visitor_country',
                                                 'subject_doc_id',
                                                 self.__document_id).to_frame() # Get the list of records
        records['visitor_continent'] = records['visitor_country'].map(self.__country_to_continent).map(self.__continents) #New Column - Continents
        view_count = records.groupby(['visitor_continent']).size() #Group by continent & get view count 
        country_dict = {view_count.index[i] : view_count[i] for i in range(0,len(view_count))} #Dictionary which has the data for views by country of the document
        
        """Plot histogram"""
        if(gui is None) :
            pf.plot_functions.plot_hist(country_dict,
                          xlab = "Continents",
                          ylab = "Views",
                          title = "Views By Continent") 
        else :
            return pf.plot_functions.plot_hist_gui(country_dict,
                          xlab = "Continents",
                          ylab = "Views",
                          title = "Views By Continent")
               
    