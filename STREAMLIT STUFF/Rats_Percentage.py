# TAKE FROM PY FILE THAT ALREADY CONTAINS FUNCTIONS AND DATA
from CUNY_DOES_CARE import find_closest_school, All_Cuny_Colleges, pd


# RATS CHECKINGSSSS
df_rats = pd.read_csv('Rat_Sightings.csv')

# COORDINATES FOR LOCATED RATS
df_rats_coords = df_rats[['Latitude', 'Longitude', 'Location', 'Borough']].copy()
# ADD CLOSEST COLLEGE COLUMN USING LAMBDA FUNCTION FOR EACH ROW
df_rats_coords['Closest_College'] = df_rats_coords.apply(
    lambda row: find_closest_school(row, All_Cuny_Colleges['School Name_Longitude_Latitude']),
    axis=1
)

# Count the number of rat sightings near each CUNY college
rat_sightings_by_college = df_rats_coords['Closest_College'].value_counts()

# TOTAL SIGHTINGS = 101,208 RATONES
total_sightings = rat_sightings_by_college.sum()

# DIVIDE ALL ROWS VALUE COUNTS BY TOTAL_SIGHTINGS 
rat_sightings_by_college_org = rat_sightings_by_college / total_sightings

# CONVERT TO DATAFRAME
rat_spoted_df = pd.DataFrame({
    'College': rat_sightings_by_college_org.index,
    'Likelihood_of_Rat_Sighting': rat_sightings_by_college_org.values
})

# OUT OF ALL 23 CUNYS HOW LIKELY ARE YOU TO SEE A RAT?
def print_rats_percentage_by_college(df):
    for index, row in df.iterrows():
        print(f"Out of all 23 CUNYs, you have a {row['Likelihood_of_Rat_Sighting'] * 100:.2f}% chance of seeing a rat at {row['College']}")
        print("-" * 60)  # Separator line for better readability

print_rats_percentage_by_college(rat_spoted_df)

''' ****** OUTPUT ******

Out of all 23 CUNYs, you have a 19.86% chance of seeing a rat at Medgar Evers College
------------------------------------------------------------
Out of all 23 CUNYs, you have a 8.37% chance of seeing a rat at Bronx Community College
------------------------------------------------------------
Out of all 23 CUNYs, you have a 8.06% chance of seeing a rat at Lehman College
------------------------------------------------------------
Out of all 23 CUNYs, you have a 6.62% chance of seeing a rat at LaGuardia Community College
------------------------------------------------------------
Out of all 23 CUNYs, you have a 6.53% chance of seeing a rat at Hostos Community College
------------------------------------------------------------
Out of all 23 CUNYs, you have a 6.16% chance of seeing a rat at The CUNY School of Public Health & Health Policy
------------------------------------------------------------
Out of all 23 CUNYs, you have a 5.91% chance of seeing a rat at York College
------------------------------------------------------------
Out of all 23 CUNYs, you have a 5.28% chance of seeing a rat at New York City College of Technology (City Tech)
------------------------------------------------------------
Out of all 23 CUNYs, you have a 5.22% chance of seeing a rat at Brooklyn College
------------------------------------------------------------
Out of all 23 CUNYs, you have a 4.83% chance of seeing a rat at College of Staten Island
------------------------------------------------------------
Out of all 23 CUNYs, you have a 3.55% chance of seeing a rat at The City College
------------------------------------------------------------
Out of all 23 CUNYs, you have a 3.48% chance of seeing a rat at Hunter College
------------------------------------------------------------
Out of all 23 CUNYs, you have a 3.02% chance of seeing a rat at Borough of Manhattan Community College
------------------------------------------------------------
Out of all 23 CUNYs, you have a 2.86% chance of seeing a rat at Baruch College
------------------------------------------------------------
Out of all 23 CUNYs, you have a 2.60% chance of seeing a rat at Queens College
------------------------------------------------------------
Out of all 23 CUNYs, you have a 2.25% chance of seeing a rat at John Jay College
------------------------------------------------------------
Out of all 23 CUNYs, you have a 1.47% chance of seeing a rat at Kingsborough Community College
------------------------------------------------------------
Out of all 23 CUNYs, you have a 1.05% chance of seeing a rat at CUNY School of Law
------------------------------------------------------------
Out of all 23 CUNYs, you have a 0.91% chance of seeing a rat at The CUNY School of Professional Studies
------------------------------------------------------------
Out of all 23 CUNYs, you have a 0.91% chance of seeing a rat at Queensborough Community College
------------------------------------------------------------
Out of all 23 CUNYs, you have a 0.64% chance of seeing a rat at The Craig Newmark Graduate School Of Journalism At CUNY
------------------------------------------------------------
Out of all 23 CUNYs, you have a 0.22% chance of seeing a rat at The Graduate School and University Center
------------------------------------------------------------
Out of all 23 CUNYs, you have a 0.20% chance of seeing a rat at Guttman Community College
------------------------------------------------------------

'''