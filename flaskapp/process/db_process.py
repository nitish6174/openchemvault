from flaskapp.shared_variables import mongo


def get_attribute_stats(round_vals=False):
    db = mongo.db
    stats = list(db.attr_stats.find({}))[0]
    if round_vals is True:
        for k, v in stats.items():
            if (k != "_id") and (type(v["min"]) is not int):
                v["min"] = round((v["min"]*1000) - 1) / 1000.0
                v["max"] = round((v["max"]*1000) + 1) / 1000.0
    return stats
