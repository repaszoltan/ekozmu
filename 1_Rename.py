#######################################################################################################################################
#
# E-KÖZMŰ adatszolgáltatás állományainak átnevezése QGIS konvertálás előtt
#
# Répás Zoltán
# 
#######################################################################################################################################

import glob
import os


# Relativ eleresi ut beallitasa a jelen scripttel azonos helyen levo "data" mappa kell lennie az e-kozurol kapott adatoknak.
path = r"data\\"

# Minta keresese az osszetartozo fileokhoz

#######################################################################################################################################
def rename(pattern, shortName):
    global path                                                         #Eleresi ut globalis atvetele
    pattern_dbf = path + "*" + pattern + "*.dbf"                        #Minta kereses elokeszitese a dbf filokban
    pattern_shx = path + "*" + pattern + "*.shx"                        #Minta kereses elokeszitese a shx filokban
    pattern_shp = path + "*" + pattern + "*.shp"                        #Minta kereses elokeszitese a shp filokban

    result_dbf = glob.glob(pattern_dbf)                                 #Lista keszites a feni minta segitsegevel
    result_shx = glob.glob(pattern_shx)                                 #Lista keszites a feni minta segitsegevel
    result_shp = glob.glob(pattern_shp)                                 #Lista keszites a feni minta segitsegevel

    def renameList(list,ext):
        count = 0                                                       # c szamlalo, mert lehet tobb azonos nevuallomany is
        for file_name in list:                                          # Atnevezesek megvalositasa
            old_name = file_name                                        # Ez az eredeti file nevet veszik ki a listabol
            if count == 0:                                              # Elso korben sima atnevezes tortenik
                new_name = path + shortName + ext
                os.rename(old_name, new_name)
            else:                                                       #Ha egynel tobb allomany van akkor a tobbi _ sorszamot kap
                new_name = path + shortName + '_' + str(count) + ext
                os.rename(old_name, new_name)
            count = count + 1                                           #Szamlalo leptetese
    
    renameList(result_dbf, '.dbf')
    renameList(result_shx, '.shx')
    renameList(result_shp, '.shp')

#######################################################################################################################################
# Itt indul az egyes lehetosegek felsorolasa

rename('el1_', 'Villamos_energia')
rename('sz1_', 'Gazvezetek')
rename('vi1_', 'Vizvezetek')
rename('ve1_', 'Vizelvezetes')
rename('th1_', 'Tavho')
rename('*_102_*hi1_', 'MagyarTelekom')
rename('*_210_*hi1_', 'DIGI')
rename('*_73_*hi1_', 'Vidanet')
rename('*_48_*hi1_', 'Vodafone')
rename('*_160_*hi1_', 'Invitel')
rename('*_161_*hi1_', 'Invitech')
rename('*_345_*hi1_', 'HirSat2000')
rename('*_44_*hi1_', 'AntennaHungaria')
rename('*_212_*hi1_', 'KabelSzatnet')
