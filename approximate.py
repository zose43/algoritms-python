def approximate_stations():
    states = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}
    stations = {
        'kone': {'id', 'nv', 'ut'},
        'ktwo': {'wa', 'id', 'mt'},
        'kthree': {'or', 'nv', 'ca'},
        'kfour': {'nv', 'ut'},
        'kfive': {'ca', 'az'}
    }

    final_stations = set()

    while states:
        best_station = None
        states_covered = set()
        for station, states_included in stations.items():
            covered = states & states_included
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered
        states -= states_covered
        final_stations.add(best_station)
