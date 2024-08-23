# TAKE FROM PY FILE THAT ALREADY CONTAINS FUNCTIONS AND DATA
from CUNY_DOES_CARE import haversine, All_Cuny_Colleges, pd


# RATS CHECKINGSSSS
df_rats = pd.read_csv('Rat_Sightings.csv')

# COORDINATES FOR LOCATED RATS
df_rats_coords = df_rats[['Latitude', 'Longitude', 'Location', 'Borough']].copy()

# ALLOW USER INPUT (FLOAT VALUES)
radius_km = float(input('Input Radius in Kilometers (1KM = 1093.61 Yards): '))

# FUNCTION TO FIND RATS WITHIN A CERTAIN RADIUS OF COLLEGE
def rats_within_radius(df_rats_coords, school_map, radius_km):
    # STORE COUNTS OF RATS IN DICTIONARY
    rats_near_colleges = {}

    # CALUCLATE NUMBER OF RATS WITHIN RADIUS OF SPECIFIC COLLEGE
    for school, (school_lat, school_lon) in school_map.items():
        
        # CALCULATE DISTANCE BETWEEN COLLEGE AND RAT SIGHTING
        df_rats_coords['Distance_to_' + school] = df_rats_coords.apply(
            lambda row: haversine(row['Latitude'], row['Longitude'], school_lat, school_lon),
            axis=1)

        # MAKE SURE RATS ARE WITHIN RADIUS
        rats_nearby = df_rats_coords[df_rats_coords['Distance_to_' + school] <= radius_km]
        
        # COUNT NUMBER OF RATS FOR EACH COLLEGE
        rats_near_colleges[school] = rats_nearby.shape[0]

    return rats_near_colleges

# RATS WITH 1KM = 1093.61 Yards
rats_near_colleges = rats_within_radius(df_rats_coords, All_Cuny_Colleges['School Name_Longitude_Latitude'], radius_km)

# CONVERT INTO DATA FRAME (.items() spits out tuples which will become their new respected column values)
rats_near_colleges_df = pd.DataFrame(list(rats_near_colleges.items()), columns=['College', 'Rats_Within_Radius'])
print(rats_near_colleges_df)

# GET DATA FORMAT BETTER
def print_rats_near_within_radius(df, radius_km):
    for index, row in rats_near_colleges_df.iterrows():
        print(f"{row['College']} has {row['Rats_Within_Radius']} rat within a {radius_km} KM radius ")
        print("-" * 50)  # Separator line for better readability

print_rats_near_within_radius(rats_near_colleges_df, radius_km)

''' ******* OUTPUT ****** 

Baruch College has 967 rat within a 1.0 KM radius 
--------------------------------------------------
Borough of Manhattan Community College has 778 rat within a 1.0 KM radius 
--------------------------------------------------
The City College has 2301 rat within a 1.0 KM radius 
--------------------------------------------------
The Graduate School and University Center has 810 rat within a 1.0 KM radius 
--------------------------------------------------
The Craig Newmark Graduate School Of Journalism At CUNY has 1054 rat within a 1.0 KM radius 
--------------------------------------------------
The CUNY School of Professional Studies has 974 rat within a 1.0 KM radius 
--------------------------------------------------
The CUNY School of Public Health & Health Policy has 2589 rat within a 1.0 KM radius 
--------------------------------------------------
Guttman Community College has 582 rat within a 1.0 KM radius 
--------------------------------------------------
Hunter College has 784 rat within a 1.0 KM radius 
--------------------------------------------------
John Jay College has 820 rat within a 1.0 KM radius 
--------------------------------------------------
Bronx Community College has 1330 rat within a 1.0 KM radius 
--------------------------------------------------
Hostos Community College has 880 rat within a 1.0 KM radius 
--------------------------------------------------
Lehman College has 1370 rat within a 1.0 KM radius 
--------------------------------------------------
Brooklyn College has 307 rat within a 1.0 KM radius 
--------------------------------------------------
Kingsborough Community College has 40 rat within a 1.0 KM radius 
--------------------------------------------------
Medgar Evers College has 1491 rat within a 1.0 KM radius 
--------------------------------------------------
New York City College of Technology (City Tech) has 652 rat within a 1.0 KM radius 
--------------------------------------------------
College of Staten Island has 35 rat within a 1.0 KM radius 
--------------------------------------------------
CUNY School of Law has 289 rat within a 1.0 KM radius 
--------------------------------------------------
LaGuardia Community College has 251 rat within a 1.0 KM radius 
--------------------------------------------------
Queens College has 50 rat within a 1.0 KM radius 
--------------------------------------------------
Queensborough Community College has 69 rat within a 1.0 KM radius 
--------------------------------------------------
York College has 521 rat within a 1.0 KM radius 
--------------------------------------------------

'''