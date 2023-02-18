from resources.mysql_data_service import MySQLDataService, MySQLDataServiceConfig


def get_svc() -> MySQLDataService:
    config = MySQLDataServiceConfig()
    svc = MySQLDataService(config)
    return svc


def t1():
    get_svc()


def t_where_clause():
    predicate = {"nameLast": "Williams", "nameFirst": "Ted", "H": 72}
    svc = get_svc()
    res, args = svc.predicate_to_where_clause_args(predicate)
    print("t_where_clause: clause=", res, "args=", args)


def t_build_sql():
    predicate = {"nameLast": "Williams", "nameFirst": "Ted"}
    svc = get_svc()
    res = svc.retrieve("lahmansbaseballdb", "people",
                                 predicate,
                                 ["nameLast", "nameFirst", "birthCity"])
    print("t_build_sql: clause=", res)


if __name__ == "__main__":
    t_build_sql()
