def insert_update_sql_request(table_name, columns_list, primary_key) :
    n = len(columns_list)
    values_str = []
    set_str = []
    for i in range(n) :
        values_str.append("%s")
    for column in columns_list :
        if column != "id" :
            set_str.append(column + " = excluded." + column)
    values_str = str(tuple(values_str))
    set_str = str(tuple(set_str)).replace("(", "").replace(")", "") 
    upsert_sql_request = (
        "INSERT INTO "
        + table_name + " " + str(columns_list) + " "
        + "VALUES " + values_str + " "
        + "ON CONFLICT " + str(primary_key).replace(",)", ")") + " DO UPDATE SET " + set_str + ";"
    )
    upsert_sql_request = upsert_sql_request.replace("'", "")
    print(upsert_sql_request)
    return upsert_sql_request

def get_primary_key(table_name) :
    get_primary_key_sql_request = (
        "SELECT column_name "
        + "FROM information_schema.constraint_column_usage "
        + "WHERE table_name = '" + table_name + "' AND constraint_name = ("
            + "SELECT constraint_name "
            + "FROM information_schema.table_constraints "
            + "WHERE table_name = '" + table_name + "' AND constraint_type = 'PRIMARY KEY');"
    )
    return get_primary_key_sql_request