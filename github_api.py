from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

GITHUB_API_URL = "https://api.github.com/users"

@app.get("/github/{username}")
def get_github_profile(username: str):
    url = f"{GITHUB_API_URL}/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    raise HTTPException(status_code=response.status_code, detail="GitHub User not found")
@app.get("/github/{username}/repos")
def get_github_repos(username: str):
    url = f"{GITHUB_API_URL}/{username}/repos"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    raise HTTPException(status_code=response.status_code, detail="Repositories not found")
@app.get("/github/{username}/followers")
def get_github_followers(username: str):
    url = f"{GITHUB_API_URL}/{username}/followers"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    raise HTTPException(status_code=response.status_code, detail="Followers not found")
