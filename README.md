# E-közmű shape --> DXF konverzió
Az E-közmű adatszolgáltatás SHP állományait formázott DXF állományba konvertálja Python és QGIS segítségével.

<h2>Disclaimer:</h2>
Kezdjük azzal, hogy ez a megoldás igen kezdetleges, erősen a saját tervezői igényeim kielégítésére született, elég nagy overheadbenne, hogy telepített python és QGIS kell a használatához. Emellett ha mégis hasznosnak találja valaki örömmel veszem haerről visszajelzést is ad, esetleg beszáll egy jobb verzió kidolgozásába.

<h2>Használati utasítás</h2>
Az https://ekozmu.e-epites.hu oldalról vásárolható adatszolgáltatás tartalmazza az adatokat SHP formátumban leíró adatokkal, valamint egy csak a topológiát tartalmazó DXF file-ban. Előbbi nem alkalmas közvetlenül a CAD-es szoftverekben való használatra, utóbbi adattartalma elégtelen.<br>
Szükséges lenne egyolyan lehetőleg nyílt forrású programami átalakítja CAD-es formába az SHP adatokat. Mivel ezt önálló programként nem tudtam elkészíteni, egy kis kerülőútraindultam, ennek a lépéseit mutatom bealább.
<h3>Környezet előkészítése</h3>
Szükséges,hogy legyen a python3 telepítve a rendszeren. (https://www.python.org/downloads/)
QGIS-re isszükség lesz, valamelyik friss LTR verzió javasolt. (https://www.qgis.org/en/site/forusers/download.html)
<h3>1. lépés</h3>
A 1_Rename.py és 2_pyQgis_ekozmu_1.2.py scripteket le kell menteni egy tetszőleges helyre<br>
Létre kell hozni egy "data" nevű köyvtárat.<br>
A 2_pyQgis_ekozmu_1.2.py állományban a "path" változónál lévő elérési utat szerkeszteni kell, hogy a fent említett "data"mappáramutasson.
A kapott adatszolgáltatástartalmát ki kell csomagolni a "data" könyvtárba.
<h3>2. lépés</h3>
A 1_Rename.py scriptet le kell futtatni, hogy az adatszolgáltatás nyomvonalas shp állományait átnevezze, a következő lépés előkészítéseképp.
<h3>3. lépés</h3>
Meg kell nyitni egy QGIS projektet, beállítani a HD72/EOV vetületet és megnyitni a "data" mappa átnevezett shp állományait. Ezután a Modulok menü/Python konzol vagy (Ctrl+Alt+P) megnyitása szükséges. Itt kell kiválasztani a 2_pyQgis_ekozmu_1.2.py scriptet és futtatni.<br>
Ha minden jól ment, eltűntek a korábbi rétegek és létrejöttek az új leválogatott állományok. <br>
A távközlési szolgáltatók listája közel sem teljes, azok szerepelnek csak benne akikkel eddig dolgom volt. A bővítésre jöhetnek javaslatok:)
<h3>3+1. lépés</h3>
Opcionális: A Vektor/Geoprocessing eszközök/Övezet segítségével a szénhidrogén vezeték 2m-es védőövezetét elő lehet állítani, engedélyeztetéskor általában megkövetelik. Fontos, hogy a vezeték rétege is HD72/EOV legyen, különben helytelenül fog megjelenni az eredmény.
<h3>4. lépés</h3>
A Projekt/Importálás Exportálás/Exportálás DXF formátumba lehetőséggel DXF-be mentjük a projekt tartalmát. Akár mentés nélkül be is zárhatjuk a QGIS-t, elvégezte a dolgát:)
<h3>5. lépés</h3>
Az exportlált DXF-et megnyitva, a tartalmát fólia típusra, globális szélességeket 0-ra kell állítani majd az összes vonallánát átmásolni a sablon rajzba.<br>
A sablon rajz a Magyar Mérnöki Kamara Geodéziai és Geoinformatika Tagozata által kiadott rétegrendet tartalmazza: GGT_sablon_V1.6_2000.dxf<br>
Ebben a rajzban már megfelelő vonaltípusokkal színekkel jelennek meg a közmű nyomvonal adatok. Ha vonaltípusok nem jelennének meg, a repóban ezek is mellékelve vannak.
