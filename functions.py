import sqlite3
import pandas as pd
import os
import datetime


class Function:
    def __init__(
        self,
        member_name,
        member_surname,
        member_address,
        member_email,
        member_phone,
        send_email,
        send_sms,
    ):
        self.db_name = "./SB_Ezerelis.db"
        self.db_table = "sb_nariai"
        self.db_tax_table = "nario_mokestis"
        self.tax_size = 3
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
            c.execute(
                f"CREATE TABLE IF NOT EXISTS '{self.db_table}' (Vardas text, Pavardė text, Adresas text, El_paštas text, Tel_nr text, El_laiškai integer, SMS integer)"
            )  # Sukuriam naują lentelę, jei ji neegzistuoja
            try:
                c.execute(
                    f"INSERT INTO {self.db_table} VALUES ('{self.member_name}', '{self.member_surname}', '{self.member_address}', '{self.member_email}', '{self.member_phone}', '{int(self.send_email)}', '{int(self.send_sms)}')"
                )  # Pridedam naują narį į duomenų bazę
                return "Duomenys sekmingai pridėti į duomenų bazę"

            except Exception as e:
                return f"Klaida: {e}"

    # BENDRIJOS NARIŲ SĄRAŠO RODYMAS EXCEL FAILE:
    def show_member_list(self, output):
        try:
            with sqlite3.connect(self.db_name) as conn:
                # Read data into a Pandas DataFrame
                df = pd.read_sql_query(
                    f"SELECT Vardas, Pavardė, Adresas, El_paštas, Tel_nr FROM {self.db_table}",
                    conn,
                )

            df = df.sort_values(by="Adresas", ascending=True)

            # Export to Excel
            df.to_excel(output, index=False, engine="openpyxl")

            # Open the file after exporting
            if os.name == "nt":  # Windows
                os.startfile(output)
            elif os.uname().sysname == "Darwin":  # macOS
                os.system(f'open "{output_file}"')
            else:  # Linux
                os.system(f'xdg-open "{output_file}"')

            return f"Duomenys sėkmingai eksportuoti į {output} failą"

        except Exception as e:
            print
            return f"Klaida: {e}"

    # BENDRIJOS NARIŲ DUOMENŲ MODIFIKAVIMAS
    def modify_member(self):
        try:
            with sqlite3.connect(self.db_name) as conn:
                c = conn.cursor()
                c.execute(
                    f"UPDATE {self.db_table} SET Vardas = '{self.member_name}', Pavardė = '{self.member_surname}', El_paštas = '{self.member_email}', Tel_nr = '{self.member_phone}', El_laiškai = {int(self.send_email)}, SMS = {int(self.send_sms)} WHERE Adresas= '{self.member_address}'"
                )
                return "Duomenys sėkmingai atnaujinti"

        except Exception as e:
            return f"Klaida: {e}"

    # BENDRIJOS NARIŲ PAIEŠKA
    def search_member(self):
        try:
            with sqlite3.connect(self.db_name) as conn:
                c = conn.cursor()

                # Prepare query dynamically based on filled fields
                conditions = []
                values = []

                if self.member_name:
                    conditions.append("Vardas = ?")
                    values.append(self.member_name)
                if self.member_surname:
                    conditions.append("Pavardė = ?")
                    values.append(self.member_surname)
                if self.member_address:
                    conditions.append("Adresas = ?")  # Removed OR Adresas IS NULL
                    values.append(self.member_address)
                if self.member_email:
                    conditions.append("El_paštas = ?")
                    values.append(self.member_email)
                if self.member_phone:
                    conditions.append("Tel_nr = ?")
                    values.append(self.member_phone)

                # If no conditions provided, return nothing instead of first row
                if not conditions:
                    return "Įveskite bent vieną paieškos kriterijų!"

                # Construct the query
                query = (
                    f"SELECT Vardas, Pavardė, Adresas, El_paštas, Tel_nr FROM {self.db_table} WHERE "
                    + " AND ".join(conditions)
                )

                members_found = c.execute(query, values).fetchall()

                return members_found if members_found else ["Narių nerasta!"]

        except Exception as e:
            return f"Klaida: {e}"

    # ATNAUJINTI MOKESČIO MOKĖJIMO SĄRAŠĄ
    def add_member_tax_info(self):
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            c.execute(
                f"""
                CREATE TABLE IF NOT EXISTS '{self.db_tax_table}' (
                    Vardas TEXT, 
                    Pavardė TEXT, 
                    Adresas TEXT, 
                    Mokestiniai_metai INTEGER, 
                    Mokėjimo_data INTEGER, 
                    Įmokos_suma INTEGER, 
                    Skola_Permoka INTEGER, 
                    Mokėjimo_būdas TEXT,
                    PRIMARY KEY (Adresas, Mokestiniai_metai)  
                )
            """
            )

            try:
                now = datetime.datetime.now()
                year_now = now.year

                results = c.execute(
                    f"SELECT Vardas, Pavardė, Adresas FROM {self.db_table}"
                ).fetchall()

                for result in results:
                    # Gauti praeitų metų duomenis
                    debt_overpayment = c.execute(
                        f"""
                        SELECT Adresas, Įmokos_suma FROM {self.db_tax_table} 
                        WHERE Mokestiniai_metai = ?
                    """,
                        (year_now - 1,),
                    ).fetchall()

                    total_debt = 0  # Default value

                    for d_o in debt_overpayment:
                        total_debt = d_o[1] - self.tax_size
                        c.execute(
                            f"""
                            UPDATE {self.db_tax_table} 
                            SET Skola_Permoka = Skola_Permoka + ? 
                            WHERE Adresas = ?
                        """,
                            (total_debt, d_o[0]),
                        )

                    # Įtraukti einamųjų metų duomenis, jei tokių nėra
                    c.execute(
                        f"""
                        INSERT INTO {self.db_tax_table} 
                        (Vardas, Pavardė, Adresas, Mokestiniai_metai, Mokėjimo_data, Įmokos_suma, Skola_Permoka, Mokėjimo_būdas)
                        SELECT ?, ?, ?, ?, NULL, ?, ?, NULL
                        WHERE NOT EXISTS (
                            SELECT 1 FROM {self.db_tax_table} 
                            WHERE Adresas = ? AND Mokestiniai_metai = ?
                        )
                    """,
                        (
                            result[0],
                            result[1],
                            result[2],
                            year_now,
                            0,
                            total_debt,
                            result[2],
                            year_now,
                        ),
                    )

                conn.commit()
                return "Duomenys sėkmingai atnaujinti"

            except Exception as e:
                return f"Klaida: {e}"

    # PRIDĖTI NAUJĄ MOKĖJIMĄ
    def add_tax_payment_info(self, payed_total, method):
        try:
            with sqlite3.connect(self.db_name) as conn:
                c = conn.cursor()
                c.execute(
                    f"""
                    UPDATE {self.db_tax_table}
                    SET Įmokos_suma = Įmokos_suma + ?, Mokėjimo_būdas = ?
                    WHERE Adresas = ?
                """,
                    (payed_total, method, self.member_address),
                )
                return "Mokėjimo duomenys sėkmingai išsaugoti"

        except Exception as e:
            return f"Klaida: {e}"

    # MOKESČIO MOKĖJIMŲ INFO EXCEL FAILE
    def show_tax_list(self, output):
        try:
            with sqlite3.connect(self.db_name) as conn:
                # Read data into a Pandas DataFrame
                df = pd.read_sql_query(f"SELECT * FROM {self.db_tax_table}", conn)

            df = df.sort_values(by="Adresas", ascending=True)

            # Export to Excel
            df.to_excel(output, index=False, engine="openpyxl")

            # Open the file after exporting
            if os.name == "nt":  # Windows
                os.startfile(output)
            elif os.uname().sysname == "Darwin":  # macOS
                os.system(f'open "{output_file}"')
            else:  # Linux
                os.system(f'xdg-open "{output_file}"')

            return f"Duomenys sėkmingai eksportuoti į {output} failą"

        except Exception as e:
            print
            return f"Klaida: {e}"
