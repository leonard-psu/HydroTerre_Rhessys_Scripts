#!/usr/bin/python

import urllib, json, time
import wget
import sys

###############################################################################################
# Variables needed to run script
#
# <ht_huc12_id> i.e. '020503030105'  USGS level 12 HUC identification
# <ht_start_date> i.e. '2000-01-01'  Start date 
# <ht_end_date> i.e. '2001-01-01'    End date
# <output location> i.e. '/tmp' folder location to place zip file
###############################################################################################

def get_HydroTerre_Data_Bundle(ht_huc12_id, ht_start_date, ht_end_date, output_folder_location):

    try:
        url_result = ""
        check_interval=30

        ###############################################################################################
        # Call HydroTerre Service

        data = {'HUC_12_ID': ht_huc12_id,
                'Start_Date' : ht_start_date,
                'End_Date' : ht_end_date,
                'f': 'pjson'}

        taskUrl = "http://hydroterre.psu.edu:6080/arcgis/rest/services/RHESSys/HydroTerre_Rhessys/GPServer/HydroTerre_Rhessys"
        submitUrl = taskUrl + "/submitJob"

        submitResponse = urllib.urlopen(submitUrl, urllib.urlencode(data))   
        submitJson = json.loads(submitResponse.read())    

        ###############################################################################################
        # Check for HydroTerre Service results

        if 'jobId' in submitJson:  
            jobID = submitJson['jobId']        
            status = submitJson['jobStatus']        
            jobUrl = taskUrl + "/jobs/" + jobID            
                
            while status == "esriJobSubmitted" or status == "esriJobExecuting":
                print "checking to see if HydroTerre job is completed..."
                time.sleep(check_interval)
                
                jobResponse = urllib.urlopen(jobUrl, "f=json")     
                jobJson = json.loads(jobResponse.read())
             
                if 'jobStatus' in jobJson:  
                    status = jobJson['jobStatus']            
                 
                    if status == "esriJobSucceeded":                                        
                            if 'results' in jobJson:
                                resultsUrl = jobUrl + "/results/"
                                resultsJson = jobJson['results']
                                for paramName in resultsJson.keys():
                                    #print paramName
                                    resultUrl = resultsUrl + paramName                                        
                                    resultResponse = urllib.urlopen(resultUrl, "f=json")   
                                    resultJson = json.loads(resultResponse.read())                            
                                    #print resultJson['value']
                                    if paramName == 'Result_URL':
                                          url_result = resultJson['value']
                                #print resultsJson['Result_URL']
             
                            #print jobJson
                    if status == "esriJobFailed":                                        
                            if 'messages' in jobJson:                        
                                print jobJson['messages']
                                print 'HydroTerre job failed'
                                sys.exit(-100)
                                                   
        else:
            print "no HydroTerre jobId found in the response"
            sys.exit(-101)

        ###############################################################################################
        # Get HydroTerre Service Data Bundle

        print '--------Download Start-------------'
        print 'Retrieving result from: '+ url_result
        wget.download(url_result, out=output_folder_location)
        print '--------Download End-------------'
        ###############################################################################################

    except Exception,e:
        print str(e)
        

    return

###############################################################################################

def main(argv):

    ht_huc12_id = '020503030105'
    ht_start_date = '2000-01-01'
    ht_end_date = '2001-01-01'
    output_folder_location = '/tmp/'

    get_HydroTerre_Data_Bundle(ht_huc12_id,ht_start_date,ht_end_date,output_folder_location)

###############################################################################################

if __name__ == "__main__":
    main(sys.argv)

