import gspread
import mysql.connector
from oauth2client.service_account import ServiceAccountCredentials

# Define scope for Google Sheets API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Load Google Sheets API credentials
creds = ServiceAccountCredentials.from_json_keyfile_name("z", scope)
client = gspread.authorize(creds)

# Open Google Sheet by URL
sheet_url = ""
spreadsheet = client.open_by_url(sheet_url)

# Select the worksheet
worksheet = spreadsheet.get_worksheet(0)  # First sheet

# Connect to MySQL Database
DB_CONFIG = {
     "host":"",       
     "user":"",   
     "password":"",  
     "database":""
     }

try:
      # ✅ Step 1: Establish DB Connection    
    conn = mysql.connector.connect(
        host=DB_CONFIG["host"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        database=DB_CONFIG["database"]
    )
    cursor = conn.cursor()    
    # First Query*******total() subscribers***************************************
    query = """
        
    """
    cursor.execute(query)
    result = cursor.fetchone()
    text_to_write = str(result[0]) if result and result[0] is not None else "0"
    cell_address = "H19"
    worksheet.update(cell_address, [[text_to_write]])
    print(f"Text '{text_to_write}' written to {cell_address} successfully!")
    # SECOND QUERY********* subscribers*************************************      
    query = """
        
    """
    cursor.execute(query)   
    result = cursor.fetchone()
    text_to_write = str(result[0]) if result and result[0] is not None else "0"    
    cell_address = "H20"
    worksheet.update(cell_address, [[text_to_write]])
    print(f"Text '{text_to_write}' written to {cell_address} successfully!")

    # THIRD QUERY*** subscribers******************************************** 
    query = """
        
    """
    cursor.execute(query)    
    result = cursor.fetchone()
    text_to_write = str(result[0]) if result and result[0] is not None else "0"  
    cell_address = "H24"
    worksheet.update(cell_address, [[text_to_write]])
    print(f"Text '{text_to_write}' written to {cell_address} successfully!")
    # Four QUERY--  Revenue***********************************************   
    query = """    
    
    """
    cursor.execute(query)    
    result = cursor.fetchone()
    text_to_write = str(result[0]) if result and result[0] is not None else "0"
    cell_address = "H21"
    worksheet.update(cell_address, [[text_to_write]])
    print(f"Text '{text_to_write}' written to {cell_address} successfully!")
    # Five QUERY--  Revenue*********************************************** 
    query = """
    
    """
    cursor.execute(query)    
    result = cursor.fetchone()
    text_to_write = str(result[0]) if result and result[0] is not None else "0"
    cell_address = "H25"
    worksheet.update(cell_address, [[text_to_write]])
    print(f"Text '{text_to_write}' written to {cell_address} successfully!")
    # Six QUERY-- ***********************************************    
    query = """
    
    """
    cursor.execute(query)
    result = cursor.fetchone()
    text_to_write = str(result[0]) if result and result[0] is not None else "0"
    cell_address = "H26"
    worksheet.update(cell_address, [[text_to_write]])
    print(f"Text '{text_to_write}' written to {cell_address} successfully!")

except mysql.connector.Error as e:
    print("❌ Database Error:", e)

finally:
    # ✅ Step 4: Close Connection
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
    print("✅ Database connection closed.")


