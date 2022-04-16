import requests
import json
import datetime

def getInspectors():
    res = []
    r_inspectors = requests.get('https://6244305b3da3ac772b0c7854.mockapi.io/fakeSolar/3rdParty/inspectors')
    #inspectors = json.loads(r_inspectors.json())
    inspectors_dict = {}
    inspectors = r_inspectors.json()
    inspectors = [inspectors_dict.update({x['id']: x['name']}) for x in inspectors]
    r_inspections = requests.get('https://6244305b3da3ac772b0c7854.mockapi.io/fakeSolar/3rdParty/inspections')
    inspections = r_inspections.json()
    for inspection in inspections:
        date = datetime.datetime.strptime(inspection['scheduledDate'].split('T')[0], '%Y-%m-%d')
        title = inspection['city'] + ' - ' + str(date.year) + '/' + str(date.month) + '/' + str(date.day)
        try:
            inspectorName = inspectors_dict[str(inspection['inspectorId'])]
        except:
            inspectorName = 'Not defined'
        itemsOK = 0
        issuesWarningCount = 0
        issuesCriticalCount = 0
        for item in inspection['items']:
            if item['isIssue'] == 'false':
                itemsOK += 1
            else:
                if item['severity'] < 60:
                    issuesWarningCount += 1
                else:
                    issuesCriticalCount += 1
        res.append({
            'title': title,
            'inspectorName': inspectorName,
            'itemsOk': itemsOK,
            'issuesWarningCount': issuesWarningCount,
            'issuesCriticalCount': issuesCriticalCount,
            'company': 'SolarGrade'
        })
    return res