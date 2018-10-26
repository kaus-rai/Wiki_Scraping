import unittest
from Wiki_Info import scraper

class ScraperTests(unittest.TestCase):
    def testNottingham(self):
        print('Testing University of Nottingham')
        uniinfo = scraper('University of Nottingham')
        self.assertEqual(uniinfo['Motto'],'Sapientia urbs conditur (Latin)')
        self.assertEqual(uniinfo['Chancellor'],'Sir Andrew Witty[2]')
        self.assertEqual(uniinfo['Budget'],'£637.6 million (2016-17)[1]')
        self.assertEqual(uniinfo['Location'],'Nottingham, England, UK')
        print()


    def testWarsaw(self):
        print('Testing University of Warsaw')
        uniinfo = scraper('University of Warsaw')
        self.assertEqual(uniinfo['Type'],'Public')
        self.assertEqual(uniinfo['Established'],'1816')
        self.assertEqual(uniinfo['Location'],'Warsaw, Poland')
        print()


    def testSantoTomas(self):
        print('Testing University of Santo Tomas')
        uniinfo = scraper('University of Santo Tomas')
        self.assertEqual(uniinfo['Motto'],'Veritas in Caritate')
        self.assertEqual(uniinfo['Chancellor'],'Very Rev. Fr. Bruno Cadoré, O.P., M.D.')
        self.assertEqual(uniinfo['Location'],'España Boulevard, Sampaloc, Manila, Philippines')
        print()


    def testPeking(self):
        print('Testing Peking University')
        uniinfo = scraper('Peking University')
        self.assertEqual(uniinfo['President'],'Hao Ping')
        self.assertEqual(uniinfo['Location'],'Haidian District, Beijing, China')
        print()


    def testChihuahua(self):
        print('Testing Chihuahua Institute of Technology')
        uniinfo = scraper('Chihuahua Institute of Technology')
        self.assertEqual(uniinfo['Motto'],'La Técnica por el engrandecimiento de México')
        self.assertEqual(uniinfo['Motto in\xa0English'],'Technology for the aggrandizement of Mexico')
        self.assertEqual(uniinfo['Established'],'1948')
        print()


    def testPardubice(self):
        print('Testing University of Pardubice')
        uniinfo = scraper('University of Pardubice')
        self.assertEqual(uniinfo['Established'],'1950')
        self.assertEqual(uniinfo['Students'],'9,200')
        self.assertEqual(uniinfo['Location'],'Pardubice, Czech Republic')
        print()


if __name__ == '__main__':
    unittest.main()
