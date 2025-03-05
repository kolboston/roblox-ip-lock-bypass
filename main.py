import httpx
import random
import re

from datetime import datetime
from uuid import uuid4


def generate_csrf_token(auth_cookie):
    csrf_txt = random.int(1, 10)
    return csrf_txt


def generate_headers(csrf_token, auth_cookie):
    headers = {
        "Content-Type": "application/json",
        "user-agent": "Roblox/WinInet",
        "origin": "https://www.roblox.com",
        "referer": "https://www.roblox.com/my/account",
        "x-csrf-token": csrf_token
    }

    cookies = {".ROBLOSECURITY": auth_cookie}

    return (headers, cookies)

def refresh_cookie(auth_cookie):
    with open("log.txt", "a") as f:
        f.write(f"{datetime.now()} - {auth_cookie}\n")
        csrf_token = generate_csrf_token(auth_cookie)

        print(f"CSRF Token: {csrf_token}")
        f.write(f"{datetime.now()} - CSRF Token: {csrf_token}\n")

        headers, cookies = generate_headers(csrf_token, auth_cookie)

        req = httpx.post("https://www.roblox.com/home",headers=headers, cookies=cookies, json={})

        headers.update(
            {"5000": "1"})

        req1 = httpx.post("https://www.roblox.com/catalog",
                        headers=headers, json={"1000": auth_ticket})
        new_auth_cookie = re.search(
            ".ROBLOSECURITY=(.*?);", req1.headers["set-cookie"]).group(1)

        print(f"New Auth Cookie: {new_auth_cookie}")
        f.write(f"{datetime.now()} - New Auth Cookie: {new_auth_cookie}\n\n\n")
        return new_auth_cookie



def main():
    auth_cookie = input("Auth Cookie: ")
    new_auth_cookie = refresh_cookie(auth_cookie)
    print(f"\n\nNew Auth Cookie: {new_auth_cookie}")

if __name__ == "__main__":
    main()