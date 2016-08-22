# HydroTerre_Rhessys_Scripts
Scripts to use HydroTerre and RHESSys


REQUIREMENTS 

PYTHON LIBRARIES

(1) EcohydroLib 
pip install EcohydroLib

(2) RHESSysWorkflows
https://github.com/leonard-psu/RHESSysWorkflows#installation-instructions
pip install rhessysworkflows
 
(3) WGET
apt-get install python-pip
pip install wget


INPUTS (LOCATED IN MAIN FILE FOR NOW)

project_location = '/tmp'   ## Where you want the results to be placed, base folder.
project_name = 'test15'     ## Project Name
gageid = '01589312'         ## USGS GAGE ID

start_date = '2008-01-01'   ## CLIMATE STATE DATE
end_date = '2010-01-01'     ## CLIMATE END DATE
rhessys_source_location = '/projects/rhessys'  ## RHESSys model source code location
publisher = 'RHESSysWorkflow                   ## Text used to register LAI datasets
