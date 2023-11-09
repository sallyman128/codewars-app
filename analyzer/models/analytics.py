class Analytics:
    def __init__(self, name, leaderboardPosition, languages, topLanguage):
        self.name = name
        self.leaderboardPosition = leaderboardPosition
        self.languages = languages
        self.topLanguage = topLanguage
    
    def to_dict(self):
        return {
            'name': self.name,
            'leaderboardPosition': self.leaderboardPosition,
            'languages': self.languages ,
            'topLanguage': self.topLanguage
        }