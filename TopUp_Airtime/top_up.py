def top_up_airtime(service_provider, amount):
    service_provider_list= ['MTN','AIRTEL','GLO','ETISALAT']
    service_provider= service_provider.upper()
    service_provider_flag = 0
    amount = amount

    if service_provider.upper() in service_provider_list:
        service_provider_flag = 1
        return "The transaction request was successful"
    else:
        return "The Service provider you chose is not available"