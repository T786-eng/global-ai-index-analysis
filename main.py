import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """Loads the AI Index dataset."""
    try:
        df = pd.read_csv(file_path)
        print(f"Successfully loaded {file_path}")
        return df
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return None

def basic_analysis(df):
    """Prints basic statistics and top performing countries."""
    print("\n--- Basic Statistics ---")
    print(df.describe())

    print("\n--- Top 10 Countries by Total Score ---")
    top_10 = df.nlargest(10, 'Total score')[['Country', 'Total score', 'Region']]
    print(top_10)

def visualize_data(df):
    """Generates and saves visualizations."""
    sns.set_theme(style="whitegrid")

    # 1. Average Total Score by Region
    plt.figure(figsize=(10, 6))
    region_avg = df.groupby('Region')['Total score'].mean().sort_values(ascending=False)
    region_avg.plot(kind='bar', color='skyblue')
    plt.title('Average AI Total Score by Region')
    plt.ylabel('Average Total Score')
    plt.xlabel('Region')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('avg_score_by_region.png')
    print("Saved: avg_score_by_region.png")

    # 2. Talent vs. Infrastructure Scatter Plot
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Talent', y='Infrastructure', hue='Region', size='Total score', sizes=(20, 200))
    plt.title('AI Talent vs. Infrastructure')
    plt.tight_layout()
    plt.savefig('talent_vs_infrastructure.png')
    print("Saved: talent_vs_infrastructure.png")

def main():
    file_name = 'AI_index_db.csv'
    df = load_data(file_name)
    
    if df is not None:
        basic_analysis(df)
        visualize_data(df)
        print("\nAnalysis complete.")

if __name__ == "__main__":
    main()