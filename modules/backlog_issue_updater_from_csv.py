from pybacklogpy.Issue import Issue
import json
import csv

def csv_to_dictlist(filename):
	issuelist_csvfile = open('issue_114-115.csv')
	issuelist_csvdictobj = csv.DictReader(issuelist_csvfile)
	return issuelist_csvdictobj

def issue_updater(dictlist):
	# Issue API naming
	issue_api = Issue()


# for loop in issuelistdict and get isuue data via api
# for dict_keys in issuelist_csvdictobj:
# 	if dict_keys['issue_id'] != 'issue_id':
# 		response = issue_api.get_issue( issue_id_or_key = dict_keys['issue_id'] )
# 		issue_data = json.loads(response.text)
# 		issue_key = issue_data['issueKey']
# 		issue_summary = issue_data['summary']
# 		issue_description = issue_data['description']
# 		# print(issue_data)
# 		print("key: " + issue_key)
# 		print("summary: " + issue_summary)
# 		print("description: " + issue_description)
# 		print("------------------------------")

