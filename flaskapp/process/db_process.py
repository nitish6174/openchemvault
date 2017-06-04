import flaskapp.shared_variables as var


def get_attribute_stats(round_vals=False):
    db = var.mongo.db
    stats = list(db.stats.find({}))[0]
    if round_vals is True:
        for k, v in stats.items():
            if (k != "_id") and (type(v["min"]) is not int):
                v["min"] = round((v["min"]*1000) - 1) / 1000.0
                v["max"] = round((v["max"]*1000) + 1) / 1000.0
    return stats
