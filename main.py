from db_connection import connect_to_db
from data_loader import load_data
from data_cleaner import clean_data
from visualizer import analyze_and_visualize


def main():
    """Main orchestration function"""
    try:
        # 1. Connect to database
        print("\n===== Connecting to Database =====")
        conn = connect_to_db()

        # 2. Load data
        print("\n===== Loading Data =====")
        data_dict = load_data(conn)

        # 3. Clean data
        print("\n===== Cleaning Data =====")
        cleaned_data = clean_data(data_dict)

        # 4. Analyze and visualize
        print("\n===== Analyzing and Visualizing Data =====")
        analyze_and_visualize(cleaned_data)

        print("\n===== Process Completed =====")

    except Exception as e:
        print(f"\nError in main process: {str(e)}")

    finally:
        # Close connection if it exists
        if 'conn' in locals() and conn.is_connected():
            conn.close()
            print("Database connection closed")


if __name__ == "__main__":
    main()
