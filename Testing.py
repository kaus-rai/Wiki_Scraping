import unittest
from Wiki_Info import scraper

class ScraperTests(unittest.TestCase):
    def testUniversitites(self):
        print('Testing University of Nottingham')
        uniinfo = scraper('University of Nottingham')
        self.assertEquals(uniinfo['Motto'],'Sapientia urbs conditur')
        self.assertEquals(uniinfo['Chancellor'],'Sir Andrew Witty')
        self.assertEquals(uniinfo['Budget'],'£637.6 million (2016-17)[1]')
        self.assertEquals(uniinfo['Location'],'Nottingham, England, UK')
        print()

        print('Testing University of Warsaw')
        uniinfo = scraper('University of Warsaw')
        self.assertEquals(uniinfo['Type'],'Public')
        self.assertEquals(uniinfo['Established'],'1816 (202 years ago)')
        self.assertEquals(uniinfo['Location'],'Sapientia urbs conditur')
        print()

        print('Testing University of Santo Tomas')
        uniinfo = scraper('University of Santo Tomas')
        self.assertEquals(uniinfo['Motto'],'Veritas in Caritate')
        self.assertEquals(uniinfo['Chancellor'],'Very Rev. Fr. Bruno Cadoré, O.P., M.D.')
        self.assertEquals(uniinfo['Location'],'España Boulevard, Sampaloc, Manila, Philippines')
        print()

        print('Testing Peking University')
        uniinfo = scraper('Peking University')
        self.assertEquals(uniinfo['Chancellor'],'Very Rev. Fr. Bruno Cadoré, O.P., M.D.')
        self.assertEquals(uniinfo['President'],'Lin Jianhua')
        self.assertEquals(uniinfo['Location'],'Haidian District, Beijing, China')
        print()

        print('Testing Chihuahua Institute of Technology')
        uniinfo = scraper('Chihuahua Institute of Technology')
        self.assertEquals(uniinfo['Motto'],'La Técnica por el engrandecimiento de México')
        self.assertEquals(uniinfo['Motto in English'],'Technology for the aggrandizement of Mexico')
        self.assertEquals(uniinfo['Established'],'1948')
        print()

        print('Testing University of Pardubice')
        uniinfo = scraper('University of Pardubice')
        self.assertEquals(uniinfo['Established'],'1950')
        self.assertEquals(uniinfo['Students'],'9,200')
        self.assertEquals(uniinfo['Location'],'Pardubice, Czech Republic')
        print()


if __name__ == '__main__':
    unittest.main()
