import re
import ideasapp.settings as settings
from ideasapp.models import idea as ideaModel
from datetime import datetime

def formatHttpHeaders(headers):
    ''' formats http headers into a nasty long string because we're not using a document store
        NOT TESTED'''
    
    out = ""
    
    for key in headers.keys():
        out += "%s:%s;" %(key, headers[key])
    
    out.rstrip(";")
    
    return out

#------------------------------------------------------------------------------------------

def formatSubmitterEmail(user):
    ''' Checks whether the submitter's id is an email. If not appends a domain to it
        NOT TESTED'''

    # Email regex
    regex = re.compile(r"^([A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*)$")
    regOut = re.match(regex, user)

    if regOut:
        email = regOut.group(0)

    # J number regex
    regex = re.compile(r'^([a-zA-Z]\d{5})$')
    regOut = re.match(regex, user)

    if regOut:
        jNumber = regOut.group(1)
        email = jNumber + '@' + settings.emailDomain 
    else:
        email = None
        
    return email

#------------------------------------------------------------------------------------------

def ideasCloud(order):
    ''' Gets all ideas from db and returns them for rendering with some measure of how to render 
    Initially this rendering will be based on classification - higher class = bigger font'''
    #Pardsed in var in the field to order by for changing font

    #data = ideaModel.objects.order_by(order).values_list('idea_title', 'pub_date')
    #data = ideaModel.objects.values_list('idea_title', 'pub_date')
    data = ideaModel.objects.order_by(order).values_list('idea_title', 'pub_date')
    
    return data
#------------------------------------------------------------------------------------------
def getDate():
    return datetime.now()

#------------------------------------------------------------------------------------------
def saveIdea(ideaTitle, ideaText, ideaClassification, ideaHeaders):
    ''' Processes idea form data and saves data '''
    #import pdb
    #pdb.set_trace()    
    out = ideaModel(idea_title = ideaTitle, pub_date = getDate(), idea_text = ideaText, num_backers = 1, idea_classification = ideaClassification, idea_headers = ideaHeaders)
    out.save()
    return
#------------------------------------------------------------------------------------------
def loadTestData():
    #Loads test data for this app
    print 'Loading test data'
    '''    
    fh = open(settings.nounspth+'/'+settings.nounsfile,'r')
    words = []
    #Load into a list
    
    while fh.readline():
        words.append(fh.readline().rstrip('\r\n'))
    
    #Work through the fields, get type etc and poulate
    for field in ideaModel.objects.all():
        print field
    
    fields = ideaModel.objects.all()
    print fields
    for field in fields:
        print field
        #print field.get_internal_type(), field.max_length()
        
    
    fh.close()
    '''





