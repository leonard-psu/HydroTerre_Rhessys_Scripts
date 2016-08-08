#!/usr/bin/python

import urllib, json, time
import wget
import sys
import os
import errno
import zipfile
import subprocess
import logging


###############################################################################################
# Function INPUTS 
#
# <XMin>  i.e. -76.838944 
# <YMin>  i.e. 39.340390
# <XMax>  i.e. -76.734944   
# <YMax>  i.e. 39.401764
#
# Function OUTPUTS
# <string> List of USGS HUC-12 keys (semi-colon separated)
###############################################################################################


def get_HUC12_IDs_from_Extent(XMin, YMin, XMax, YMax):

    try:
        huc_list_result = ""

        check_interval=30
        taskUrl = "http://hydroterre.psu.edu:6080/arcgis/rest/services/RHESSys/getHUC12sfromRHESSysWorkflows/GPServer/get_HUC12_IDs_from_Extent"

        ###############################################################################################
        # Call HydroTerre Service

        data = {'XMin': XMin,
                'YMin' : YMin,
                'XMax' : XMax,
                'YMax' : YMax,
                'f': 'pjson'}

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
                                    if paramName == 'Result_HUC12_List':
                                        huc_list_result = resultJson['value']
 
                                #print resultsJson['Result_HUC12_List']
             
                            #print jobJson

                    if status == "esriJobFailed":                                        
                            if 'messages' in jobJson:                        
                                print jobJson['messages']
                                print 'HydroTerre job failed get_HUC12_IDs_from_Extent'
                                sys.exit(-100)
                                                   
        else:
            print "no HydroTerre jobId found in the response get_HUC12_IDs_from_Extent"
            sys.exit(-101)

    except Exception,e:
        print str(e)
        

    return huc_list_result


###############################################################################################

def main(argv):


    XMin = -76.838944
    YMin = 39.340390
    XMax = -76.734944
    YMax = 39.401764

    huc12s = get_HUC12_IDs_from_Extent(XMin, YMin, XMax, YMax)
    print huc12s

###############################################################################################

if __name__ == "__main__":
    main(sys.argv)

