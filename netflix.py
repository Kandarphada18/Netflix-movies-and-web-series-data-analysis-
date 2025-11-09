import pandas as pd
import numpy as np
import time
# Load data from CSV
df=pd.read_csv("D:\\CODES24\\project2\\netflix_titles.csv")
print("\n===== Loaded Dataset =====")
print(df)
#hnadle missing values
print("\nMisssing Valus Summary::")
print(df.isnull().sum())
df['director'].fillna('Unknown',inplace=True)
df['cast'].fillna('Unknown',inplace=True)
#filling missing values with mode for categorical columns
categorical_cols=['director','cast','country','date_added','rating','duration','listed_in','description']
for col in categorical_cols:
  df[col].fillna(df[col].mode()[0],inplace=True)
print("\n===== Dataset after handling missing values =====")
print(df)   
#convert dataframe columns to numpy arrays
title=df["title"].to_numpy()
release_year=df["release_year"].to_numpy()
print("\n=====Numpy-Based-Analysis=====")
#descriptive statistics using numpy
print(f"Total title:{np.size(title)}")
print(f"release_year min and max:{np.min(release_year)}-{np.max(release_year)}")
print(f"Average release_year:{np.mean(release_year):.2f}")
print(f"release_year Std Dev:{np.std(release_year):.2f}")
import matplotlib.pyplot as plt
#visulation using matplotlib
def plot_release_year_histogram(release_year):
    plt.hist(release_year,bins=30,color='skyblue',edgecolor='black')
    plt.title('Distribution of Release Year')
    plt.xlabel('Release Year')
    plt.ylabel('Number of Titles')
    plt.show()
def show_Bar_chart(Type,df):
    Type_counts=df[Type].value_counts()
    plt.bar(Type_counts.index,Type_counts.values,color='Lightgreen',edgecolor='lightyellow')
    plt.title("Movies vs TV Shows")
    plt.xlabel("Type")
    plt.ylabel("Count")
    plt.show()
def show_county_bar():
   top_countries=df["country"].value_counts().head(10)
   plt.bar(top_countries.index,top_countries.values,color='orange',edgecolor='red')
   plt.title("Top 10 Countries by Number of Titles")    
   plt.xlabel("Country")
   plt.ylabel("Count")
   plt.gca().invert_xaxis()
   plt.tight_layout()
   plt.show()
def show_pie_chart():
    rating_counts=df["rating"].value_counts()
    plt.pie(rating_counts.values,labels=rating_counts.index,autopct='%1.1f%%',startangle=140,labeldistance=1.1,pctdistance=0.8)
    plt.title("Distribution of Ratings",fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()

def animated_exit():
    print("\nThanks for using Netflix Data Visualizer ❤️")
    print("Generating an animated goodbye...")

    x = np.linspace(0, 4*np.pi, 100)
    for i in range(1, 8):
        y = np.sin(x + i)
        plt.plot(x, y, color='orange')
        plt.title("Goodbye! •See you again • :)")
        plt.pause(0.6)
        plt.clf()

    print("keep Coding , keep Learning!")
    plt.close()

while True:
   print("\nVisulation Options:")
   print("1. Release Year Histogram")
   print("2. Movies vs TV Shows Bar Chart")
   print("3. Top 10 Countries Bar Chart")
   print("4.Rating Distribution Pie Chart")
   print("5. Exiting with Animated Goodbye")

   choice =input("Enter your choice(1-5):")
   if choice=='1':
      plot_release_year_histogram(release_year)
   elif choice=='2':
      show_Bar_chart('type',df)
   elif choice=='3':
        show_county_bar()
   elif choice=='4':
        show_pie_chart()
   elif choice=='5':
        animated_exit()
        break
   else:
       print("Invalid choice.Please try again.")
   
        