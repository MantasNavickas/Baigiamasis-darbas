import sqlite3
import pandas as pd
import os




class Function():
    def __init__(self, member_name, member_surname, member_address, member_email, member_phone, send_email, send_sms):
        self.db_name = 'SB_Ezerelis.db'
        self.db_table = 'sb_nariai'
        self.member_name = member_name
        self.member_surname = member_surname
        self.member_address = member_address
        self.member_email = member_email
        self.member_phone = member_phone
        self.send_email = send_email
        self.send_sms = send_sms
    
    # BENDRIJOS NARIO DUOMENŲ PRIDĖJIMAS Į SISTEMĄ
    def add_member_data(self):
        with sqlite3.connect(self.db_name) as conn: 
            c = conn.cursor()
            c.execute(f"CREATE TABLE IF NOT EXISTS {self.db_table} (Vardas text, Pavardė text, Adresas text, El.paštas text, Tel.nr text, El.laiškai integer, SMS integer)") #Sukuriam naują lentelę, jei ji neegzistuoja
            try:
                c.execute(
                    f"INSERT INTO sb_nariai VALUES ('{self.member_name}', '{self.member_surname}', '{self.member_address}', '{self.member_email}', '{self.member_phone}', '{self.send_email}', '{self.send_sms}')"
                    ) #Pridedam naują narį į duomenų bazę
                return 'Duomenys sekmingai pridėti į duomenų bazę' 
           
            except Exception as e:
                return f"Klaida: {e}"
              

   
    # BENDRIJOS NARIŲ SĄRAŠO RODYMAS EXCEL FAILE:
    def show_member_list(self, output):
        output = 'nariu_sarasas.xlsx'
        try:
            with sqlite3.connect(self.db_name) as conn:
                # Read data into a Pandas DataFrame
                df = pd.read_sql_query(f"SELECT * FROM {self.db_table}", conn)
            
            # Export to Excel
            df.to_excel(output, index=False, engine='openpyxl')

            # Open the file after exporting
            if os.name == 'nt':  # Windows
                os.startfile(output)
            elif os.uname().sysname == "Darwin":  # macOS
                os.system(f'open "{output_file}"')
            else:  # Linux
                os.system(f'xdg-open "{output_file}"')

            print(f"Duomenys sėkmingai eksportuoti į {output} failą")

        except Exception as e:
            print(f"Klaida: {e}")

    
    # BENDRIJOS NARIŲ DUOMENŲ MODIFIKAVIMAS
    def modify_member(self):
        try:
            with sqlite3.connect(self.db_name) as conn: 
                c = conn.cursor()
                c.execute(
                    f"UPDATE {self.db_table} SET Vardas = '{self.member_name}', Pavardė = '{self.member_surname}', El.paštas = '{self.member_email}', Tel.nr = '{self.member_phone}', El.laiškai = {self.send_email}, SMS = {self.send_sms} WHERE Adresas= '{self.member_address}'"
                    )
                print('Duomenys sėkmingai atnaujinti')

        except Exception as e:
            print(f"Klaida: {e}")
    

    # BENDRIJOS NARIŲ PAIEŠKA
    def search_by_name(self):
        try:
            with sqlite3.connect(self.db_name) as conn: 
                    c = conn.cursor()
                    members_found = c.execute(f"SELECT * From {self.db_name} WHERE Vardas = '{self.member_name}' or Pavardė = '{self.member_surname}' or Adresas = '{self.member_address}' or El.paštas = '{self.member_email}' or Tel.nr = '{self.member_phone}'"
                                            ).fetchall()

                    for member in members_found:
                        print(member)
        
        except Exception as e:
            print(f"Klaida: {e}")
    



