import requests
class MotivationAPI:
    def get_quote(self):
        url = "https://zenquotes.io/api/random"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.exceptions.Timeout:
            return "Error : the request took too long"
        except requests.exceptions.ConnectionError:
            return "Error : no internet connexion"
        except requests.exceptions.RequestException as e:
            return f"Network error: {e}"
        
        try:
            data = response.json()
        except ValueError:
            return "Error : invalide JSON response" 
        try:
            if not data:
                return "Error : no citation found"
            quote = data[0]["q"]
            author = data[0]["a"]
            return f"{quote} - {author}"
        except (IndexError, KeyError):
            return "Error : unexpected JSON structure"



