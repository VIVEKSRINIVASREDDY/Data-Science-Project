import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = "C:/Users/Vivek/Downloads/Electric_Vehicle_Population_Data.csv"
df = pd.read_csv(file_path)

# Objective 1 
# Top 10 Cities
city_counts = df['City'].value_counts().head(10).reset_index()
city_counts.columns = ['City', 'EV Count']

plt.figure(figsize=(10,6))
sns.barplot(data=city_counts, x='EV Count', y='City', hue='City', palette='viridis', legend=False)
plt.title("Top 10 Cities by Electric Vehicle Count")
plt.xlabel("Number of Electric Vehicles")
plt.ylabel("City")
plt.tight_layout()
plt.show()

# Top 10 ZIP Codes
zip_counts = df['ZIP Code'].value_counts().head(10).reset_index()
zip_counts.columns = ['ZIP Code', 'EV Count']

plt.figure(figsize=(10,6))
sns.barplot(data=zip_counts, x='EV Count', y='ZIP Code', hue='ZIP Code', palette='magma', legend=False)
plt.title("Top 10 ZIP Codes by Electric Vehicle Count")
plt.xlabel("Number of Electric Vehicles")
plt.ylabel("ZIP Code")
plt.tight_layout()
plt.show()

# Objective 2
# Count number of vehicles per make
make_counts = df['Make'].value_counts().head(10)  # Top 10 makes

# Create pie chart
plt.figure(figsize=(8, 8))
colors = sns.color_palette('pastel')[0:10]
plt.pie(make_counts, labels=make_counts.index, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Top 10 Most Popular Electric Vehicle Makes')
plt.axis('equal')
plt.tight_layout()
plt.show()


# Objective 3
# EVs over Model Year
year_counts = df['Model Year'].value_counts().sort_index().reset_index()
year_counts.columns = ['Model Year', 'Count']

plt.figure(figsize=(12,6))
sns.lineplot(data=year_counts, x='Model Year', y='Count', marker='o')
plt.title("Electric Vehicle Growth Over Model Years")
plt.xlabel("Model Year")
plt.ylabel("Number of Vehicles")
plt.grid(True)
plt.tight_layout()
plt.show()

# Objective 4
# Crosstab City vs. EV Type (Top 10 Cities only)
top_cities = df['City'].value_counts().head(10).index
city_evtype = pd.crosstab(df['City'], df['Electric Vehicle Type']).loc[top_cities]

# Convert crosstab to long format
city_evtype_reset = city_evtype.reset_index().melt(id_vars='City', var_name='EV Type', value_name='Count')

plt.figure(figsize=(12,6))
sns.barplot(data=city_evtype_reset, x='Count', y='City', hue='EV Type', palette='Accent')
plt.title("Electric Vehicle Types by Top 10 Cities")
plt.xlabel("Number of Vehicles")
plt.ylabel("City")
plt.tight_layout()
plt.show()

# Objective 5
# Top 10 Cities
city_reg = df['City'].value_counts().head(10).reset_index()
city_reg.columns = ['City', 'Count']

plt.figure(figsize=(10,5))
sns.barplot(data=city_reg, x='Count', y='City', hue='City', palette='pastel', legend=False)
plt.title("Top 10 Cities by EV Registrations")
plt.xlabel("Number of Vehicles")
plt.ylabel("City")
plt.tight_layout()
plt.show()

# Top 10 Counties
county_reg = df['County'].value_counts().head(10).reset_index()
county_reg.columns = ['County', 'Count']

plt.figure(figsize=(10,5))
sns.barplot(data=county_reg, x='Count', y='County', hue='County', palette='Blues', legend=False)
plt.title("Top 10 Counties by EV Registrations")
plt.xlabel("Number of Vehicles")
plt.ylabel("County")
plt.tight_layout()
plt.show()

# Objective 6
# Drop rows with missing values in relevant columns
df = df.dropna(subset=['Model Year', 'Clean Alternative Fuel Vehicle (CAFV) Eligibility'])

# Convert Model Year to numeric (if it's not already)
df['Model Year'] = pd.to_numeric(df['Model Year'], errors='coerce')

plt.figure(figsize=(10,6))
sns.boxplot(data=df, x='Clean Alternative Fuel Vehicle (CAFV) Eligibility', y='Model Year', palette='Set2')
plt.title("Influence of Policy Eligibility on Electric Vehicle Model Year")
plt.xlabel("CAFV Eligibility Status")
plt.ylabel("Model Year of EV")
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()

# Objective 7
top_cities = df['City'].value_counts().head(10).index
filtered_df = df[df['City'].isin(top_cities)]

# Pivot for stacked bar chart
pivot_data = pd.crosstab(filtered_df['City'], filtered_df['Electric Vehicle Type'])

pivot_data.plot(kind='bar', stacked=True, figsize=(12, 6), colormap='Spectral')
plt.title("EV Type Distribution in Top 10 Cities")
plt.xlabel("City")
plt.ylabel("Number of Vehicles")
plt.legend(title="EV Type")
plt.tight_layout()
plt.show()
