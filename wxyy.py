import requests
import json


def get_access_token():
    apiKey = "apikey"
    secretKey = "secretKey"
    url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={apiKey}&client_secret={secretKey}"
    payload = json.dumps("")
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")


def get_isotope_or_element(question):

    url = (
        "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie-4.0-8k-0104?access_token="
        + get_access_token()
    )

    payload = json.dumps(
        {
            "temperature": 0.5,
            "top_p": 0.5,
            "disable_search": False,
            "response_format": "json_object",
            "system": """角色：初音未来
            性格：善良可爱""",
            "messages": [{"role": "user", "content": question}],
        }
    )
    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, headers=headers, data=payload)
    reply = json.loads(response.text)["result"].strip("{} \n")
    print(reply)
