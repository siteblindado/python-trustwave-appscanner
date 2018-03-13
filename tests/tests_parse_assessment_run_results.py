import unittest
from datetime import datetime

from lxml import etree

from appscanner.model.assessment_run_result import AssessmentRunInfo, SmartAttackInfo, \
    ReportItem, Category, PagesVisited, AssessmentRunData, SmartAttacks


class TestsAssessmentRunInfo(unittest.TestCase):
    def test_create_from_valid_xml(self):
        valid_xml = '<AssessmentRunInfo><HarmScore>0</HarmScore><RiskFactor>1</RiskFactor><Status>Complete</Status><AttackCount>315550</AttackCount><MaxPagesVisited>100</MaxPagesVisited><StartTime>09/26/2017 17:26:02</StartTime><EndTime>09/26/2017 23:53:06</EndTime></AssessmentRunInfo>'

        run_info = AssessmentRunInfo.from_etree(etree.XML(valid_xml))

        self.assertEqual(0, run_info.HarmScore)
        self.assertEqual(1, run_info.RiskFactor)
        self.assertEqual('Complete', run_info.Status)
        self.assertEqual(315550, run_info.AttackCount)
        self.assertEqual(100, run_info.MaxPagesVisited)
        self.assertEqual(datetime(2017, 9, 26, 17, 26, 2), run_info.StartTime)
        self.assertEqual(datetime(2017, 9, 26, 23, 53, 6), run_info.EndTime)


class TestsSmartAttackInfo(unittest.TestCase):
    def test_create_from_valid_xml(self):
        valid_xml = '<Assessment PolicyId="67a127f2-85fc-4797-8092-d4fe2312acef" PolicyVersion="1.2" CenzicId="CPL0002110" Severity="Default" VulnerabilityIds="CWE-548"><SmartAttackName>Directory Browsing - [OWASP 2013 A 5]</SmartAttackName><Description>Directory Browsing is a vulnerability caused by unintentionally disclosing directory listings to users. The SmartAttack attempts to retrieve and identify such listings and reports them as vulnerabilities based on the assumption that the listings are unintended.</Description><TechnicalDescription>Directories on the web server or applications are typically locked down to prevent remote browsing when the directory contains executables, text files, documentation, or application-related install or configuration materials. In such cases either the entire directory is configured to block access, or access is granted on a per file basis, requiring a precise request to access objects in the directory. Directory listing can be prevented in server configuration files, but may also arise from vulnerability in a particular application.</TechnicalDescription><HowItWorks>The SmartAttack examines each page and attempts to access directory listing for the page by making an http request using the url of the parent directory of the page.</HowItWorks><Impact>If a Web application is vulnerable to directory browsing, an attacker can gain information about the web application by browsing directory listings that reveal files and folder hierarchy in the application. These resources may store sensitive information about web applications and operational systems, such as source code, credentials, internal network addressing, and so on which can be used to exploit vulnerabilities in the web application.</Impact><Remediation>Obtaining directory lists gives an attacker useful information when planning attacks against your server or your application. Follow these guidelines to prevent unintended information disclosure:</Remediation></Assessment>'

        attack_info = SmartAttackInfo.from_etree(etree.XML(valid_xml))

        self.assertEqual("67a127f2-85fc-4797-8092-d4fe2312acef", attack_info.PolicyId)
        self.assertEqual("1.2", attack_info.PolicyVersion)
        self.assertEqual("CPL0002110", attack_info.CenzicId)
        self.assertEqual("Default", attack_info.Severity)
        self.assertEqual("CWE-548", attack_info.VulnerabilityIds)
        self.assertEqual("Directory Browsing - [OWASP 2013 A 5]", attack_info.SmartAttackName)
        self.assertEqual("Directory Browsing is a vulnerability caused by unintentionally disclosing directory listings to users. The SmartAttack attempts to retrieve and identify such listings and reports them as vulnerabilities based on the assumption that the listings are unintended.", attack_info.Description)
        self.assertEqual("Directories on the web server or applications are typically locked down to prevent remote browsing when the directory contains executables, text files, documentation, or application-related install or configuration materials. In such cases either the entire directory is configured to block access, or access is granted on a per file basis, requiring a precise request to access objects in the directory. Directory listing can be prevented in server configuration files, but may also arise from vulnerability in a particular application.", attack_info.TechnicalDescription)
        self.assertEqual("The SmartAttack examines each page and attempts to access directory listing for the page by making an http request using the url of the parent directory of the page.", attack_info.HowItWorks)
        self.assertEqual("If a Web application is vulnerable to directory browsing, an attacker can gain information about the web application by browsing directory listings that reveal files and folder hierarchy in the application. These resources may store sensitive information about web applications and operational systems, such as source code, credentials, internal network addressing, and so on which can be used to exploit vulnerabilities in the web application.", attack_info.Impact)
        self.assertEqual("Obtaining directory lists gives an attacker useful information when planning attacks against your server or your application. Follow these guidelines to prevent unintended information disclosure:", attack_info.Remediation)


class TestsReportItem(unittest.TestCase):
    def test_create_from_valid_xml(self):
        valid_xml = '<ReportItem Id="3040478"><ReportItemType>Pass</ReportItemType><ReportItemCreateDate>9/26/2017 11:52:52 PM</ReportItemCreateDate><Severity>Medium</Severity><HarmScore>160</HarmScore><CVSSBaseScore/><ComputedHarmScore>0</ComputedHarmScore><Count>1</Count><Message>No directory listings found.</Message><GlobalizedMessage>czTranslate{3686053274}</GlobalizedMessage><Url/><TraversalName>[Default Spider]</TraversalName><Filtered>0</Filtered><HttpRequest/><HttpResponse/><StructuredData/></ReportItem>'

        report_item = ReportItem.from_etree(etree.XML(valid_xml))

        self.assertEqual("3040478", report_item.Id)
        self.assertEqual("Pass", report_item.ReportItemType)
        self.assertEqual(datetime(2017, 9, 26, 23, 52, 52), report_item.ReportItemCreateDate)
        self.assertEqual("Medium", report_item.Severity)
        self.assertEqual(160, report_item.HarmScore)
        self.assertEqual(None, report_item.CVSSBaseScore)
        self.assertEqual(0, report_item.ComputedHarmScore)
        self.assertEqual(1, report_item.Count)
        self.assertEqual("No directory listings found.", report_item.Message)
        self.assertEqual("czTranslate{3686053274}", report_item.GlobalizedMessage)
        self.assertEqual(None, report_item.Url)
        self.assertEqual("[Default Spider]", report_item.TraversalName)
        self.assertEqual(0, report_item.Filtered)
        self.assertEqual(None, report_item.HttpRequest)
        self.assertEqual(None, report_item.HttpResponse)
        self.assertEqual(None, report_item.StructuredData)


class TestsCategory(unittest.TestCase):
    def test_create_from_valid_xml(self):
        valid_xml = '<Category><Name>OWASP-2013</Name></Category>'

        category = Category.from_etree(etree.XML(valid_xml))

        self.assertEqual("OWASP-2013", category.Name)


class TestsPagesVisited(unittest.TestCase):
    def test_create_from_valid_xml(self):
        valid_xml = '<PagesVisited><Url>www.mydomain.com.br/</Url><Url>www.mydomain.com.br/ProdutoBusca/Busca-site</Url><Url>www.mydomain.com.br/login</Url></PagesVisited>'

        pages_visited = PagesVisited.from_etree(etree.XML(valid_xml))

        self.assertEqual(3, len(pages_visited))
        self.assertEqual('www.mydomain.com.br/', pages_visited[0])
        self.assertEqual('www.mydomain.com.br/ProdutoBusca/Busca-site', pages_visited[1])
        self.assertEqual('www.mydomain.com.br/login', pages_visited[2])


class TestsAssessmentRunData(unittest.TestCase):
    def test_create_from_valid_xml(self):
        valid_xml = open('test_files/Assessment_run_results.xml', 'rb').read()

        assessment_run_data = AssessmentRunData.from_etree(
            etree.XML(valid_xml).find('AssessmentRunData'))

        self.assertEqual('', assessment_run_data.RequestId)
        self.assertEqual("04f58082-605e-4bbc-b145-2610c4786c37",
                         assessment_run_data.AssessmentRunId)
        self.assertEqual("Site Blindado E-commerce",
                         assessment_run_data.AssessmentName)
        self.assertEqual("www.mydomain.com.br",
                         assessment_run_data.ApplicationName)
        self.assertEqual("f5cb1fa9-1e19-4557-a745-84f04d926c7d",
                         assessment_run_data.ApplicationId)
        self.assertEqual("https://www.mydomain.com.br/",
                         assessment_run_data.ApplicationUrl)

        self.assertIsInstance(assessment_run_data.AssessmentRunInfo,
                              AssessmentRunInfo)

        self.assertIsInstance(assessment_run_data.SmartAttacks,
                              SmartAttacks)

        self.assertIsInstance(assessment_run_data.PagesVisited,
                              PagesVisited)