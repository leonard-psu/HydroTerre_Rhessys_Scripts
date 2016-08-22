# HydroTerre_Rhessys_Scripts
Scripts to use HydroTerre and RHESSys


REQUIREMENTS 

PYTHON LIBRARIES

(1) EcohydroLib <br />
pip install EcohydroLib

(2) RHESSysWorkflows <br />
https://github.com/leonard-psu/RHESSysWorkflows#installation-instructions <br />
pip install rhessysworkflows<br />
 
(3) WGET <br />
apt-get install python-pip<br />
pip install wget<br />


INPUTS (LOCATED IN MAIN FILE FOR NOW)<br />

project_location = '/tmp'   ## Where you want the results to be placed, base folder.<br />
project_name = 'test15'     ## Project Name<br />
gageid = '01589312'         ## USGS GAGE ID<br />

start_date = '2008-01-01'   ## CLIMATE STATE DATE<br />
end_date = '2010-01-01'     ## CLIMATE END DATE<br />
rhessys_source_location = '/projects/rhessys'  ## RHESSys model source code location<br />
publisher = 'RHESSysWorkflow                   ## Text used to register LAI datasets<br />
