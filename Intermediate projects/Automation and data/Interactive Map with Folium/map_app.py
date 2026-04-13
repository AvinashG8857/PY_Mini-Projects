import folium
import pandas as pd

def create_map():
    data={
        "name":["Eiffel Tower","Statue of Liberty","Colosseum"],
        'lat': [48.8584, 40.6892, 41.8902],
        'lon': [2.2945, -74.0445, 12.4922],
        "info":["paris","France","New York,USA","Rome","Italy"]
    }
    df= pd.DataFrame(data)

    my_map = folium.Map(location=[20,0],zoom_start=2,tiles="OpenStreetMap")
    for index,row in df.itterrows():
        popup_text= f"<b>{row['name']}</b><br>{row['ainfo']}"

        folium.Marker(
            location=[row["lat"],row["lon"]],
            popup=folium.Popup(popup_text,max_width=200),
            tooltip="Click for Info",
            icon=folium.icon(color="red",icon="info-sign")).add_to(my_map)
        
    my_map.save("world_map.html")
    print("Map has Created! Open 'world_map.html' in your browser to see")


    if __name__ == "__main__":
        create_map()