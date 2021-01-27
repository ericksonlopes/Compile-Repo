class CompileRepo:
    def __init__(self):
        with open('repositories.txt', 'r') as file:
            self.repos = file.read().split()

        print(self.repos)


if __name__ == '__main__':
    CompileRepo()
