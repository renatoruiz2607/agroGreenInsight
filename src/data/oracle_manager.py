# data/oracle_manager.py

import os
import oracledb

def get_oracle_connection():
    """
    Creates and returns an Oracle database connection using environment variables.
    """
    user = os.getenv("ORACLE_USER")
    password = os.getenv("ORACLE_PASSWORD")
    dsn = os.getenv("ORACLE_DSN")

    if not user or not password or not dsn:
        raise ValueError(
            "Oracle environment variables are not properly configured. "
            "Please set ORACLE_USER, ORACLE_PASSWORD and ORACLE_DSN."
        )

    return oracledb.connect(
        user=user,
        password=password,
        dsn=dsn
    )

def test_oracle_connection():
    """
    Tests the Oracle connection.
    Returns True if the connection is successful.
    """
    connection = None

    try:
        connection = get_oracle_connection()
        return True, "Conexão com Oracle realizada com sucesso."

    except Exception as error:
        return False, f"Erro ao conectar no Oracle: {error}"

    finally:
        if connection:
            connection.close()

def create_fields_table():
    """
    Creates the fields table if it does not exist.
    """
    connection = None

    try:
        connection = get_oracle_connection()

        with connection.cursor() as cursor:
            cursor.execute("""
                BEGIN
                    EXECUTE IMMEDIATE '
                        CREATE TABLE fields (
                            field_id NUMBER PRIMARY KEY,
                            name VARCHAR2(100) NOT NULL,
                            area NUMBER(10,2) NOT NULL,
                            crop_type VARCHAR2(100) NOT NULL
                        )
                    ';
                EXCEPTION
                    WHEN OTHERS THEN
                        IF SQLCODE != -955 THEN
                            RAISE;
                        END IF;
                END;
            """)

        connection.commit()
        return True, "Tabela FIELDS criada com sucesso ou já existente."

    except Exception as error:
        return False, f"Erro ao criar tabela FIELDS: {error}"

    finally:
        if connection:
            connection.close()

def create_fertilizer_applications_table():
    """
    Creates the fertilizer_applications table if it does not exist.
    """
    connection = None

    try:
        connection = get_oracle_connection()

        with connection.cursor() as cursor:
            cursor.execute("""
                BEGIN
                    EXECUTE IMMEDIATE '
                        CREATE TABLE fertilizer_applications (
                            application_id NUMBER PRIMARY KEY,
                            field_id NUMBER NOT NULL,
                            fertilizer_type VARCHAR2(100) NOT NULL,
                            quantity NUMBER(10,2) NOT NULL,
                            application_date VARCHAR2(20) NOT NULL,
                            CONSTRAINT fk_fertilizer_field
                                FOREIGN KEY (field_id)
                                REFERENCES fields(field_id)
                        )
                    ';
                EXCEPTION
                    WHEN OTHERS THEN
                        IF SQLCODE != -955 THEN
                            RAISE;
                        END IF;
                END;
            """)

        connection.commit()
        return True, "Tabela FERTILIZER_APPLICATIONS criada com sucesso ou já existente."

    except Exception as error:
        return False, f"Erro ao criar tabela FERTILIZER_APPLICATIONS: {error}"

    finally:
        if connection:
            connection.close()

def create_production_records_table():
    """
    Creates the production_records table if it does not exist.
    """
    connection = None

    try:
        connection = get_oracle_connection()

        with connection.cursor() as cursor:
            cursor.execute("""
                BEGIN
                    EXECUTE IMMEDIATE '
                        CREATE TABLE production_records (
                            record_id NUMBER PRIMARY KEY,
                            field_id NUMBER NOT NULL,
                            harvest_name VARCHAR2(100) NOT NULL,
                            production_amount NUMBER(10,2) NOT NULL,
                            record_date VARCHAR2(20) NOT NULL,
                            CONSTRAINT fk_production_field
                                FOREIGN KEY (field_id)
                                REFERENCES fields(field_id)
                        )
                    ';
                EXCEPTION
                    WHEN OTHERS THEN
                        IF SQLCODE != -955 THEN
                            RAISE;
                        END IF;
                END;
            """)

        connection.commit()
        return True, "Tabela PRODUCTION_RECORDS criada com sucesso ou já existente."

    except Exception as error:
        return False, f"Erro ao criar tabela PRODUCTION_RECORDS: {error}"

    finally:
        if connection:
            connection.close()

def insert_field(field_data):
    """
    Inserts a field record into the Oracle database.
    """
    connection = None

    try:
        connection = get_oracle_connection()

        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO fields (field_id, name, area, crop_type)
                VALUES (:field_id, :name, :area, :crop_type)
            """, field_data)

        connection.commit()
        return True, "Talhão salvo no Oracle com sucesso."

    except Exception as error:
        if connection:
            connection.rollback()
        return False, f"Erro ao salvar talhão no Oracle: {error}"

    finally:
        if connection:
            connection.close()

def insert_fertilizer_application(application_data):
    """
    Inserts a fertilizer application record into the Oracle database.
    """
    connection = None

    try:
        connection = get_oracle_connection()

        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO fertilizer_applications (
                    application_id,
                    field_id,
                    fertilizer_type,
                    quantity,
                    application_date
                )
                VALUES (
                    :application_id,
                    :field_id,
                    :fertilizer_type,
                    :quantity,
                    :application_date
                )
            """, application_data)

        connection.commit()
        return True, "Aplicação de fertilizante salva no Oracle com sucesso."

    except Exception as error:
        if connection:
            connection.rollback()
        return False, f"Erro ao salvar aplicação no Oracle: {error}"

    finally:
        if connection:
            connection.close()

def insert_production_record(record_data):
    """
    Inserts a production record into the Oracle database.
    """
    connection = None

    try:
        connection = get_oracle_connection()

        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO production_records (
                    record_id,
                    field_id,
                    harvest_name,
                    production_amount,
                    record_date
                )
                VALUES (
                    :record_id,
                    :field_id,
                    :harvest_name,
                    :production_amount,
                    :record_date
                )
            """, record_data)

        connection.commit()
        return True, "Registro de produção salvo no Oracle com sucesso."

    except Exception as error:
        if connection:
            connection.rollback()
        return False, f"Erro ao salvar produção no Oracle: {error}"

    finally:
        if connection:
            connection.close()

def list_fields_from_oracle():
    """
    Returns all fields stored in Oracle.
    """
    connection = None

    try:
        connection = get_oracle_connection()

        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT field_id, name, area, crop_type
                FROM fields
                ORDER BY field_id
            """)
            rows = cursor.fetchall()

        return True, rows

    except Exception as error:
        return False, f"Erro ao listar talhões no Oracle: {error}"

    finally:
        if connection:
            connection.close()

def list_fertilizer_applications_from_oracle():
    """
    Returns all fertilizer applications stored in Oracle.
    """
    connection = None

    try:
        connection = get_oracle_connection()

        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                    application_id,
                    field_id,
                    fertilizer_type,
                    quantity,
                    application_date
                FROM fertilizer_applications
                ORDER BY application_id
            """)
            rows = cursor.fetchall()

        return True, rows

    except Exception as error:
        return False, f"Erro ao listar aplicações no Oracle: {error}"

    finally:
        if connection:
            connection.close()

def list_production_records_from_oracle():
    """
    Returns all production records stored in Oracle.
    """
    connection = None

    try:
        connection = get_oracle_connection()

        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                    record_id,
                    field_id,
                    harvest_name,
                    production_amount,
                    record_date
                FROM production_records
                ORDER BY record_id
            """)
            rows = cursor.fetchall()

        return True, rows

    except Exception as error:
        return False, f"Erro ao listar produções no Oracle: {error}"

    finally:
        if connection:
            connection.close()

def delete_field_from_oracle(field_id):
    """
    Deletes a field from the Oracle database by field_id.
    """
    connection = None

    try:
        connection = get_oracle_connection()

        with connection.cursor() as cursor:
            cursor.execute("""
                DELETE FROM fields
                WHERE field_id = :field_id
            """, {"field_id": field_id})

        connection.commit()
        return True, "Talhão excluído do Oracle com sucesso."

    except Exception as error:
        if connection:
            connection.rollback()
        return False, f"Erro ao excluir talhão do Oracle: {error}"

    finally:
        if connection:
            connection.close()

def delete_fertilizer_applications_by_field_id(field_id):
    """
    Deletes fertilizer applications by field_id.
    """
    connection = None

    try:
        connection = get_oracle_connection()

        with connection.cursor() as cursor:
            cursor.execute("""
                DELETE FROM fertilizer_applications
                WHERE field_id = :field_id
            """, {"field_id": field_id})

        connection.commit()
        return True, "Aplicações vinculadas excluídas do Oracle com sucesso."

    except Exception as error:
        if connection:
            connection.rollback()
        return False, f"Erro ao excluir aplicações no Oracle: {error}"

    finally:
        if connection:
            connection.close()

def delete_production_records_by_field_id(field_id):
    """
    Deletes production records by field_id.
    """
    connection = None

    try:
        connection = get_oracle_connection()

        with connection.cursor() as cursor:
            cursor.execute("""
                DELETE FROM production_records
                WHERE field_id = :field_id
            """, {"field_id": field_id})

        connection.commit()
        return True, "Registros de produção vinculados excluídos do Oracle com sucesso."

    except Exception as error:
        if connection:
            connection.rollback()
        return False, f"Erro ao excluir produções no Oracle: {error}"

    finally:
        if connection:
            connection.close()

def initialize_oracle_database():
    """
    Creates all required Oracle tables for the system.
    """
    messages = []

    fields_success, fields_message = create_fields_table()
    messages.append(fields_message)

    applications_success, applications_message = create_fertilizer_applications_table()
    messages.append(applications_message)

    production_success, production_message = create_production_records_table()
    messages.append(production_message)

    all_success = fields_success and applications_success and production_success

    return all_success, messages

def field_exists(field_id):
    """
    Checks if a field already exists in Oracle.
    """
    connection = None

    try:
        connection = get_oracle_connection()

        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT COUNT(*)
                FROM fields
                WHERE field_id = :field_id
            """, {"field_id": field_id})

            result = cursor.fetchone()
            return result[0] > 0

    finally:
        if connection:
            connection.close()

def fertilizer_application_exists(application_id):
    """
    Checks if a fertilizer application already exists in Oracle.
    """
    connection = None

    try:
        connection = get_oracle_connection()

        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT COUNT(*)
                FROM fertilizer_applications
                WHERE application_id = :application_id
            """, {"application_id": application_id})

            result = cursor.fetchone()
            return result[0] > 0

    finally:
        if connection:
            connection.close()

def production_record_exists(record_id):
    """
    Checks if a production record already exists in Oracle.
    """
    connection = None

    try:
        connection = get_oracle_connection()

        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT COUNT(*)
                FROM production_records
                WHERE record_id = :record_id
            """, {"record_id": record_id})

            result = cursor.fetchone()
            return result[0] > 0

    finally:
        if connection:
            connection.close()

def sync_fields_to_oracle(fields):
    """
    Synchronizes JSON fields data to Oracle.
    Inserts only records that do not already exist.
    """
    inserted_count = 0

    for field in fields:
        if not field_exists(field["field_id"]):
            success, _ = insert_field(field)
            if success:
                inserted_count += 1

    return inserted_count

def sync_fertilizer_applications_to_oracle(applications):
    """
    Synchronizes JSON fertilizer applications data to Oracle.
    Inserts only records that do not already exist.
    """
    inserted_count = 0

    for application in applications:
        if not fertilizer_application_exists(application["application_id"]):
            success, _ = insert_fertilizer_application(application)
            if success:
                inserted_count += 1

    return inserted_count

def sync_production_records_to_oracle(production_records):
    """
    Synchronizes JSON production records data to Oracle.
    Inserts only records that do not already exist.
    """
    inserted_count = 0

    for record in production_records:
        if not production_record_exists(record["record_id"]):
            success, _ = insert_production_record(record)
            if success:
                inserted_count += 1

    return inserted_count

def sync_json_data_to_oracle(fields, applications, production_records):
    """
    Synchronizes JSON data to Oracle after table initialization.
    """
    fields_inserted = sync_fields_to_oracle(fields)
    applications_inserted = sync_fertilizer_applications_to_oracle(applications)
    production_inserted = sync_production_records_to_oracle(production_records)

    return {
        "fields_inserted": fields_inserted,
        "applications_inserted": applications_inserted,
        "production_inserted": production_inserted
    }