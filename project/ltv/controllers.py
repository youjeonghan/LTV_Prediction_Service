def make_pipeline(target, percentile):
    return [
        {"$sort": {"imps_cnt": -1}},
        {"$limit": percentile},
        {"$sortByCount": f"${target}"},
        {
            "$project": {
                "count": 1,
                "percentile": {
                    "$round": [
                        {
                            "$multiply": [
                                {"$divide": ["$count", {"$literal": percentile}]},
                                100,
                            ]
                        },
                        2,
                    ]
                },
            }
        },
    ]
