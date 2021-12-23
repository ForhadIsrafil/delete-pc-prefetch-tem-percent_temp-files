from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults
zillow_data = ZillowWrapper('X1-ZWz1iet37nlyiz_4lr3d')
deep_search_response = zillow_data.get_deep_search_results('2114 Bigelow Ave', '98109', True)
result = GetDeepSearchResults(deep_search_response)
print(result.zillow_id)
print(result)
print(result.bathrooms)