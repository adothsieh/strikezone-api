class PitchGlossary:
    def __init__(self):
        self.glossary = {}
        self.glossary['FA'] = ('Fastball', '#FFFD98') 
        self.glossary['FF'] = ('Four-seam Fastball', '#BDE4A7')
        self.glossary['FT'] = ('Two-seam Fastball', '#B3D2B2')
        self.glossary['FC'] = ('Cutter', '#9FBBCC')
        self.glossary['SI'] = ('Sinker', '#7A9CC6')
        self.glossary['SF'] = ('Split-finger Fastball', '#61E8E1')
        self.glossary['FS'] = ('Splitter', '#F25757')
        self.glossary['SL'] = ('Slider', '#3626A7')
        self.glossary['CH'] = ('Changeup', '#E55812')
        self.glossary['CU'] = ('Curveball', '#FF4365')
        self.glossary['KC'] = ('Knuckle-curve', '#036D19')
        self.glossary['KN'] = ('Knuckleball', '#A67DB8')
        self.glossary['EP'] = ('Eephus', '#8CFF98')

    def get_pitch(self, abbr):
        return self.glossary[abbr][0]

    def colourMap(self, abbr):
        return self.glossary[abbr][1]

class ResultGlossary:
    def __init__(self):
        self.glossary = {}
        self.glossary['Groundout'] = '#BF1A2F'
        self.glossary['Strikeout'] = '#F00699'
        self.glossary['Lineout'] = '#454E9E'
        self.glossary['Pop Out'] = '#018E42'
        self.glossary['Flyout'] = '#F7D002'
        self.glossary['Single'] = '#7AE7C7'
        self.glossary['Double'] = '#E16036'
        self.glossary['Triple'] = '#5F0F40'
        self.glossary['Home Run'] = '#306B34'
        self.glossary['Walk'] = '#141414'
        self.glossary['Hit By Pitch'] = '#F56416'
        self.glossary['Grounded Into DP'] = '#E28413'
        self.glossary['Double Play'] = '#44BBA4'

    def colourMap(self, result):
        return self.glossary[result]