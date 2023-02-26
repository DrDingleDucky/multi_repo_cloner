import git
import requests

github_user = input("username: -> ")

response = requests.get(f"https://api.github.com/users/{github_user}/repos")
repo_urls = [repo["html_url"] for repo in response.json()]

for i, repo_url in enumerate(repo_urls):
    repo_name = repo_url.split("/")[-1].replace(".get", "")
    git.Repo.clone_from(repo_url, repo_name)
    print(f"{i + 1}: cloned '{repo_name}' successfully")
