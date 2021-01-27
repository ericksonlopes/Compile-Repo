class CompileRepo:
    def __init__(self):
        self.url_git = 'https://github.com'

        with open('repositories.txt', 'r') as file:
            self.repos = file.read().split()

        for repo in self.repos:
            url_repo = self.url_git + '/' + repo
            print(url_repo)


if __name__ == '__main__':
    CompileRepo()
