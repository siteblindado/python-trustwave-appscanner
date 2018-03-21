import unittest

from lxml import etree

from appscanner.model.assessment import Assessment, Assessments


class TestsAssessment(unittest.TestCase):
    def test_create_from_valid_xml(self):
        valid_xml = '<Assessment><AssessmentId>e531b427-aa1b-48df-af99-714f80' \
                    '3b15ed</AssessmentId><AssessmentName>Site Blindado' \
                    ' E-commerce - HIGH</AssessmentName><IsApiSafe>True' \
                    '</IsApiSafe><Url>https://www.mydomain.com.br/</Url>' \
                    '<ApplicationId>f5cb1fa9-1e19-4557-a745-84f04d926c7d' \
                    '</ApplicationId></Assessment>'

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
        valid_xml = open(
            'tests/test_files/assessments_by_app_id.xml', 'rb').read()

        assessments = Assessments.from_etree(etree.XML(valid_xml))

        self.assertEqual('bb8c6a5d-b1fc-40ea-9c58-1d58efbdb023',
                         assessments[0].AssessmentId)
        self.assertEqual('E-commerce',
                         assessments[0].AssessmentName)
        self.assertEqual(True, assessments[0].IsApiSafe)
        self.assertEqual('http://www.mydomain.com.br',
                         assessments[0].Url)
        self.assertEqual('dcb434b9-8101-4a85-9bf5-57396b283c7e',
                         assessments[0].ApplicationId)
