import unittest

from lxml import etree

from appscanner.model.assessment import Assessment, Assessments


class TestsAssessment(unittest.TestCase):
    def test_create_from_valid_xml(self):
        valid_xml = "<Assessment><AssessmentId>e531b427-aa1b-48df-af99-714f803b15ed</AssessmentId><AssessmentName>Site Blindado E-commerce - HIGH</AssessmentName><IsApiSafe>True</IsApiSafe><Url>https://www.mydomain.com.br/</Url><ApplicationId>f5cb1fa9-1e19-4557-a745-84f04d926c7d</ApplicationId></Assessment>"

        assessment = Assessment.from_etree(etree.XML(valid_xml))

        self.assertEqual('e531b427-aa1b-48df-af99-714f803b15ed',
                         assessment.AssessmentId)
        self.assertEqual('Site Blindado E-commerce - HIGH',
                         assessment.AssessmentName)
        self.assertEqual(True, assessment.IsApiSafe)
        self.assertEqual('https://www.mydomain.com.br/', assessment.Url)
        self.assertEqual('f5cb1fa9-1e19-4557-a745-84f04d926c7d',
                         assessment.ApplicationId)


class TestsAssessments(unittest.TestCase):
    def test_create_from_valid_xml(self):
        valid_xml = open('test_files/Assessments.xml', 'rb').read()

        assessments = Assessments.from_etree(etree.XML(valid_xml))

        self.assertEqual('171ce949-eced-4ee1-8123-2d704f2d130b',
                         assessments[0].AssessmentId)
        self.assertEqual('Site Blindado E-commerce',
                         assessments[0].AssessmentName)
        self.assertEqual(True, assessments[1].IsApiSafe)
        self.assertEqual('https://www.mydomain.com.br/',
                         assessments[0].Url)
        self.assertEqual('f5cb1fa9-1e19-4557-a745-84f04d926c7d',
                         assessments[0].ApplicationId)

        self.assertEqual('e531b427-aa1b-48df-af99-714f803b15ed',
                         assessments[1].AssessmentId)
        self.assertEqual('Site Blindado E-commerce - HIGH',
                         assessments[1].AssessmentName)
        self.assertEqual(True, assessments[1].IsApiSafe)
        self.assertEqual('https://www.mydomain.com.br/',
                         assessments[1].Url)
        self.assertEqual('f5cb1fa9-1e19-4557-a745-84f04d926c7d',
                         assessments[1].ApplicationId)