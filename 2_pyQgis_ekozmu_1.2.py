#E-kozmu adatszolgaltatast feldolgozo script
#
# Eleresi ut beallitasa, hogy hova exportaljon a script. (eleg kezdetleges, de lesz ez jobb is)
#path = "c:/Users/DELL2/Komtel/repasz/Felhő/Sablonok/E-kozmu/shp2dxf/data"
path = "d:/Felho/RZoli/Sablonok/E-kozmu/shp2dxf/data"
#
# Reteg eltavolito fuggveny
def removeLayers(layerName):
    for layer in QgsProject.instance().mapLayers().values():
        if layer.name()==layerName:
            QgsProject.instance().removeMapLayers( [layer.id()] )
#
#Elektromos vezetek#############################################################################################################
try:
    layers_vi = QgsProject.instance().mapLayersByName('Villamos_energia')
    layer = layers_vi[0]
    #
    #KIF földkabel
    layer.selectByExpression('"V_SZALLMOD"=2 AND "V_ELHMOD"=2')
    #Uj reteg letrehozasa
    fn_kif_fa = path + "/EKOZM_ELEKTROMOS_VEZ_FOLD_KIF.shp"
    writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn_kif_fa, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
    selected_layer = iface.addVectorLayer(fn_kif_fa, '', 'ogr')
    del (writer)
    #KOF földkabel
    layer.selectByExpression('"V_SZALLMOD"=1 AND "V_ELHMOD"=2')
    #Uj reteg letrehozasa
    fn_kof_fa = path + "/EKOZM_ELEKTROMOS_VEZ_FOLD_KOF.shp"
    writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn_kof_fa, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
    selected_layer = iface.addVectorLayer(fn_kof_fa, '', 'ogr')
    del (writer)
    #NAF földkabel
    layer.selectByExpression('"V_SZALLMOD"=3 AND "V_ELHMOD"=2')
    #Uj reteg letrehozasa
    fn_naf_fa = path + "/EKOZM_ELEKTROMOS_VEZ_FOLD_NAF.shp"
    writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn_naf_fa, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
    selected_layer = iface.addVectorLayer(fn_naf_fa, '', 'ogr')
    del (writer)
    #
    #KIF legkabel
    layer.selectByExpression('"V_SZALLMOD"=2 AND "V_ELHMOD"=1')
    #Uj reteg letrehozasa
    fn_kif_ff = path + "/EKOZM_ELEKTROMOS_VEZ_LEG_KIF.shp"
    writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn_kif_ff, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
    selected_layer = iface.addVectorLayer(fn_kif_ff, '', 'ogr')
    del (writer)
    #KOF legkabel
    layer.selectByExpression('"V_SZALLMOD"=1 AND "V_ELHMOD"=1')
    #Uj reteg letrehozasa
    fn_kof_ff = path + "/EKOZM_ELEKTROMOS_VEZ_LEG_KOF.shp"
    writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn_kof_ff, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
    selected_layer = iface.addVectorLayer(fn_kof_ff, '', 'ogr')
    del (writer)
    #NAF legkabel
    layer.selectByExpression('"V_SZALLMOD"=3 AND "V_ELHMOD"=1')
    #Uj reteg letrehozasa
    fn_naf_ff = path + "/EKOZM_ELEKTROMOS_VEZ_LEG_NAF.shp"
    writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn_naf_ff, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
    selected_layer = iface.addVectorLayer(fn_naf_ff, '', 'ogr')
    del (writer)
    removeLayers('Villamos_energia')
    #
except:
    print("Nincs ilyen layer")

#Vizvezetek, csak nevet valtztatunk#############################################################################################
try:
    layers_vi = QgsProject.instance().mapLayersByName('Vizvezetek')
    layer = layers_vi[0]
    layer.selectByExpression('"V_SZALLKOZ">=1')

    #Uj reteg letrehozasa
    fn_ve = path + "/EKOZM_VIZELLATAS_VEZETEK.shp"
    writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn_ve, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
    selected_layer = iface.addVectorLayer(fn_ve, '', 'ogr')
    del (writer)
    removeLayers('Vizvezetek')
except:
    print("Nincs ilyen layer")

#Vizvezetek, szennyviz es csapadekviz retegre kell osztani######################################################################
try:
    layers_ve = QgsProject.instance().mapLayersByName('Vizelvezetes')
    layer = layers_ve[0]
    layer.selectByExpression('"V_SZALLKOZ"=1 OR "V_SZALLKOZ"=2 ')

    fn_sz = path + "/EKOZM_VIZELVEZETES_SZ_VEZ.shp"
    writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn_sz, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
    selected_layer = iface.addVectorLayer(fn_sz, '', 'ogr')
    del (writer)

    layer.selectByExpression('"V_SZALLKOZ"=3 OR "V_SZALLKOZ"=4 OR "V_SZALLKOZ"=5')

    fn_cs = path + "/EKOZM_VIZELVEZETES_CS_VEZ.shp"
    writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn_cs, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
    selected_layer = iface.addVectorLayer(fn_cs, '', 'ogr')
    del (writer)
    removeLayers('Vizelvezetes')
except:
    print ("Nincs ilyen layer")

#Gazvezetek, csak nevet valtztatunk############################################################################################
try:
    layers_sz = QgsProject.instance().mapLayersByName('Gazvezetek')
    layer = layers_sz[0]
    layer.selectByExpression('"V_SZALLKOZ">=1')

    #Uj reteg letrehozasa
    fn_sz = path + "/EKOZM_SZENHIDROGEN_VEZ.shp"
    writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn_sz, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
    selected_layer = iface.addVectorLayer(fn_sz, '', 'ogr')
    del (writer)
    removeLayers('Gazvezetek')
except:
    print("Nincs ilyen layer")

#Tavho, fold feletti es fold alatti retegekre osztjuk##########################################################################
###Itt problema van a "V_ELHMOD" attributum mezovel, van, hogyhianyzik###
try:
    layers_th = QgsProject.instance().mapLayersByName('Tavho')
    layer = layers_th[0]
    #V_SZALLMOD ellenorzese
    layer.selectByExpression('"V_SZALLMOD"=1 AND "V_SZALLMOD"=2')
    szamlalo = layer.selectedFeatureCount()
    print (szamlalo)
    #Ha nem szerepel V_SZALLMOD bejegyzes, akkor a tavhot egy retegre kell kiirni, ha szerepel, akkor FF és FA retegekre
    if szamlalo == 0:
        #Uj reteg letrehozasa
        fn_th = path + "/EKOZM_TAVHO_HIBAS_LEKERDEZES.shp"
        writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn_th, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
        selected_layer = iface.addVectorLayer(fn_th, '', 'ogr')
        del (writer)
        print("Hianyzo V_SZALLMOD attributumok!")
    else:
        #Fold feletti lekerdezese
        layer.selectByExpression('"V_SZALLMOD"=1')

        #Uj reteg letrehozasa
        fn_th = path + "/EKOZM_TAVHO_VEZ_FF.shp"
        writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn_th, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
        selected_layer = iface.addVectorLayer(fn_th, '', 'ogr')
        del (writer)

        #Fold alatti lekerdezese
        layer.selectByExpression('"V_ELHMOD"=2')

        #Uj reteg letrehozasa
        fn_th = path + "/EKOZM_TAVHO_VEZ_FA.shp"
        writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn_th, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
        selected_layer = iface.addVectorLayer(fn_th, '', 'ogr')
        del (writer)
    removeLayers('Tavho')
except:
    print("Nincs ilyen layer")

#Tavkozles, cegenkent #########################################################################################################
# Magyar Telekom #######################################################
try:
    layers_ve = QgsProject.instance().mapLayersByName('MagyarTelekom')
    layer = layers_ve[0]
    layer.selectByExpression('"V_ELHMOD"=1 ')

    fn_sz = path + "/EKOZM_HIRKOZLES_VEZ_FF_MagyarTelekom.shp"
    writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn_sz, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
    selected_layer = iface.addVectorLayer(fn_sz, '', 'ogr')
    del (writer)

    layer.selectByExpression('"V_ELHMOD"=2 OR "V_ELHMOD"=3')

    fn_cs = path + "/EKOZM_HIRKOZLES_VEZ_FA_MagyarTelekom.shp"
    writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn_cs, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
    selected_layer = iface.addVectorLayer(fn_cs, '', 'ogr')
    del (writer)
    removeLayers('MagyarTelekom')
except:
    print ("Nincs ilyen layer")
# Digi ###############################################################
try:
    layers_ve = QgsProject.instance().mapLayersByName('DIGI')
    layer = layers_ve[0]
    layer.selectByExpression('"V_ELHMOD"=1 ')

    fn_sz = path + "/EKOZM_HIRKOZLES_VEZ_FF_DIGI.shp"
    writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn_sz, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
    selected_layer = iface.addVectorLayer(fn_sz, '', 'ogr')
    del (writer)

    layer.selectByExpression('"V_ELHMOD"=2 OR "V_ELHMOD"=3')

    fn_cs = path + "/EKOZM_HIRKOZLES_VEZ_FA_DIGI.shp"
    writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn_cs, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
    selected_layer = iface.addVectorLayer(fn_cs, '', 'ogr')
    del (writer)
    removeLayers('DIGI')
except:
    print ("Nincs ilyen layer")
# Vidanet ###############################################################
try:
    layers_ve = QgsProject.instance().mapLayersByName('Vidanet')
    layer = layers_ve[0]
    layer.selectByExpression('"V_ELHMOD"=1 ')

    fn_sz = path + "/EKOZM_HIRKOZLES_VEZ_FF_Vidanet.shp"
    writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn_sz, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
    selected_layer = iface.addVectorLayer(fn_sz, '', 'ogr')
    del (writer)

    layer.selectByExpression('"V_ELHMOD"=2 OR "V_ELHMOD"=3')

    fn_cs = path + "/EKOZM_HIRKOZLES_VEZ_FA_Vidanet.shp"
    writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn_cs, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
    selected_layer = iface.addVectorLayer(fn_cs, '', 'ogr')
    del (writer)
    removeLayers('Vidanet')
except:
    print ("Nincs ilyen layer")
# Vodafone ###############################################################
try:
    layers_ve = QgsProject.instance().mapLayersByName('Vodafone')
    layer = layers_ve[0]
    layer.selectByExpression('"V_ELHMOD"=1 ')

    fn_sz = path + "/EKOZM_HIRKOZLES_VEZ_FF_Vodafone.shp"
    writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn_sz, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
    selected_layer = iface.addVectorLayer(fn_sz, '', 'ogr')
    del (writer)

    layer.selectByExpression('"V_ELHMOD"=2 OR "V_ELHMOD"=3')

    fn_cs = path + "/EKOZM_HIRKOZLES_VEZ_FA_Vodafone.shp"
    writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn_cs, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
    selected_layer = iface.addVectorLayer(fn_cs, '', 'ogr')
    del (writer)
    removeLayers('Vodafone')
except:
    print ("Nincs ilyen layer")
# Invitel ###############################################################
try:
    layers_ve = QgsProject.instance().mapLayersByName('Invitel')
    layer = layers_ve[0]
    layer.selectByExpression('"V_ELHMOD"=1 ')

    fn_sz = path + "/EKOZM_HIRKOZLES_VEZ_FF_Invitel.shp"
    writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn_sz, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
    selected_layer = iface.addVectorLayer(fn_sz, '', 'ogr')
    del (writer)

    layer.selectByExpression('"V_ELHMOD"=2 OR "V_ELHMOD"=3')

    fn_cs = path + "/EKOZM_HIRKOZLES_VEZ_FA_Invitel.shp"
    writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn_cs, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
    selected_layer = iface.addVectorLayer(fn_cs, '', 'ogr')
    del (writer)
    removeLayers('Invitel')
except:
    print ("Nincs ilyen layer")
# Invitech ###############################################################
try:
    layers_ve = QgsProject.instance().mapLayersByName('Invitech')
    layer = layers_ve[0]
    layer.selectByExpression('"V_ELHMOD"=1 ')

    fn_sz = path + "/EKOZM_HIRKOZLES_VEZ_FF_Invitech.shp"
    writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn_sz, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
    selected_layer = iface.addVectorLayer(fn_sz, '', 'ogr')
    del (writer)

    layer.selectByExpression('"V_ELHMOD"=2 OR "V_ELHMOD"=3')

    fn_cs = path + "/EKOZM_HIRKOZLES_VEZ_FA_Invitech.shp"
    writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn_cs, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
    selected_layer = iface.addVectorLayer(fn_cs, '', 'ogr')
    del (writer)
    removeLayers('Invitech')
except:
    print ("Nincs ilyen layer")
# HirSat ###############################################################
try:
    layers_ve = QgsProject.instance().mapLayersByName('HirSat')
    layer = layers_ve[0]
    layer.selectByExpression('"V_ELHMOD"=1 ')

    fn_sz = path + "/EKOZM_HIRKOZLES_VEZ_FF_HirSat.shp"
    writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn_sz, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
    selected_layer = iface.addVectorLayer(fn_sz, '', 'ogr')
    del (writer)

    layer.selectByExpression('"V_ELHMOD"=2 OR "V_ELHMOD"=3')

    fn_cs = path + "/EKOZM_HIRKOZLES_VEZ_FA_HirSat.shp"
    writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn_cs, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
    selected_layer = iface.addVectorLayer(fn_cs, '', 'ogr')
    del (writer)
    removeLayers('HirSat')
except:
    print ("Nincs ilyen layer")
# AntennaHungaria ###############################################################
try:
    layers_ve = QgsProject.instance().mapLayersByName('AntennaHungaria')
    layer = layers_ve[0]
    layer.selectByExpression('"V_ELHMOD"=1 ')

    fn_sz = path + "/EKOZM_HIRKOZLES_VEZ_FF_AntennaHungaria.shp"
    writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn_sz, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
    selected_layer = iface.addVectorLayer(fn_sz, '', 'ogr')
    del (writer)

    layer.selectByExpression('"V_ELHMOD"=2 OR "V_ELHMOD"=3')

    fn_cs = path + "/EKOZM_HIRKOZLES_VEZ_FA_AntennaHungaria.shp"
    writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn_cs, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
    selected_layer = iface.addVectorLayer(fn_cs, '', 'ogr')
    del (writer)
    removeLayers('Antenna')
except:
    print ("Nincs ilyen layer")
# KabelszatNet ###############################################################
try:
    layers_ve = QgsProject.instance().mapLayersByName('KabelszatNet')
    layer = layers_ve[0]
    layer.selectByExpression('"V_ELHMOD"=1 ')

    fn_sz = path + "/EKOZM_HIRKOZLES_VEZ_FF_KabelszatNet.shp"
    writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn_sz, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
    selected_layer = iface.addVectorLayer(fn_sz, '', 'ogr')
    del (writer)

    layer.selectByExpression('"V_ELHMOD"=2 OR "V_ELHMOD"=3')

    fn_cs = path + "/EKOZM_HIRKOZLES_VEZ_FA_KabelszatNet.shp"
    writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn_cs, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
    selected_layer = iface.addVectorLayer(fn_cs, '', 'ogr')
    del (writer)
    removeLayers('KabelszatNet')
except:
    print ("Nincs ilyen layer")
# MicroWave ###############################################################
try:
    layers_ve = QgsProject.instance().mapLayersByName('MicroWave')
    layer = layers_ve[0]
    layer.selectByExpression('"V_ELHMOD"=1 ')

    fn_sz = path + "/EKOZM_HIRKOZLES_VEZ_FF_MicroWave.shp"
    writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn_sz, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
    selected_layer = iface.addVectorLayer(fn_sz, '', 'ogr')
    del (writer)

    layer.selectByExpression('"V_ELHMOD"=2 OR "V_ELHMOD"=3')

    fn_cs = path + "/EKOZM_HIRKOZLES_VEZ_FA_MicroWave.shp"
    writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn_cs, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
    selected_layer = iface.addVectorLayer(fn_cs, '', 'ogr')
    del (writer)
    removeLayers('MicroWave')
except:
    print ("Nincs ilyen layer")
