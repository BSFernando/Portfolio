from qgis.core import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qgis.utils import *
import time
import sys
sys.path.append(r'qgis')
from dicionario import *

arquivos = os.listdir(r'qgis')
arquivos_shp = [arq for arq in arquivos if arq[-4:] == '.shp']

for arq in arquivos_shp:

    for at in atri_dic.keys():
        QgsProject.instance().clear()
        path = "qgis/" + arq
        vlayer = QgsVectorLayer(path, atri_dic[at][6])
        project = QgsProject.instance()
        project.addMapLayer(vlayer)
        layer = iface.activeLayer()
        features = layer.getFeatures()
        

        areatot = 0
        area1,area2, area3, area4, area5, area6 = 0,0,0,0,0,0
        
        if at not in ['C_Superfic','C_SubSuper','C_Compacta','C_Argila','Class_Fina']:

            for elem in features:
                if at in ['P'] and elem['ARGILA'] < 250:
                    primeiro = atri_dic[at][0][0]
                    segundo_1, segundo_2 = atri_dic[at][1][0], atri_dic[at][1][1]
                    terceiro_1, terceiro_2 = atri_dic[at][2][0], atri_dic[at][2][1]
                    quarto_1, quarto_2 = atri_dic[at][3][0], atri_dic[at][3][1]
                    quinto_1, quinto_2 = atri_dic[at][4][0], atri_dic[at][4][1]
                    sexto = atri_dic[at][5][0]
                else:
                    primeiro = atri_dic[at][0][0]
                    segundo_1, segundo_2 = atri_dic[at][1][0], atri_dic[at][1][1]
                    terceiro_1, terceiro_2 = atri_dic[at][2][0], atri_dic[at][2][1]
                    quarto_1, quarto_2 = atri_dic[at][3][0], atri_dic[at][3][1]
                    quinto_1, quinto_2 = atri_dic[at][4][0], atri_dic[at][4][1]
                    sexto = atri_dic[at][5][0]

                geom = elem.geometry()
                areatot = areatot + geom.area()
  
                
        area1_porc = round((area1 / areatot) * 100,2)
        area2_porc = round((area2 / areatot) * 100,2)
        area3_porc = round((area3 / areatot) * 100,2)
        area4_porc = round((area4 / areatot) * 100,2)
        area5_porc = round((area5 / areatot) * 100,2)
        area6_porc = round((area6 / areatot) * 100,2)
            
        cores = ['darkGreen','#6ac84b', 'yellow', '#ff681c','red']


        if at in ['AL','CA','MG','M%', 'MOS','MO_2','K','S','AL_2','M%_2','CA_2','MG_2',
                'K_2','S_2','CTC_PH7_2', 'CTC_EFET_1','CTC_PH7','CTC_EFETIV']:
            values_lista = [
                ('(< ' + str(primeiro) + ') - Muito baixo | ' + str(round(area1/10000,2)) + ' ha (' + str(area1_porc) + '%)', 0, primeiro, cores[0]),
                ('(' + str(segundo_1) +' - '+str(segundo_2) + ') - Baixo | ' + str(round(area2/10000,2)) + ' ha (' + str(area2_porc) + '%)', segundo_1, segundo_2, cores[1]),
                ('(' + str(terceiro_1) +' - '+str(terceiro_2) + ') - Médio | ' + str(round(area3/10000,2)) + ' ha (' + str(area3_porc) + '%)', terceiro_1, terceiro_2, cores[2]),
                ('(' + str(quarto_1) +' - '+str(quarto_2) + ') - Alto | ' + str(round(area4/10000,2)) + ' ha (' + str(area4_porc) + '%)', quarto_1, quarto_2, cores[3]),
                ('(> ' + str(quinto_1) + ') - Muito alto | ' + str(round(area5/10000,2)) + ' ha (' + str(area5_porc) + '%)', quinto_1, 100000000000, cores[4])
            ]

       
        map = QgsLayoutItemMap(layout)
        map.setRect(30, 30, 30, 30)
        ms = QgsMapSettings()
        ms.setLayers([layer])
        rect = QgsRectangle(ms.fullExtent())
        rect.scale(1.2)
        ms.setExtent(rect)
        map.setExtent(rect)
        map.setBackgroundColor(QColor(255, 255, 255, 0))
        map.attemptMove(QgsLayoutPoint(10, 10, QgsUnitTypes.LayoutMillimeters))
        
        #Alterar escala
        map.attemptResize(QgsLayoutSize(250, 250, QgsUnitTypes.LayoutMillimeters))
        layout.addLayoutItem(map)


        legend = QgsLayoutItemLegend(layout)
        layerTree = QgsLayerTree()
        layerTree.addLayer(layer)
        legend.model().setRootGroup(layerTree)
        layout.addLayoutItem(legend)
        legend.attemptMove(QgsLayoutPoint(180, 15, QgsUnitTypes.LayoutMillimeters))


        layout = manager.layoutByName(layoutName)
        exporter = QgsLayoutExporter(layout)
        time.sleep(3)
        fn = "qgis/"+arq + '_' + at+".png"
        exporter.exportToImage(fn, QgsLayoutExporter.ImageExportSettings())
