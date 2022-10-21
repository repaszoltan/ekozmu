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
A kapott adatszolgáltatástartalmát ki kell csomagolni a "data" könyvtárba.
