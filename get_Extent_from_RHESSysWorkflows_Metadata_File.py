#!/usr/bin/python


###############################################################################################
# Used for retaining workflow extent
#
class Extent(object):

    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0
    
    def __init__(self, min_x, min_y, max_x, max_y):
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y

    def __repr__(self):
        return "min x = " + str(self.min_x) + "\nmin y = " + str(self.min_y) + "\nmax x = " + str(self.max_x)  + "\nmax y = " + str(self.max_y) + "\n"


###############################################################################################
def get_Extent_from_RHESSysWorkflows_Metadata_File(metadata_file_and_path):

    try:
        
        extent_min_x = ''
        extent_max_x = ''
        extent_min_y = ''
        extent_max_y = ''

        f = open(metadata_file_and_path, 'r')
        lines = f.readlines()
        for line in lines:
            #print line
            fnd = line.find('bbox_wgs84 = ')
            if fnd == 0:
                #print line
                split1 = line.split(' = ') #BEWARE OF SPACES
                split2 = split1[1].replace('\n','').split(' ')
                #print split2
                extent_min_x = split2[0]
                extent_min_y = split2[1]
                extent_max_x = split2[2]
                extent_max_y = split2[3]


        result = Extent(extent_min_x,extent_min_y,extent_max_x,extent_max_y)
        return result
    except Exception,e:
        return str(e)



###############################################################################################

def main(argv):

    metadata_filename = '/tmp/test/standard/metadata.txt'
    my_extent = get_Extent_from_RHESSysWorkflows_Metadata_File(metadata_filename)
    print my_extent


###############################################################################################

if __name__ == "__main__":
    main(sys.argv)

