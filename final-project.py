import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image


NYC_neighbourGroup = ['Manhattan', 'Brooklyn', 'Queens', 'Staten Island', 'Bronx']
Manhattan_neighbour = [ "Midtown", "Harlem", "East Harlem", "Murray Hill", "Hell's Kitchen", "Upper West Side", 
                   "Chinatown", "West Village", "Chelsea", "Inwood", "East Village", "Lower East Side", "Kips Bay", 
                   "SoHo", "Upper East Side", "Washington Heights", "Financial District", "Morningside Heights", 
                   "NoHo", "Flatiron District", "Roosevelt Island", "Greenwich Village", "Little Italy", "Two Bridges", 
                   "Nolita", "Gramercy", "Theater District", "Tribeca", "Battery Park City", "Civic Center", 
                   "Stuyvesant Town", "Marble Hill"
                   ] 

Brooklyn_neigh = [ 'Bushwick', 'Kensington', 'Clinton Hill', 'Bedford-Stuyvesant', 'South Slope', 
                  'Williamsburg', 'Fort Greene', 'Crown Heights', 'Park Slope', 'Windsor Terrace', 
                  'Greenpoint', 'Flatbush', 'Prospect-Lefferts Gardens', 'Prospect Heights', 
                  'Brooklyn Heights', 'Carroll Gardens', 'Gowanus', 'Flatlands', 'Cobble Hill', 
                  'Boerum Hill', 'DUMBO', 'East Flatbush', 'Gravesend', 'East New York', 'Sheepshead Bay', 
                  'Fort Hamilton', 'Bensonhurst', 'Sunset Park', 'Brighton Beach', 'Cypress Hills', 
                  'Bay Ridge', 'Columbia St', 'Vinegar Hill', 'Canarsie', 'Borough Park', 
                  'Downtown Brooklyn', 'Midwood', 'Red Hook', 'Dyker Heights', 'Sea Gate', 'Navy Yard', 
                  'Brownsville', 'Manhattan Beach', 'Bergen Beach', 'Coney Island', 'Bath Beach', 'Mill Basin'
                  ]

Queens_neigh = [ "Long Island City", "Woodside", "Flushing", "Sunnyside", "Ridgewood", "Jamaica", 
               "Middle Village", "Ditmars Steinway", "Astoria", "Queens Village", "Rockaway Beach", 
               "Forest Hills", "Elmhurst", "Jackson Heights", "St. Albans", "Rego Park", "Briarwood", 
               "Ozone Park", "East Elmhurst", "Arverne", "Cambria Heights", "Bayside", "Kew Gardens", 
               "College Point", "Glendale", "Richmond Hill", "Bellerose", "Maspeth", "Woodhaven", 
               "Kew Gardens Hills", "Bay Terrace", "Whitestone", "Bayswater", "Fresh Meadows", 
               "Springfield Gardens", "Howard Beach", "Belle Harbor", "Jamaica Estates", 
               "Far Rockaway", "South Ozone Park", "Corona", "Neponsit", "Laurelton", "Holliswood", 
               "Rosedale", "Edgemere", "Jamaica Hills", "Hollis", "Douglaston", "Little Neck", "Breezy Point"
          ]
StatenIsland_neigh = [ "St. George", "Tompkinsville", "Emerson Hill", "Shore Acres", "Arrochar", "Clifton", 
                      "Graniteville", "Stapleton", "New Springville", "Tottenville", "Mariners Harbor", 
                      "Concord", "Port Richmond", "Woodrow", "Eltingville", "Lighthouse Hill", "West Brighton", 
                      "Great Kills", "Dongan Hills", "Castleton Corners", "Randall Manor", "Todt Hill", "Silver Lake", 
                      "Grymes Hill", "New Brighton", "Midland Beach", "Richmondtown", "Howland Hook", "New Dorp Beach", 
                      "Prince's Bay", "South Beach", "Oakwood", "Huguenot", "Grant City", "Westerleigh", 
                      "Bay Terrace, Staten Island", "Fort Wadsworth", "Rosebank", "Arden Heights", "Bull's Head", 
                      "New Dorp", "Rossville", "Willowbrook"
         ]
Bronx_neigh = [ "Highbridge", "Clason Point", "Eastchester", "Kingsbridge", "Woodlawn", "University Heights", "Allerton", 
               "Concourse Village", "Concourse", "Wakefield", "Spuyten Duyvil", "Mott Haven", "Longwood", "Morris Heights", 
               "Port Morris", "Fieldston", "Mount Eden", "City Island", "Williamsbridge", "Soundview", "Co-op City", 
               "Parkchester", "North Riverdale", "Bronxdale", "Riverdale", "Norwood", "Claremont Village", "Fordham", 
               "Mount Hope", "Van Nest", "Morris Park", "Tremont", "East Morrisania", "Hunts Point", "Pelham Bay", 
               "Throgs Neck", "West Farms", "Morrisania", "Pelham Gardens", "Belmont", "Baychester", "Melrose", 
               "Schuylerville", "Castle Hill", "Olinville", "Edenwald", "Westchester Square", "Unionport"]

######################
# Page Title
######################
# 1. welcome picture
# PIL.Image
image = Image.open('welcome.png')

#https://docs.streamlit.io/library/api-reference/media/st.image
st.header('Welcome to my new App')
st.image(image, use_column_width=False)

st.write("""
# Airbnb NYC 2019 Count Web App

This App is showing Airbnb NYC 2019 housing data!
***
""") 

# 2. load data
uploaded_file = 'AB_NYC_2019.csv' 

st.subheader('Display Overall View')
# df = pd.DataFrame.from_dict(X, orient='index')
df = pd.read_csv(uploaded_file)
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

st.write("---") # line separater


# (please choose)
option_group = st.selectbox(
    'please select neighbor group:',
    NYC_neighbourGroup)

# 显示选中的项
st.header('you select this neighbor group:', option_group)
# -------
if option_group == 'Manhattan':
    option_anything=Manhattan_neighbour
elif option_group =='Brooklyn':
    option_anything=Brooklyn_neigh
elif option_group =='Queens':
    option_anything=Queens_neigh
elif option_group =='Staten Island':
    option_anything=StatenIsland_neigh
elif option_group =='Bronx':
    option_anything=Bronx_neigh


option_neighbor = st.selectbox(
    'please select neighbor:',
    option_anything)

# 显示选中的项
st.write('you select ', option_neighbor, 'neighborhoods in', option_group)

st.write("---") # line separater

Min_pric=0
Max_price=100000
# price
df = pd.read_csv(uploaded_file)

Min_price = st.number_input('Insert a Minimum price:')
Max_price = st.number_input('Insert a maximum price:')
st.write('The current minimum number is ', Min_price)
st.write('The current maximum number is ', Max_price)
list_2d = df.values.tolist()


New_list=[]

for line in list_2d:
    if line[5]== option_neighbor and int(line[9])>= Min_price and int(line[9]) <=Max_price:
            New_list.append(line)
number=len(New_list)
st.header(f'Total {number} housing rental are found in {option_neighbor} of {option_group} with price between ${Min_price} and {Max_price}')

st.write("---") # line separater

# 遍历

# addresses = ["地址1", "地址2", "地址3", "...", "地址100"]

# 使用 st.radio 来显示地址列表
selected_address_index = st.radio("please select an address：", New_list)

# 显示选中的地址


if selected_address_index != None:
    st.write("information of the address：")
    st.write('Name:', selected_address_index[1])
    st.write('Host name:', selected_address_index[3])
    st.write('neighbor group:', selected_address_index[4])
    st.write('neighborhood:', selected_address_index[5])
    st.write('room type:', selected_address_index[8])
    st.write('pricetips:$' , selected_address_index[9])
    # st.write("你选择的地址是：" , selected_address_index)
    address_lat=selected_address_index[6]
    address_lon=selected_address_index[7]
    data = {
        'lat': [address_lat - 0.1,    address_lat,    address_lat + 0.1],  # 纬度列表
        'lon': [address_lon - 0.1,    address_lon,    address_lon + 0.1]  # 经度列表
    }
    df = pd.DataFrame(data)   # 将数据转换为 DataFrame
    st.map(df)                 # 在 Streamlit 应用中显示地图

