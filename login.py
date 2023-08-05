from duneanalytics import DuneAnalytics

def get_query_id_from_url(url):
    parts = url.split('/')
    query_id = parts[-2] if len(parts) > 2 else None
    return query_id

def get_data(username, password, query_id):
    dune = DuneAnalytics(username, password)
    dune.login()
    dune.fetch_auth_token()
    result_id = dune.query_result_id(query_id)
    data = dune.query_result(result_id)
    return data

volume_per_dex_url = "https://dune.com/queries/1347247/2299026"
agg_OI = "https://dune.com/queries/2660944/4423130"

query_id = get_query_id_from_url(volume_per_dex_url)

data1 = get_data('leviathan_dionysian', 'ruz.jzy7hfn4vmu2GCU', query_id)
print(data1)



