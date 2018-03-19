Python Trustwave Appscanner
===========================

Python Trustwave Appscanner transforms Appscanner REST API results into Plain Python Objects for easier processing.

Installation
------------

`pip install python-trustwave-appscanner`

Usage
-----

The library exposes some functions that can return Python objects representing the XML response, strings or booleans.

Simple functions that return strings or booleans include: `application_exists`, `get_application_id_by_name`, `assessment_exists`, `get_assessment_id_by_name`.

Complex functions that return objects are: `get_assessment_status`, `get_current_assessment_run_id`, `get_assessment_run_status`, `get_assessment_run_results`

Last but not least the is the execution function that queues an assessment for execution: `queue_assessment`
