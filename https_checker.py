def https_checker(host):
    import requests
    try :
        resp = requests.get(host)
        if resp.status_code == 200:
            return True
        else :
            return False
            
    except requests.exceptions.RequestException as e :
        print("Error : {}".format(str(e)))