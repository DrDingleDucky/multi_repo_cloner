import git
import requests

github_user = "MrDingleDucky"

response = requests.get(f"https://api.github.com/users/{github_user}/repos")
repo_urls = [repo["html_url"] for repo in response.json()]

index = 1

for repo_url in repo_urls:
    repo_name = repo_url.split("/")[-1].replace(".get", "")
    git.Repo.clone_from(repo_url, repo_name)
    print(f"{index}: Cloned '{repo_name}' SUCCESSFULLY")
    index += 1

print("Done")
