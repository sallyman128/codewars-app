class Analytics:
    def __init__(self, name, leaderboardPosition, language_scores, topLanguage):
        self.name = name
        self.leaderboardPosition = leaderboardPosition
        self.language_scores = language_scores
        self.topLanguage = topLanguage
    
    def to_dict(self):
        return {
            'name': self.name,
            'leaderboardPosition': self.leaderboardPosition,
            'language_scores': self.language_scores ,
            'topLanguage': self.topLanguage
        }