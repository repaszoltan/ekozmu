import glob
import os

# Hosszu nevek redukalasa egyseges elnevezesre

# Relativ eleresi ut beallitasa a jelen scripttel azonos helyen levo "data" mappa kell lennie az e-kozurol kapott adatoknak.
path = r"data\\"

# Minta keresese az osszetartozo fileokhoz

#1. Elektromos szekcio############################################################
# A el1 keresese a file neveben
pattern_dbf = path + "*" + "el1" + "*.dbf"
pattern_shx = path + "*" + "el1" + "*.shx"
pattern_shp = path + "*" + "el1" + "*.shp"
# Lista keszites az illeszkedo fileokrol
result_dbf = glob.glob(pattern_dbf)
result_shx = glob.glob(pattern_shx)
result_shp = glob.glob(pattern_shp)
# Atnevezesek megvalositasa
for file_name in result_dbf:
    old_name = file_name
    new_name = path + 'Villamos_energia' + ".dbf"
    os.rename(old_name, new_name)
    
for file_name in result_shx:
    old_name = file_name
    new_name = path + 'Villamos_energia' + ".shx"
    os.rename(old_name, new_name)
    
for file_name in result_shp:
    old_name = file_name
    new_name = path + 'Villamos_energia' + ".shp"
    os.rename(old_name, new_name)

#2. Hirkozlesi szekcio############################################################

##### A Telekom keresese a file neveben
pattern_dbf = path + "*_102_*" + "hi1" + "*.dbf"
pattern_shx = path + "*_102_*" + "hi1" + "*.shx"
pattern_shp = path + "*_102_*" + "hi1" "*.shp"
# Lista keszites az illeszkedo fileokrol
result_dbf = glob.glob(pattern_dbf)
result_shx = glob.glob(pattern_shx)
result_shp = glob.glob(pattern_shp)
# Atnevezesek megvalositasa
for file_name in result_dbf:
    old_name = file_name
    new_name = path + 'MagyarTelekom' + ".dbf"
    os.rename(old_name, new_name)
    
for file_name in result_shx:
    old_name = file_name
    new_name = path + 'MagyarTelekom' + ".shx"
    os.rename(old_name, new_name)
    
for file_name in result_shp:
    old_name = file_name
    new_name = path + 'MagyarTelekom' + ".shp"
    os.rename(old_name, new_name)
##### A DIGI keresese a file neveben
pattern_dbf = path + "*_210_*" + "hi1" + "*.dbf"
pattern_shx = path + "*_210_*" + "hi1" + "*.shx"
pattern_shp = path + "*_210_*" + "hi1" + "*.shp"
# Lista keszites az illeszkedo fileokrol
result_dbf = glob.glob(pattern_dbf)
result_shx = glob.glob(pattern_shx)
result_shp = glob.glob(pattern_shp)
# Atnevezesek megvalositasa
for file_name in result_dbf:
    old_name = file_name
    new_name = path + 'DIGI' + ".dbf"
    os.rename(old_name, new_name)
    
for file_name in result_shx:
    old_name = file_name
    new_name = path + 'DIGI' + ".shx"
    os.rename(old_name, new_name)
    
for file_name in result_shp:
    old_name = file_name
    new_name = path + 'DIGI' + ".shp"
    os.rename(old_name, new_name)
##### A Vidanet keresese a file neveben
pattern_dbf = path + "*_73_*" + "hi1" + "*.dbf"
pattern_shx = path + "*_73_*" + "hi1" + "*.shx"
pattern_shp = path + "*_73_*" + "hi1" + "*.shp"
# Lista keszites az illeszkedo fileokrol
result_dbf = glob.glob(pattern_dbf)
result_shx = glob.glob(pattern_shx)
result_shp = glob.glob(pattern_shp)
# Atnevezesek megvalositasa
for file_name in result_dbf:
    old_name = file_name
    new_name = path + 'Vidanet' + ".dbf"
    os.rename(old_name, new_name)
    
for file_name in result_shx:
    old_name = file_name
    new_name = path + 'Vidanet' + ".shx"
    os.rename(old_name, new_name)
    
for file_name in result_shp:
    old_name = file_name
    new_name = path + 'Vidanet' + ".shp"
    os.rename(old_name, new_name)
##### A Vodafone keresese a file neveben
pattern_dbf = path + "*_48_*" + "hi1" + "*.dbf"
pattern_shx = path + "*_48_*" + "hi1" + "*.shx"
pattern_shp = path + "*_48_*" + "hi1" + "*.shp"
# Lista keszites az illeszkedo fileokrol
result_dbf = glob.glob(pattern_dbf)
result_shx = glob.glob(pattern_shx)
result_shp = glob.glob(pattern_shp)
# Atnevezesek megvalositasa
for file_name in result_dbf:
    old_name = file_name
    new_name = path + 'Vodafone' + ".dbf"
    os.rename(old_name, new_name)
    
for file_name in result_shx:
    old_name = file_name
    new_name = path + 'Vodafone' + ".shx"
    os.rename(old_name, new_name)
    
for file_name in result_shp:
    old_name = file_name
    new_name = path + 'Vodafone' + ".shp"
    os.rename(old_name, new_name)
##### Az Invitel keresese a file neveben
pattern_dbf = path + "*_160_*" + "hi1" + "*.dbf"
pattern_shx = path + "*_160_*" + "hi1" + "*.shx"
pattern_shp = path + "*_160_*" + "hi1" + "*.shp"
# Lista keszites az illeszkedo fileokrol
result_dbf = glob.glob(pattern_dbf)
result_shx = glob.glob(pattern_shx)
result_shp = glob.glob(pattern_shp)
# Atnevezesek megvalositasa
for file_name in result_dbf:
    old_name = file_name
    new_name = path + 'Invitel' + ".dbf"
    os.rename(old_name, new_name)
    
for file_name in result_shx:
    old_name = file_name
    new_name = path + 'Invitel' + ".shx"
    os.rename(old_name, new_name)
    
for file_name in result_shp:
    old_name = file_name
    new_name = path + 'Invitel' + ".shp"
    os.rename(old_name, new_name)
##### Az Invitech keresese a file neveben
pattern_dbf = path + "*_161_*" + "hi1" + "*.dbf"
pattern_shx = path + "*_161_*" + "hi1" + "*.shx"
pattern_shp = path + "*_161_*" + "hi1" + "*.shp"
# Lista keszites az illeszkedo fileokrol
result_dbf = glob.glob(pattern_dbf)
result_shx = glob.glob(pattern_shx)
result_shp = glob.glob(pattern_shp)
# Atnevezesek megvalositasa
for file_name in result_dbf:
    old_name = file_name
    new_name = path + 'Invitech' + ".dbf"
    os.rename(old_name, new_name)
    
for file_name in result_shx:
    old_name = file_name
    new_name = path + 'Invitech' + ".shx"
    os.rename(old_name, new_name)
    
for file_name in result_shp:
    old_name = file_name
    new_name = path + 'Invitech' + ".shp"
    os.rename(old_name, new_name)
##### A HirSat2000 keresese a file neveben
pattern_dbf = path + "*_345_*" + "hi1" + "*.dbf"
pattern_shx = path + "*_345_*" + "hi1" + "*.shx"
pattern_shp = path + "*_345_*" + "hi1" + "*.shp"
# Lista keszites az illeszkedo fileokrol
result_dbf = glob.glob(pattern_dbf)
result_shx = glob.glob(pattern_shx)
result_shp = glob.glob(pattern_shp)
# Atnevezesek megvalositasa
for file_name in result_dbf:
    old_name = file_name
    new_name = path + 'HirSat2000' + ".dbf"
    os.rename(old_name, new_name)
    
for file_name in result_shx:
    old_name = file_name
    new_name = path + 'HirSat2000' + ".shx"
    os.rename(old_name, new_name)
    
for file_name in result_shp:
    old_name = file_name
    new_name = path + 'HirSat2000' + ".shp"
    os.rename(old_name, new_name)
##### Az AntennaHungaria keresese a file neveben
pattern_dbf = path + "*_44_*" + "hi1" + "*.dbf"
pattern_shx = path + "*_44_*" + "hi1" + "*.shx"
pattern_shp = path + "*_44_*" + "hi1" + "*.shp"
# Lista keszites az illeszkedo fileokrol
result_dbf = glob.glob(pattern_dbf)
result_shx = glob.glob(pattern_shx)
result_shp = glob.glob(pattern_shp)
# Atnevezesek megvalositasa
for file_name in result_dbf:
    old_name = file_name
    new_name = path + 'AntennaHungaria' + ".dbf"
    os.rename(old_name, new_name)
    
for file_name in result_shx:
    old_name = file_name
    new_name = path + 'AntennaHungaria' + ".shx"
    os.rename(old_name, new_name)
    
for file_name in result_shp:
    old_name = file_name
    new_name = path + 'AntennaHungaria' + ".shp"
    os.rename(old_name, new_name)
##### A KabelSzatnet keresese a file neveben
pattern_dbf = path + "*_212_*" + "hi1" + "*.dbf"
pattern_shx = path + "*_212_*" + "hi1" + "*.shx"
pattern_shp = path + "*_212_*" + "hi1" + "*.shp"
# Lista keszites az illeszkedo fileokrol
result_dbf = glob.glob(pattern_dbf)
result_shx = glob.glob(pattern_shx)
result_shp = glob.glob(pattern_shp)
# Atnevezesek megvalositasa
for file_name in result_dbf:
    old_name = file_name
    new_name = path + 'KabelSzatnet' + ".dbf"
    os.rename(old_name, new_name)
    
for file_name in result_shx:
    old_name = file_name
    new_name = path + 'KabelSzatnet' + ".shx"
    os.rename(old_name, new_name)
    
for file_name in result_shp:
    old_name = file_name
    new_name = path + 'KabelSzatnet' + ".shp"
    os.rename(old_name, new_name)





#3. Szenhidogen szekcio############################################################
# A sz1 keresese a file neveben
pattern_dbf = path + "*" + "sz1" + "*.dbf"
pattern_shx = path + "*" + "sz1" + "*.shx"
pattern_shp = path + "*" + "sz1" + "*.shp"
# Lista keszites az illeszkedo fileokrol
result_dbf = glob.glob(pattern_dbf)
result_shx = glob.glob(pattern_shx)
result_shp = glob.glob(pattern_shp)
# Atnevezesek megvalositasa
for file_name in result_dbf:
    old_name = file_name
    new_name = path + 'Gazvezetek' + ".dbf"
    os.rename(old_name, new_name)
    
for file_name in result_shx:
    old_name = file_name
    new_name = path + 'Gazvezetek' + ".shx"
    os.rename(old_name, new_name)
    
for file_name in result_shp:
    old_name = file_name
    new_name = path + 'Gazvezetek' + ".shp"
    os.rename(old_name, new_name)
    
#4. Tavho szekcio####################################################################
# A sz1 keresese a file neveben
pattern_dbf = path + "*" + "th1" + "*.dbf"
pattern_shx = path + "*" + "th1" + "*.shx"
pattern_shp = path + "*" + "th1" + "*.shp"
# Lista keszites az illeszkedo fileokrol
result_dbf = glob.glob(pattern_dbf)
result_shx = glob.glob(pattern_shx)
result_shp = glob.glob(pattern_shp)
# Atnevezesek megvalositasa
for file_name in result_dbf:
    old_name = file_name
    new_name = path + 'Tavho' + ".dbf"
    os.rename(old_name, new_name)
    
for file_name in result_shx:
    old_name = file_name
    new_name = path + 'Tavho' + ".shx"
    os.rename(old_name, new_name)
    
for file_name in result_shp:
    old_name = file_name
    new_name = path + 'Tavho' + ".shp"
    os.rename(old_name, new_name)

#5. Vizelvezetes szekcio#############################################################
# A ve1 keresese a file neveben
pattern_dbf = path + "*" + "ve1" + "*.dbf"
pattern_shx = path + "*" + "ve1" + "*.shx"
pattern_shp = path + "*" + "ve1" + "*.shp"
# Lista keszites az illeszkedo fileokrol
result_dbf = glob.glob(pattern_dbf)
result_shx = glob.glob(pattern_shx)
result_shp = glob.glob(pattern_shp)
# Atnevezesek megvalositasa
for file_name in result_dbf:
    old_name = file_name
    new_name = path + 'Vizelvezetes' + ".dbf"
    os.rename(old_name, new_name)
    
for file_name in result_shx:
    old_name = file_name
    new_name = path + 'Vizelvezetes' + ".shx"
    os.rename(old_name, new_name)
    
for file_name in result_shp:
    old_name = file_name
    new_name = path + 'Vizelvezetes' + ".shp"
    os.rename(old_name, new_name)
   
#6. Vizvezetek szekcio###############################################################
# A vi1 keresese a file neveben
pattern_dbf = path + "*" + "vi1" + "*.dbf"
pattern_shx = path + "*" + "vi1" + "*.shx"
pattern_shp = path + "*" + "vi1" + "*.shp"
# Lista keszites az illeszkedo fileokrol
result_dbf = glob.glob(pattern_dbf)
result_shx = glob.glob(pattern_shx)
result_shp = glob.glob(pattern_shp)
# Atnevezesek megvalositasa

for file_name in result_dbf:
    old_name = file_name
    new_name = path + 'Vizvezetek' + ".dbf"
    os.rename(old_name, new_name)
    
for file_name in result_shx:
    old_name = file_name
    new_name = path + 'Vizvezetek' + ".shx"
    os.rename(old_name, new_name)
    
for file_name in result_shp:
    old_name = file_name
    new_name = path + 'Vizvezetek' + ".shp"
    os.rename(old_name, new_name)
    

 

# Logolashoz
res = glob.glob(path + "*" + "1" + "*")
for name in res:
    print(name)