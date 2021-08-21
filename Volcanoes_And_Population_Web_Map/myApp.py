import folium
import pandas

def createMapObject(location=[0, 0]):
    map = folium.Map(location=location, tiles="Stamen Terrain", zoom_start=6)
    return map

def getDataFrame():
    dataFR = pandas.read_csv("resource/Volcanoes.txt")
    return dataFR

def addVolcanoesPopulation(map, dataList):

    def getColor(height):
        if height <= 2000:
            return 'green'
        elif height <= 3000:
            return 'orange'
        else:
            return 'red'

    #Add volcanoes  layer
    groupV = folium.FeatureGroup(name="Volcanoes")
    for index in range(len(dataList)):
        item = dataList.loc[index]
        popupStr = item['NAME'] + '\n' + str(item['ELEV'])
        lat = item['LAT']
        lon = item['LON']
        groupV.add_child(folium.Marker(location=[lat, lon], popup=popupStr, icon=folium.Icon(color=getColor(item['ELEV']))))
    
    # Add population layer
    groupP = folium.FeatureGroup(name="Population")
    borderData = open('resource/world.json', 'r', encoding='utf-8-sig').read()
    groupP.add_child(folium.GeoJson(data=borderData, 
    style_function=lambda x: {"fillColor":'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

    map.add_child(groupV)
    map.add_child(groupP)

    #Add layer control
    map.add_child(folium.LayerControl())

    return map

if __name__ == "__main__":
    myMap = createMapObject([38, -99])
    dataList = getDataFrame()
    myMap = addVolcanoesPopulation(myMap, dataList)
    myMap.save("VolcanoesMap.html")
